<!--
.. title: 角膜的折射率
.. slug:  refractive_index_of_cornea
.. date: 2019-9-4 12:00:00 UTC+08:00
.. tags: ophthalmology
.. category: ophthalmology
.. link:
.. description:
.. type: text
-->

如果在眼科书或者眼科设备的说明书上查找, 会发现有两种角膜折射率

* n = 1.3375
* n = 1.376

真实的角膜折射率是1.376, 而1.3375是一个测量角膜K值时使用的**人为设定**的测量用折射率.

下面听我解释: 
<!-- TEASER_END -->

## K值有几个

所有计算人工晶体度数的公式, 都要用上角膜曲率K, 也就是角膜的屈光力. 比如最基本的SRK公式:

$$
Power= A - 0.9 K - 2.5 AL
$$

我们来看一下角膜的解剖，角膜都有两个面前表面和后表面，前后表面肯定不是完全平行的，那样的话角膜就没有屈光能力了，所以角膜前后表面是各自有一个屈光力的，那么应该有两个k值。

![p1](https://i.loli.net/2019/09/04/iy5URPQrwWBv8Cn.jpg)

但我们看最简单的SRK公式，这里面只有一个K值. 是不是有矛盾? 

这是因为这是一个合成的K值，是角膜前后表面的屈光力之和。

## 测量设备

对于大多数测量角膜曲率的仪器，比如角膜曲率计(我估计手动角膜曲率计的使用已经快失传了)，这里面包含了自动验光仪 和 IOL Master，都是测量角膜前表面的曲率半径，

如果用Plasicdo环原理测量的角膜地形图，就是那种可以看到一个一个圆环的那种角膜地形图，能够测量的也只是角膜的前表面。

因为他们的原理都是看一个图像在角膜前表面的反射像, 虽然角膜后表面也可能有反射像, 但是被前表面的反射像给遮挡了, 于是后表面的数据测不到.
![p2](https://i.loli.net/2019/09/04/xdnGSyH5Bs1WbmT.jpg)

测能够测量角膜后表面的设备并不多，

* 基于 scheimpflug原理的PentaCam、
* 使用Placido环和Scheimpflug原理的SIRIUS天狼星，
* 基于扫描的Obscan，
* 用点光源的Cassini，
* 还有前节OCT，

到2019年大概也就这几种。一个设备如果能够测量角膜后表面的曲率，一定会大张旗鼓地宣传的, 所以他们的海报上一定会有一个角膜的断面图.

![PentaCam](https://www.pentacam.com/fileadmin/_processed_/3/c/csm_General_Overview_16_9_EN_1.21r59_b2274acd47.png)

现在问题来了，角膜实际有两个面，K值应当是综合这两个面的，而现在只能测量一个面，那怎么办呢？

## 整合前后表面的K值

![屏幕快照 2019-09-04 11.28.17](https://i.loli.net/2019/09/04/ikwNxTdojR51yva.png)

这是从曲率半径算角膜屈光力的公式，如果是前后两个面，那么

![屏幕快照 2019-09-04 11.28.27](https://i.loli.net/2019/09/04/4S3cXB1C6FdPtvj.png)

为了只从前表面的数据得出整体的数据。人们假设前后表面的曲率半径是成比例变化的，于是可以把后表面的曲率半径写成前表面曲率半径乘个系数.

![屏幕快照 2019-09-04 11.34.18](https://i.loli.net/2019/09/04/sAJnFpXClGu4SBt.png)

把这个式子代入到前面公式中:

![屏幕快照 2019-09-04 11.28.38](https://i.loli.net/2019/09/04/kKx4sNUdImybvSD.png)

于是就可以把1/r提取出来，得到:

![p4](https://i.loli.net/2019/09/04/aQyz3riHhRweUbW.jpg)

这里面除了1/r都是常数, 加减乘除之后当然也是得到一个常数. 那么就可以直接用数值相等的常数等效替换之. 为了跟其他的光学公式一致. 于是写成:

![p5](https://i.loli.net/2019/09/04/5hZfYp4V3mugeBj.jpg)

这就是1.3375的来历. 是一个为了仅仅测量前表面就可以得到前后两个表面屈光力之和的权宜之计. 

至于为何等于1.3375, 因为前表面曲率半径=7.5mm时, 算出来的K值等于45.

## 1.3375的失效

当角膜前表面进行了屈光手术以后, 之前角膜后表面曲率半径与前表面曲率半径成比例的这个假设就不成立了. 虽然你仍然可以用角膜后表面的曲率半径去除前表面, 但每个做屈光手术的人切削的程度不同, 除出来的系数不再是一个常数了. 

由于基本的假设失效, 那么连带着后面的推导也就都失效了, 1.3375这个数值不再能够使用.

![p6](https://i.loli.net/2019/09/04/aTWvZVuxMtlDH5z.jpg)

## 影响

所以, 当一个做完了角膜屈光手术的病人来到你的面前. 即使你亲自动手给他测量了角膜曲率, 比如设备告诉你说K=40, 你也不能相信这个数据, 因为这个数据是从1.3375算出来的. 真实的K值, 很可能只有39.6左右. 

## IOL Master

研读[IOL Master的说明书](https://www.doctor-hill.com/physicians/docs/iolmaster_5-4.pdf), IOL master的测量结果可以显示为K值或者角膜曲率半径Radius.

![屏幕快照 2019-09-11 12.46.13](https://i.loli.net/2019/09/11/l3VUOfS8mXhsg92.png)

## 参考文献

* [Intraocular lens power calculation in eyes with previous corneal refractive surgery](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6053834/) 这是一篇2018年关于角膜屈光手术后人工晶体度数计算的综述, 作者是Giacomo Savini和 Kenneth J. Hoffer, 前面的名字可能不熟悉, 后面的Hoffer, 就是Hoffer Q公式的作者K.J. Hoffer

