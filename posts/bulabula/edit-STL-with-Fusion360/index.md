<!--
.. title: 用Fusion360编辑STL
.. slug: edit-STL-with-Fusion360
.. date: 2018-4-3 2:30 UTC+08:00
.. tags: 3D print
.. category:
.. link:
.. description:
.. type: text
-->

STL文件就像是PDF, 是面向打印机的. 难以编辑. 即使能够编辑, 面对大量的三角形, 运行速度也非常慢.

不过最近总算找到了用Fusion360的一点点技巧.

<!-- TEASER_END -->

1. 要打开首选项->预览->"网格"工作空间
![](https://i.loli.net/2018/04/03/5ac2756be46a2.png)

1. 插入网格, 或者使用"上传"STL文件.
![插入网格](https://i.loli.net/2018/04/03/5ac275c903dd1.png)
![插入网格2](https://i.loli.net/2018/04/03/5ac275c97231b.png)

1. 不捕获设计历史
![不捕获设计历史](https://i.loli.net/2018/04/03/5ac275cab7bff.png)

1. 右键选择网格对象, "Mesh到BRep", 转换成实体
![Mesh到BRep](https://i.loli.net/2018/04/03/5ac275ca15a81.png)

1. 铛铛, 变成实体了, 可以在各个面上编辑. 但明明是一个平面, 还是被分成了很多的三角形. 很不方便, 下面才是重点.
![很多三角形](https://i.loli.net/2018/04/03/5ac275c9e694b.png)


1. 随便找一个面进行"分割实体"的操作.
![分割实体](https://i.loli.net/2018/04/03/5ac275ca86ccb.png)
![任选一个面](https://i.loli.net/2018/04/03/5ac275ca84e6a.png)

1. 切完以后, 所有的平面突然就不再是一堆三角形了.
![三角形消失](https://i.loli.net/2018/04/03/5ac2780923f8c.png)

1. 然后在使用"合并", 将切开的实体合并在一起.
![合并](https://i.loli.net/2018/04/03/5ac2784911a66.png)
![到一起](https://i.loli.net/2018/04/03/5ac275ca4f95b.png)

1. 成品. 平面都得到了简化, 但曲面目前还没有办法. 记得完成以后把"捕获历史"的功能在再打开.
![成品](https://i.loli.net/2018/04/03/5ac27884f2f99.png)

最后, 号召一下. 如果设计的3D模型仅仅以STL或者其他网格形式发布, 就请尽量少用圆角吧. 谢谢!
