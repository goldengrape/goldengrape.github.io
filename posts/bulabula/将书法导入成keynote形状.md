<!--
.. title: 将书法导入成keynote形状
.. slug: import_calligraphy_to_keynote_as_shape
.. date: 2018-8-23 12:00 UTC+08:00
.. tags: mac
.. category:
.. link:
.. description:
.. type: text
-->

自己写的毛笔字仍然有诸多缺陷, 不过现代人的展示更多发生在幻灯片而不是宣纸上, 比如在做幻灯的时候用上自己写的字, 感觉很开心.

导入成Keynote形状以后, 多了许多后期调整的可能性. 很有意思.

![屏幕快照 2018-08-22 21.35.52](https://i.loli.net/2018/08/23/5b7e2d3ddb6f6.png)

先说说如何导入:

<!-- TEASER_END -->

1. 用手机上的[adobe caputre](https://www.adobe.com/products/capture.html)拍摄, 简单修饰形状. 这个app在android和iOS上都有.
2. 导出成SVG
3. 发送到电脑上, 如果是iOS对mac可以很简单使用airdrop.
4. 下载并安装 [SvgToKeynote](https://www.christianholz.net/keynote_utilities.html#svg2keynote)
5. 运行SvgToKeynote将SVG文件转换成keynote文件, 注意转换出来的是早期版本的keynote文件, 编辑或者存储时会提示升级, 升级就好了.
6. keynote文件内的图形就是“形状”了, 如果用右键点击可以出现“使可以编辑”, 就可以编辑顶点. 还可以“存储到我的形状”

Keynote形状, 或者说Keynote shape的好处是可以进行逻辑运算, 能够将两个形状进行融合/ 交叉/ 减少/ 排除, 于是可以比较方便地拆分各个组件.

在书法, 可以用编辑顶点的方法修改笔画的细节, 比如笔锋, 牵丝。 还可以将各个笔势分离开来, 调整裹束, 也就是间架结构.

如果有处理SVG的专业软件, 当然直接处理可能会更简单一些.

对于PowerPoint, 需要升级到office 365以后, 能够有convert to shape功能, 但我买的不是, 所以无法处理SVG.

对于PowerPoint,  原来有三种“图像”:

* 形状: 可以编辑顶点, 可以改变填充颜色, 是矢量图
* 图形: 不能编辑顶点, 可以改变填充颜色, 是矢量图
* 图片: 不能编辑顶点, 不能改变填充颜色, 是标量图

其中后两种在keynote里都作为图片处理. 在keynote中, 如果把文件导出成powerpoint文件, 那么形状->形状, 如果是在keynote中复制, 到powerpoint中粘贴, 是形状->图片.
