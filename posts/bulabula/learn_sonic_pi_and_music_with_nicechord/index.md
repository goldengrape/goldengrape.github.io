<!--
.. title: 看好和弦学音乐和sonic-pi
.. slug: learn_sonic_pi_and_music_with_nicechord
.. date: 2019-11-20 13:00 UTC+08:00
.. tags: 
.. category: 
.. link:
.. description:
.. type: text
-->

[Sonic-Pi](https://sonic-pi.net/)是一个用Ruby语言写的音乐编程工具, 可以使用代码来即兴“演奏”音乐. 所谓演奏,live coding music,  是可以在程序中修改代码, 随时更新, 使音乐发生变化. 有点像是用命令行的DJ. 比如[这个演出](http://player.bilibili.com/player.html?aid=74702936&cid=127783914&page=1)

不过学习Sonic-Pi就有两个内容要学习了, 一个是Ruby语言, 一个是音乐语言. 

* Ruby语言
    * Sonic-Pi本身使用的是Ruby语言, 用来编写音乐的也是Ruby的一个子集, Sonic-Pi自带的mehackit上有个快速上手的[中文教程](http://sonic-pi.mehackit.org/index_chs.html), 文字阅读困难的, 这里也有[视频教程](https://www.bilibili.com/video/av47554214)
    * 如果需要更复杂的功能, 可能需要加强Ruby语言的学习, 引入更多数据结构、函数定义之类. Ruby是个很流行的语言, 有大量的教程可以参考, 比如[30分钟的快速入门](https://www.yiibai.com/ruby/quick-start.html) 或者更完全一些的[教程](https://www.runoob.com/ruby/ruby-tutorial.html)
    * 对于Sonic-Pi, 简单的音乐或者midi处理, 似乎还用不到面向对象编程, 多数是面向过程的, 如果会其他的编程语言, 很容易学会.

* 音乐语言
    * 音乐语言就要复杂多了, 概括地说音乐只是模式涌现. 但为了让人类的大脑觉得好听, 还有很多的规律. 
    * 很多“学习音乐”的人, 比如我小时候学琴, 只是学习了乐器的演奏, 并没有学习用音乐来表达. 学习演奏类似于学习写字, 高等一点的类似于学习书法. 音乐则是类似文学, 至少要有一些写作的训练才行, 也就是乐理的学习.

好和弦([NiceChord](https://nicechord.com/))是一个台湾作曲家做的“作曲、編曲、即興和電腦音樂的 YouTube 教學頻道”, 从2014年到现在已经更新了200多集了. 每一集5-10分钟, 轻松有趣. 是很好的乐理课程. 

既然我同时在学习这两者, 我就干脆结合在一起学. 所以我对着好和弦的课程, 尽量给每一集写一段对应的Sonic-Pi代码. 目前写了10集左右, 如果我不太懒的话, 就持续更新. 

您可以将代码贴到sonic-pi的编辑器里然后运行, 就可以听到结果了. 推荐顺手改改其中的代码, 也许能够产生更好的效果. 

其中也有很多比较固定的音乐表达方式, 比如常用的和弦琶音生成、12小节蓝调. 我还可能会加入一些自己会的编程技巧, 比如马尔可夫链、状态转移之类. 

这些代码供抛砖引玉, 您可以直接拿到自己的sonic-pi音乐中.

项目地址: 
[https://github.com/goldengrape/sonic_pi_for_nice_chord](https://github.com/goldengrape/sonic_pi_for_nice_chord)