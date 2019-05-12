<!--
.. title: 齿条绘制
.. slug: rack_by_fusion360
.. date: 2019-05-12 8:00 UTC+08:00
.. tags: 
.. category: 3D print
.. link:
.. description:
.. type: text
-->

学会了绘制齿条rack。就是和齿轮配合，将圆周运动变换成直线运动的结构。

![rack](https://i.loli.net/2019/05/12/5cd767b4bdd0f.jpg)

<!-- TEASER_END -->

有一个[fusion360官方制作教程参考](https://knowledge.autodesk.com/support/fusion-360/learn-explore/caas/screencast/Main/Details/a7992d99-5d4d-48c2-b971-a86ba3014608.html)，但是我觉得绘制过程太麻烦。而且在实际使用中，要真实确定齿条和齿轮的具体位置，否则其他支架不好安装。

所以自己学习了一下齿轮的知识，齿轮的主要参数有3个：

* module：模数，这个描述了齿的大小
* 齿数：很好理解，一圈有多少个齿
* 压力角：也就是齿轮上每个齿的斜边角度。

module x 齿数 = 齿轮的“分度圆”直径

关于齿轮和齿条的知识，强烈推荐小原齿轮工业株式会社(暨KHK株式会社)制作的[《齿轮设计所需的齿轮基础知识》](https://khkgears.net/china/gearknowledge/index.html) 

这种在日常生活中无处不在，却又隐藏在后台，完全不懂也不影响工作学习生活的，无比有用又非常无用的知识，非常酷。

画齿条的原理：

两个齿轮之间的是按齿轮的“分度圆”来接触的，比如两个完全相等的齿轮互相咬合时，圆心相当于在分度圆的切线上是对称的。

如果把齿条看作一个直径无穷大的齿轮，那么也是以分度圆的切线作为对称线，将一个齿镜像即可。这就是画图的原理。

详细步骤请参考我放在SlideShare上的[幻灯](https://www.slideshare.net/goldengrape/draw-a-rack-with-fusion-360)。