<!--
.. title: 音乐编程
.. slug: music_coding
.. date: 2019-11-20 12:00 UTC+08:00
.. tags: 
.. category: 
.. link:
.. description:
.. type: text
-->

一个月前我买了一件电子乐器[artiphon instrument1](https://artiphon.com/), 然后就沉迷于音乐不能自拔. 

## sonic-pi

前几天重新翻看[好和弦](https://nicechord.com/), 其中[有一集](https://youtu.be/8nmSsjQgO7s?t=593)说到用各种开源或者免费的软件制作音乐, 里面提到了[sonic-pi](https://sonic-pi.net/), 说可以用写程序的方法做现场音乐演出. 

于是我就去下载了[sonic-pi](https://sonic-pi.net/)来玩, 确实很有趣. 可以play音符, 可以播放采样(sample), 也就是事先录制好的声音, 可以循环播放一组音符或者声音, 于是就有节拍、和弦, 还可以引入随机数, 可以产生变化的旋律. 还可以和midi硬件交互. 

我写了一段代码, 可以将我的[artiphon instrument1](https://artiphon.com/) 中的特别低的低音(反正平时很少用到), 映射到和弦上, 于是我就可以用一个键来演奏需要好几个手指扭来扭去才能弹出的和弦了.[代码](https://github.com/goldengrape/artiphon_gadget)

![](https://cdn.shopify.com/s/files/1/0229/7157/products/06_Connectivity_2eb1d183-14a2-48f3-98c0-ad7821be2f63_928x896.jpg?v=1569094989)

我开始以为这只是一个专门用来写音乐的语言, 随着学习的深入. 怎么看到了越来越多的编程内容, 数组、分支、循环甚至函数. 看完了基础教程以后, 感觉这就是个图灵完备的计算机语言啊. 搜索了一下sonic-pi的来历, 果然, 其实sonic-pi是Ruby语言的一个方言. 没想到我为了弹吉他偷懒, 居然顺手学了一多半Ruby.

## Live Coding Music

我对音乐编程更有兴趣了. 在github上搜了一下, 发现这个[Awesome Live Coding Music](https://github.com/pjagielski/awesome-live-coding-music)的列表.

* [SuperCollider](https://github.com/supercollider/supercollider/)  Smalltalk-like (SClang)
* [Sonic Pi](https://github.com/samaaron/sonic-pi)   Ruby
* [Overtone](https://github.com/overtone/overtone)  Clojure
* [Tidal](https://github.com/tidalcycles/Tidal)  Haskell
* [Alda](https://github.com/alda-lang/alda)  Alda/Clojure
* [Gibber](https://github.com/charlieroberts/Gibber) Javascript
* [Extempore](https://github.com/digego/extempore)  Scheme-like
* [FoxDot](https://github.com/Qirky/FoxDot) Python

大名鼎鼎的潮流解释型语言一网打尽呐, 艺术家们果然是技术先行者. 

感觉Live Coding Music非常适合儿童(/中老年)编程教育, 

* 语法循序渐进,
  * 从语法上, play声音的命令远远比print、cout要有趣得多, 又比画个GUI简单得多. 
  * 变量命名时, 音符本来就有do/re/mi,CDE, 123, 几类名字混在一起, 所以对变量应该比较容易理解.
  * loop和循环天然对应.
  * 函数/块完全是复用性出发. 
  * 多乐器、多音轨天然对应多线程.
  * 还有众多midi硬件、通讯问题
* 写出来的东西很容易出成就感
  * sonic-pi的口号是“没有错误, 只有机会”, 用在编程学习上, 不容易出现挫折感. 音乐这种东西, 规律出现了就不会太难听. 
  * 编程的结果是产生音乐, 可以录制成wav、mp3文件, 很容易分享. 即使在别人没有安装什么额外软件的条件下, 也可以播放成果. 当然也可以放在soundcloud这样的音乐作品分享网站上. 比如我按照好和弦的指导做的[这首伴奏](https://soundcloud.com/user-544914923/continuum-with-ghost-note). 炫耀是互联网第一生产力, 也可以用来督促学习.
* 编程技巧上, live coding对程序需求的修改又是大量、即时的, 演奏者自己就是个不断改需求的甲方, 所以慢慢各种编程技巧都会自然加入. 为了快速切换风格, 很可能要准备上各种设计模式. 

所以等我学完了Ruby(sonic-pi), 考虑把Clojure和一直没啃下来的JavaScript通过音乐来搞定. 

## 对冲式学习

* 我最近学习弹吉他, 为了偷懒学会了Ruby, 
* 我之前想研究书法的用笔, 虽然没搞定写书法的机械臂, 却好好练习了书法.
* 再往远想, 我高中时就是用Mathematica(那时候还是4.0, 现在都12了)写数学和物理作业. 

所以可以引入“对冲式学习”的概念: 同时学习两个东西, 互补没学好的风险, 其中:

* 一个是古老的对技巧要求很高的技艺, 比如乐器、书法、解数学物理题;
* 一个是现代的可自动重复的工具, 有可能降低前者的难度, 比如音乐编程、CNC、mathematica. 

两者同时学习, 反正学会其中一个就很有收获, 也可能慢慢两者都会了. 