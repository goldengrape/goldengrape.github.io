<!--
.. title: 公理设计笔记（1）
.. slug: axiomatic_design_note_1
.. date: 2019-07-17 18:00 UTC+08:00
.. tags: 设计
.. category: 
.. link:
.. description:
.. type: text
-->

一个夏日的上午，我在图书馆里闲逛（据@cxqn 说这是有闲阶级才能做的事情），偶遇一本[《公理设计》](https://book.douban.com/subject/1238993/)，看书名觉得好奇于是拿出来翻了翻，觉得内容不错。网上还可以找到一篇文献[《公理设计理论及其应用》](http://blog.sciencenet.cn/home.php?mod=attachment&id=40989) 做了一些基本介绍。

但看起来这是一门课了，所以估计会有公开课来讲解。于是上网搜了一下，还真是找到了[MFE 594 An Introduction to Axiomatic Design](https://www.youtube.com/playlist?list=PLMDNnNJK3B1UlhdIfsFaezkHWbofX7Blj)，有4节课，大约一共4个多小时，花了两天看完，再回来翻翻书，有一些收获，决定写一点笔记。

<!-- TEASER_END -->

首先从1862年11月13日的[一场海战](https://www.history.com/this-day-in-history/u-s-s-monitor-battles-c-s-s-virginia)讲起。这场海战“标志着蒸汽动力铁甲舰新时代的到来。”

南方C.S.S的Virginia号战舰，体型庞大，非常凶悍。已经击沉了两艘联邦军舰。北方U.S.S派出了Monitor号，一艘小得多的军舰。

![](https://www.battlefields.org/sites/default/files/styles/gallery_item/public/thumbnails/image/comparison-of-the-css_0.jpg)
图片来自https://www.battlefields.org/learn/galleries/battle-hampton-roads

CSS Virginia的特点除了大，还有就是都是固定炮塔，两侧和首位有很多门炮。而USS Monitor有一个可以旋转的炮台。

一条战舰需要满足两个功能：
* 调整航行方向
* 调整炮击方向

对于CSS Virginia，这两个功能需求是“耦合”couple 的，要改变炮击方向，就需要将船只转向。而对于USS Monitor，这两个功能需求则是“解耦合”decouple 的，航行方向与炮击方向无关，炮击方向可以独立调整。

于是Monitor一直尽量守在Virginia的射击死角攻击，而Virginia则必须不断绕开，于是就不断绕圈。这两条船打了4个小时，Virginia撤退了。

这是视频公开课上老师讲的一个有趣的例子。

可以引出设计公理的第一条：

>满足功能需求（Functional Requirements, FRs)的参数设计（Design Parameter, DPs) 应当要解耦合（decouple）
