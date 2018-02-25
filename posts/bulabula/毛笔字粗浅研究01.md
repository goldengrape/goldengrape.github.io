<!--
.. title: 毛笔字粗浅研究(1)--硬件搭建
.. slug: brush-pen-research-1-hardware
.. date: 2018-2-26 00:20 UTC+08:00
.. tags: Art
.. category:
.. link:
.. description:
.. type: text
-->

这是春节假期的娱乐项目. 我做了一个能够模仿手腕运动能力的绘图仪. 真正的快乐还是来自于创造的过程啊.

![brush](https://i.loli.net/2018/02/26/5a92e3ad29971.jpg)
<!-- TEASER_END -->

主体的部分来自于[makeblock的xy plot](http://learn.makeblock.com/cn/xy-plotter-robot-kit/). 在此称赞一下makeblock的机械部分, 铝制的框架比小时候玩的上海玩具十七厂的"创"系列要精巧不少, 而且设计上也要好很多. 精度和强度也高出不少. 我觉得在某些情况下甚至可以考虑直接用到光学平台上了.

原作的绘图仪有两个步进电机和一个舵机控制, 步进电机控制xy平面上的移动, 舵机控制笔的抬起和放下.

![xy plotter](http://learn.makeblock.com/cn/wp-content/uploads/2016/01/KM2EQ92AMSKANCMBV8.png)

这个结构用来写钢笔字是可以的, 因为并不需要控制笔管的方向. 但写毛笔字不够, 如前一篇[毛笔字粗浅研究00](../brush-pen-research-0)中所描述的, 在写毛笔字时要通过手腕的运动, 控制毛笔的倾倒, 以使笔锋能够行走在笔画的中央.
![侧锋](/images/侧锋.png)

所以, 除了笔管在xy方向上的运动, 还需要能够控制笔管的倾侧. 当然笔在运行时还有轻重, 也就是在z轴方向的运动.

于是, 执笔的部分是这样的:

![执笔 v51](https://i.loli.net/2018/02/26/5a92ecc591527.png)

由3个舵机来控制, 最上方的舵机配合一个齿轮来控制z轴的运动,下方是由两个舵机组成的两自由度控制部分, 这样笔管就可以向各个方向倾倒. 整体再通过螺丝连接到xy plotter的其他部分上(青色的梁).

需要控制的电机一共有5个:

* 两个步进电机控制xy平面上的运动.
* 三个舵机控制笔管的倾斜和z轴的运动.

对比一下其他常见的机械臂, 一般最少也是6个自由度的.
![6 DOF](https://upload.wikimedia.org/wikipedia/commons/thumb/9/9b/Robot_arm_model_1.png/640px-Robot_arm_model_1.png)

那么缺少的是什么呢? 仔细看一下, 会发现没有毛笔的笔管绕自身长轴的旋转. 在[黄简讲书法课程](https://www.youtube.com/playlist?list=PL54cajc78e_S8g1Ow2r3epz9GfDLu6iKT)中, 要求对笔的控制是[通过手腕而不是手指](https://youtu.be/F6-fEdG6n48?list=PL54cajc78e_S8g1Ow2r3epz9GfDLu6iKT&t=760), 如果使用手指, 那么就可以在一定范围内完成笔管绕自身长轴的旋转, 大约有+/-90度, 如果禁止, 那么就丢失了一个自由度.
![屏幕快照 2018-02-26 01.13.48](https://i.loli.net/2018/02/26/5a92eef28774b.png)

[3D模型下载](https://grabcad.com/library/chinese-brush-holder-1)

实际操作中, 稳定z轴移动的两个圆柱不是打印的, 而是用纸卷的, 其实用A4纸裁好尺寸, 然后卷成足够紧密的纸卷, 外表再用胶带粘好, 还是很结实的, 而且表面光滑, 比打印一个轴效果更好.


<!-- EOF -->
