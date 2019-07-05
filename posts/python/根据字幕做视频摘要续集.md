<!--
.. title: 根据字幕做视频摘要续集
.. slug: video_keynote_2
.. date: 2019-07-05 12:00 UTC+08:00
.. tags: 
.. category: python
.. link:
.. description:
.. type: text
-->

我又继续做奇怪的小工具了。上一次做完了[根据字幕做视频摘要](https://goldengrape.github.io/posts/python/video_keynote/)之后，仍然不太满意，因为那个工具只是面向youtube的，对于本地的视频，或者是下载到本地的视频课程，仍然不够好用。所以我做了一些修改，已经[发布到了github上](https://github.com/goldengrape/video_keynotes)

现在可以先通过[coursera-dl](https://github.com/coursera-dl/coursera-dl)下载整个课程，然后再通过字幕划出重点，生成复习用的视频摘要。

<!-- TEASER_END -->
# 使用

* 需先下载课程视频和字幕文件
    * coursera上的课程可以使用[coursera-dl](https://github.com/coursera-dl/coursera-dl)进行下载。注意其中的[china-issues](https://github.com/coursera-dl/coursera-dl#china-issues), 可能需要通过VPN才能正常访问国际互联网。
        * 使用coursera-dl下载出现"HTTPError:400"问题，请参考[此解决方案](https://github.com/coursera-dl/coursera-dl/issues/702#issuecomment-506929946)
    * Youtube上的课程，例如OCW，可以使用[youtube-dl](https://rg3.github.io/youtube-dl/)进行下载。注意需要将对应的字幕也下载下来
* 将字幕文件处理成txt脚本
    * 处理单个文件：``` python sub2txt.py -i <subtitle file name>```
    * 处理整个目录：``` python sub2txt.py -p <path>```
* 手动编辑txt脚本，将你认为不重要的部分删除后保存，尽量不要修改txt文件名
* 按编辑后的txt脚本剪辑视频课程：
    * 处理单个文件：```python clip_by_txt.py -t <txt file>```
    * 处理整个目录：```python clip_by_txt.py -p <path>```

剪辑完成的视频将以summary_开头，存储在视频课程原位，并且附带有srt的字幕。

# Demo

这是一个剪辑自coursera上的learning how to learn课程第一周第一课[introduction-to-the-focused-and-diffuse-modes](https://www.coursera.org/learn/learning-how-to-learn/lecture/75EsZ/introduction-to-the-focused-and-diffuse-modes) 

* [Youtube视频](https://www.youtube.com/embed/UjkYY6HUSyY)

# 其他

似乎用来剪辑电影也会很方便吧。

说到剪辑电影，我还发现了一个有趣的工具[videogrep](https://antiboredom.github.io/videogrep/)，与我做的工具类似，但他是在字幕中检索关键词或者使用正则表达式来检索，效果惊艳：
[All the instances of the phrase “time” in the movie “In Time”](https://www.youtube.com/watch?v=PQMzOUeprlk)

