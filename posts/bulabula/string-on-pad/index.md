<!--
.. title: iPad上的琴弦
.. slug: string-on-pad
.. date: 2018-3-20 12:00 UTC+08:00
.. tags: python
.. category: python
.. link:
.. description:
.. type: text
-->

前一段时间玩Ukulele. 真不知道人类怎么想的, 用手指头去按又硬又粗的琴弦. 每次练琴都恨不得把手指勒出几个槽来. 实在是不爽, 于是放弃了, 吉他什么的也一并拉黑. 大约从小我就和弦乐或者半弦乐有仇.

不过弄出有意思的声音还是我有兴趣做的事情. 于是就有了在iPad上做一把Ukulele的项目:
![ipadminiukulele](https://i.loli.net/2018/03/20/5ab08921c906d.gif)

这把琴是有琴弦的, 琴弦能够给人有触觉反馈, 在乐器演奏是还是很重要的. 琴弦使用的是鱼线, 线绷紧的力度可调. 这样不至于勒手. 仅仅按住琴弦还是不响的, 要在拨弦的时候iPad才会发出声音.

<!-- TEASER_END -->

# 硬件部分

很简单的两个打印件, 可以卡住iPad两端.
![手机琴新版 v15](https://i.loli.net/2018/03/20/5ab08b60e5759.png)

从淘宝几块钱买来一个吉他调弦钮, 安在圆孔里. 把鱼线4个弦槽穿过, 然后绑在吉他调弦钮上, 线要从iPad前后绕过, 这样才能稳定. 线的长度要试试, 大约是iPad长度的7-9倍. 装上的时候可以很松, 然后通过调弦钮逐渐拉紧.

如果喜欢Ukulele/吉他这类半弦乐中横隔的手感, 可以在鱼线上打结, 或者在基本调好线的松紧之后穿入几根牙签.

琴弦应该放在iPad的右侧. 要和相应的app位置匹配.

打印件已经[存放在Thingiverse. ](https://www.thingiverse.com/thing:2832687)

# 软件部分

这部分代码是用的iPad上的[Pythonista 3](http://omz-software.com/pythonista/)写的, 这大概是唯一能够在ipad上写出可执行python脚本的工具了.

Pythonista自带里有个钢琴的demo, 演示多点触控, Ukulele是一样的, 只是要把按键和拨弦两件事情分开, 按键的时候把音高确定好, 拨弦的时候再调出该弦的声音进行播放.

遗憾的是Pythonista里的sound库只有钢琴的声音, 音域的范围也很有限. 于是做出来的是一把拨弦钢琴了.

[代码在此](../../../code/iPad-Ukulele/Ukulele.py)












<!-- EOF -->
----
[press.one签名](https://press.one/file/v?s=3bf28f812a1c1308b7942dd424cf4114c7cd2241038b3df453038fcdde5f7561b345a77b2b9879b84cb6ab3601d1bce58f8e31dad3110e79912e1c179209f8811&h=01f31dd17b0af32cca3bc8cdb4c450b59c5c6812749b31c2e4632073cb14dcdb&a=79c1846bc532ec0cf61ad0f1f5604a80a1387aca&f=P1&v=2)
