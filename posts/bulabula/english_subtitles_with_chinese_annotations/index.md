<!--
.. title: 英文字幕加单词注释
.. slug: english_subtitles_with_chinese_annotations
.. date: 2019-12-23 10:00 UTC+08:00
.. tags: 
.. category: 
.. link:
.. description:
.. type: text
-->

写了一小段代码, 给英文字幕里的生词加上中文解释. 效果如图所示:
![The.Expanse.S04E01.New.Terra.1080p.AMZN.WEB-DL.DDP5.1.H.264-NTG-0005](https://i.loli.net/2019/12/23/Dfg8w9snSizWhMk.png)

> 1,300 habitable(可居住) systems(系统) on the other side of those rings(环).

<!-- TEASER_END -->

大家看剧的时候都是打着学英语的旗号, 但显然现在都是等着有中文字幕的“熟肉”出了以后再看. 甚至Amazon、Netflix还直接提供了多数语种的字幕. 于是我练就的是潜意识读取中文字幕并且在脑中自动中文播出的本领, 而听力、单词量其实没啥提高.

不久前, 我作为海淀家长的同学, 被刺激了. 现在二三年级的小朋友可以达到什么KET、PET、FCE的英语水平, 查了一下大概至少是大学英语4级, 可能相当于雅思5-7分了. 说人家小朋友也是看剧, 哈利波特刷好几遍, 都能背了. (我还啃不下哈利波特的生肉, 深受刺激.)  

不久前, 还看到了[tinyfool](https://twitter.com/tinyfool)的“英语轻松读”[android版](https://tiny4.org/enreaderapk.apk), [iOS版](https://apps.apple.com/cn/app/%E8%8B%B1%E8%AF%AD%E8%BD%BB%E6%9D%BE%E8%AF%BB/id1471605122) 感觉这种在字里行间直接加单词解释的界面真好. 视线没有大幅度地跳动, 
![WechatIMG5](https://i.loli.net/2019/12/23/PIm5woSckXNvtUE.png)

所以我也想在看剧的时候也加一个这样的功能, 在字幕里加上生词的中文解释.

既然想到, 看起来也不是个大工程, 就利用周末动手写一下. 

其中单词词义的选择是个小难题, 比如:
>They even(甚至) understand(懂) ophthalmology(眼科学)

其中even如果直接调用字典得到的解释是:
>>a. 平坦的, 相等的, 连贯的, 均等的, 公平的, 偶数的, 平均的, 平衡的, 恰好的
vt. 使平坦, 使相等
vi. 变平, 成为相等
adv. 甚至, 实际上, 完全, 十分
n. 偶数, 偶校验
[计] 偶数, 偶校验

从这么多词义中选择出找到正确的词义“甚至”, 而没有翻译成“平坦”或者“偶数”之类. 还是要一点小技巧的. 

咨询了一下本领域的专家:
>目前的NMT都是会把句子先做encoding变成高维向量，然后做decoding时，依据上下文（时间序列，和注意力机制等）来决定当前词该如何翻译。所以，每个词的翻译是由上下文语义决定的。（虽然不完美）

>你这个场景，用现有NMT的架构，稍加改动，可以完成。

翻译一下: 我的高龄电脑跑不动.

我用的方案是:

* 先找到句子的机器翻译, 
* 然后再找到单词的翻译, 
* 最后找到这两个翻译中最长的公共字符串. 

简单粗暴高概率有效.

目前使用的机器翻译API是[彩云小译](https://open.caiyunapp.com/%E4%BA%94%E5%88%86%E9%92%9F%E5%AD%A6%E4%BC%9A%E5%BD%A9%E4%BA%91%E5%B0%8F%E8%AF%91_API), 免费版提供了每月翻译100万字符数的额度, 没有优化的前提下一个字幕文件用了20863字符.

于是就做出来了. 
[代码在这里](https://github.com/goldengrape/Partial-English-Subtitle-Translation)
需要您自己去[彩云科技开放平台](https://dashboard.caiyunapp.com/user/sign_in/)注册账号，申请开通小译Token.


[结果样例在这里](https://github.com/goldengrape/Partial-English-Subtitle-Translation/blob/master/my_subtitles_edited.srt)
结果样例是The expanse s04e01的字幕注释, srt格式, 下载下来在播放器里播放视频时加载就好了, 其中"生词"的定义以下满足3项: 

* 托福雅思GRE; 
* collins<=2星;
* 英国国家语料库词频顺序bnc>5000; 
* 当代语料库词频顺序frq>5000;

程序里还有些小bug, 比如we're-> were之类, 还有可以优化的地方, 能够降低API翻译的用量.  后续还会继续修改, 仅作为抛砖引玉用. 