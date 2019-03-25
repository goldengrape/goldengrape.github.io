
# coding: utf-8

# 周末做了一个奇怪的小东西.
# 
# 一个根据字幕来做出视频缩略版的工具, 效果参见[李永乐老师讲柏拉图立体的复习缩略版](https://www.youtube.com/watch?v=wxlySg9TBBI)
# 
# <iframe width="560" height="315" src="https://www.youtube.com/embed/wxlySg9TBBI" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
# 
# 这是一段remix的视频, 是从[李永乐老师讲柏拉图立体](https://www.youtube.com/watch?v=m9AE_G_9c7Y) 的课程中节选了数学概念的部分, 去掉了推导与展开的部分. 原视频大约12分钟, 剪辑后的视频只有4分钟. 可以方便用来快速复习概念. 
# 
# <!-- TEASER_END -->

# 过程是这样的, 先从youtube下载某个视频的字幕, 然后你可以对字幕进行编辑, 删去不重要的部分, 只留下需要保留的文字, 但注意仍然要保留原来的换行. 然后程序会自动在字幕中查找保留文字, 并找到对应的时间. 把对应时间的视频片段下载下来, 连成一体.
# 
# 这个程序最好是在Google Colab上运行, 在本地电脑上运行要令终端也可以__正常访问国际互联网__ 本文的[代码在github上](https://github.com/goldengrape/goldengrape.github.io/blob/master/posts/python/video_keynote/index.ipynb), 可以上传至[google colab](https://colab.research.google.com/)中运行

# 这个程序依赖于[webvtt-py](https://webvtt-py.readthedocs.io/en/latest/)、[youtube-dl](https://rg3.github.io/youtube-dl/) 和 [ffmpeg](https://ffmpeg.org/) , 当然还有[pandas](https://pandas.pydata.org/)
# 
# 注意在Google Colab上, webvtt-py和youtube-dl都是需要每次安装的. 

# In[4]:


try:
    import webvtt
except:
    get_ipython().system('pip install webvtt-py')
    import webvtt
try:
    import youtube_dl
except:
    get_ipython().system('pip install youtube_dl')
    import youtube_dl
import pandas as pd
import os, subprocess, difflib


# # 下载youtube视频字幕
# 
# 首先是要下载youtube上的视频字幕, youtube的字幕有两类, 一是作者自己上传的文字字幕, 一是由youtube进行语音识别后生成的自动字幕, 其中自动字幕又会被机器翻译成各种语言. 
# 
# youtube字幕是一种叫做WebVTT的格式, 可以使用youtube-dl进行下载. 虽然youtube-dl有python运行方式, 但我还不能熟练掌握, 于是使用了subprocess.call运行命令行进行下载.
# 
# 如果是下载自动字幕, 要使用`--write-auto-sub`, 如果是下载作者上传的字幕, 则是`--write-sub`, 下载字幕的时候, 我觉得并不需要将视频也下载下来, 所以要使用`--skip-download`, 字幕的语言简体中文=zh-Hans, 英文=en

# In[5]:


def download_youtube_sub(youtube_url,out_filename, lang="zh-Hans"):
    vtt_command = ['youtube-dl',
               '--write-auto-sub', # 如果下载作者自制的字幕则使用--write-sub
               '--sub-lang', lang, # 选择语言
               '--skip-download',  # 不下载视频, 只下载字幕
               '--no-continue',    # 强制覆盖已经下载的文件
                   youtube_url,
              '--output', out_filename] # 输出文件名格式
    # final out filename=out_filename+lang+'.vtt'
    p=subprocess.call(vtt_command, shell=False, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    if p!=0:
        print(p.stdout.decode("utf-8"))
    else:
        return True


# # 清理vtt字幕
# 
# vtt的字幕, 是一种还挺丰富(=复杂)的字幕格式, 里面不仅仅是时间戳和文字, 文字里可以加入丰富的特效.  特别是英文版本的vtt字幕, 为了表现出连贯的效果, 会把当前行与下一行字幕都显示出来, 于是每一句话其实记录了两次(中文似乎没有). 所以要进行一点清理. 将重复的部分删去. 只保留当前说的一句话, 和这句话的起止时间戳. 保存到一个pandas Dataframe里. 毕竟pandas后期好处理

# In[6]:


def clean_vtt(vtt):
    lines = []
    starts = []
    ends = []
    for line in vtt:
        extend_text=line.text.strip().splitlines()
        repeat=len(extend_text)
        lines.extend(extend_text)
        starts.extend([line.start] * repeat)
        ends.extend([line.end] * repeat)

    previous = None
    new_lines=[]
    new_starts=[]
    new_ends=[]

    for l,s,e in zip(lines,starts,ends):
        if l == previous:
            continue
        else:
            new_lines.append(l)
            new_starts.append(s)
            new_ends.append(e)
            previous = l

    df={"start":new_starts,"end":new_ends,"text":new_lines}
    df=pd.DataFrame(df)
    return df


# # 合并vtt字幕成为脚本
# 
# 无他, 一行一句, 保留换行之后比较好看也好编辑. 

# In[7]:


def vtt_to_transcript(vtt):
    df=clean_vtt(vtt)
    transcript="\n".join(df["text"])
    return transcript


# # 在字幕中找到对应的句子
# 
# 给定一句话, 要在字幕中找到这一句话的时间戳, 这样才能按照时间对视频切片. python的标准库里有一个difflib, 专门用来比较, 其中我使用的是get_close_matches, 找到最接近的文字. 这样即使只截取了一句话中的一部分, 也有可能找到相应的话语. 
# 
# 考虑到给定的一句话, 一定是从字幕中提取出来, 所以没有考虑找不到的情况. 
# 
# 使用pandas的优点在此显现, 只需要merge两个数据库, 就可以把相同字段, 相同内容的部分求出交集, 这样就可以获得时间戳了. 
# 
# (在这里记录url, 是为了日后扩展成从多个字幕中找句子, 那时就要记录每个字幕从哪里来的, 这是后话, 暂时还没有开始)

# In[8]:


def find_text_in_vtt(text,vtt,youtube_url):
    df=clean_vtt(vtt)
    df["url"]=youtube_url
    chosen_text=[]
    for t in text.splitlines():
        sentence=difflib.get_close_matches(t,df["text"],n=1)
        if sentence:
            chosen_text.extend(sentence)
    df_chosen=pd.DataFrame(chosen_text,columns=["text"])
    df_chosen=df_chosen.merge(df)
    return df_chosen


# 以上就是处理字幕的部分.
# 
# 还是以李永乐老师讲课的视频为例, 这堂课的字幕内容

# In[11]:


if __name__=="__main__":
    youtube_url='https://www.youtube.com/watch?v=m9AE_G_9c7Y'
    vtt_pre="test"
    lang='zh-Hans'
    vtt_filename='.'.join([vtt_pre,lang,"vtt"])
    download_youtube_sub(youtube_url,vtt_pre, lang=lang)
    
    vtt=webvtt.read(vtt_filename)
    print(vtt_to_transcript(vtt)[:100]) #blog中只显示100个字符


# # 手工选择必要的关键部分
# 
# 对, 这个程序做不到人工智能, 只有手工智能, 我怎么知道你觉得那一部分更重要, 所以请复制粘贴上面打印出来的字幕, 然后删掉其中不想要的部分, 保留下需要的, 注意不要改变换行的方式.

# In[13]:


if __name__=="__main__":
    keynote='''
什么叫柏拉图立体呢
他提出正多面体只有五种
所以我们就把正多面体称为柏拉图立体
首先它必须每一个面… 它是个正多面体
每个面都是同样的正多边形
除此之外 它还有一个要求
就是每个顶点的情况必须是相同的
比如说如果每一个顶点都连接三条棱
那所有顶点都必须是这样
然后你如果把这个图形稍微转一个方向
你会发现所有顶点都会跟以前重合
这个就叫每个顶点的情况是相同的
我们就把这种立体称之为正多面体
或者叫柏拉图立体
我们现在想证明一下 正多面体只有五种
首先我们先来看由正三角形所组成的
我们知道三角形每一个内角是60度
'''


# 然后我们就可以给出一句话的起止时间了: 

# In[14]:


if __name__=="__main__":
    df=find_text_in_vtt(keynote,vtt,youtube_url)
    print(df.head())


# # 下载youtube片段
# 
# 根据上面获得的起止时间, 去下载youtube视频中的片段. 很遗憾, youtube-dl虽然可以方便下载youtube视频, 但却无法只下载某个片段. 所以这里有两个事情要做:
# 
# * 获得真实的youtube视频文件地址. 真正的视频文件并不是你看到的www.youtube.com/watch?v=m9AE_G_9c7Y 而是一个带有签名的超复杂地址, 我猜测可能还会在不同电脑或者不同时间段有变化. 但YouTube-dl是能够获得这个地址的, 方便起见, 我直接抓取的是视频+音频合并的格式. 此时也不必下载视频.
# * 通过ffmpeg下载视频片段, ffmpeg的`-ss -to`可以设定起止时间, 但如果直接使用起止时间, 应当用`-copyts`来强制使用原始视频的绝对时间. 而且`-ss`放在`-i`之前还是之后,也有不少学问. 具体请参考https://trac.ffmpeg.org/wiki/Seeking
# 
# 这里使用了x264和mp3分别对视频和音频进行了重新编码, 导致速度较慢. 理论上可以使用“copy”, 但实测发现因为每个片段都很短, 高概率丢失关键帧, 所以不重新编码的话, 很有可能画面是静止的. 
# 
# 虽然ffmpeg也有python的处理版本, 但是那个库也是生成了ffmpeg的命令行, 还要学一堆他自定的语法, 还不如我直接用subprocess.run呢

# In[15]:


def download_part_youtube(video_url, start, end,output_filename):
    with youtube_dl.YoutubeDL({'format': '22'}) as ydl:
        info_dict = ydl.extract_info(video_url, download=False)
        real_video_url = info_dict.get("url", None)

    ffmpeg_command=['ffmpeg',
     '-ss',start,
     '-i',
     real_video_url,
     '-to', end,
     '-c:v', 'libx264', '-c:a', 'libmp3lame', #视频重编码使用x264, 音频重编码使用mp3
     '-copyts', # 强制使用原视频的绝对时间
     '-y', # 强制覆盖
     output_filename]
    p=subprocess.run(ffmpeg_command, shell=False, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    return(p.stdout.decode("utf-8"))


# # 根据文字截取视频片段并合并
# 
# 这就是把前面的准备工作合并到一起了, 根据摘取的数据库中的url、起止时间, 去到每个url中下载起止时间的视频片段. 这些视频片段都下载到了本地, 将文件名写入一个txt文件进行记录. 然后使用ffmpeg的concat功能将txt文件中的文件合并成一个视频文件. 最后再打扫一下临时文件, 就大功告成了. 
# 

# In[16]:


def get_youtube_by_keynote(df, final_output):
    #临时文件命名, 记录临时文件列表
    temp_file_list=["tmp_{}.mp4".format(index) for index in range(len(df))]
    temp_input='tmp_input_files.txt'
    with open(temp_input,'w') as f:
        for index in range(len(df)):
            f.write("file '{}'\n".format(temp_file_list[index]))    

    
    # 遍历数据库, 下载每个视频片段
    for index, row in df.iterrows():
        download_part_youtube(row.url, row.start, row.end,temp_file_list[index])
    
    # 将临时文件合并起来
    ff_concat_command=["ffmpeg", 
                   '-f','concat',
                   '-safe','0',
                   '-i', temp_input,
                   '-c:v', 'copy', '-c:a', 'copy', '-copyts', #合并似乎不需要重新编码
                   '-y',
                   final_output
                   ]
    subprocess.run(ff_concat_command, shell=False)
    # 打扫临时文件
    os.remove(temp_input)
    for f in temp_file_list:
        os.remove(f)


# 合并到一起, 如果是在本地运行, 只需要找本地目录中的内容. 如果是放在colab上, 下载文件是要调用google.colab库中的file.download函数

# In[ ]:


if __name__=="__main__":
    df=find_text_in_vtt(keynote,vtt,youtube_url)
    final_output="final.mp4"
    get_youtube_by_keynote(df, final_output)
    
    # download from google colab
    try:
        from google.colab import files
        files.download(final_output)
    except:
        print("not in google colab")


# # 使用与进一步改进
# 
# 这个小工具可以用来制作公开课的快速复习视频. 比如OCW, deeplearning.ai中的课程, 都是放在youtube上的. 一些上过的课时间一久就该忘了, 太可惜了. 但完全重看一遍又没有必要, 如果用此方法可以制作出快速复习视频. 只需要很短的时间就可以唤起回忆. 
# 
# 另一个可能的诡异应用是, 我也可以不视频字幕中的文字, 而是自己撰写一些常用的语句, 如果difflib.get_close_matches能够找到接近的语句, 就可以摘取下来. 那么给定一组视频, 比如某个总统的演讲视频. 也可以制作出一份“断章取义”的视频来. 当然每句话之间是断断续续, 背景也可能不断转换. 但可能很有趣吧. 这个功能需要对查找的部分进行一些修改, 以后有时间再进行了.
