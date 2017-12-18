<!--
.. title: 为什么对比敏感度的视标亮度是正弦变化的？(4)
.. slug: wei-shi-yao-dui-bi-min-gan-du-de-shi-biao-liang-du-shi-zheng-xian-bian-hua-de-4
.. date: 2017-12-19 01:10:00 UTC+08:00
.. tags: CSF, 教程, 现代眼科医生知识扩展包
.. category: ophthalmology
.. link:
.. description:
.. type: text
-->
正如侦探小说里凶手都是出场人物，数学、物理题里出现的条件都是要用上的，前面讲到的Eigenfunction显然和“为什么对比敏感度的视标亮度是正弦变化的“是直接相关的。

因为，正弦函数sin(x)、余弦函数cos(x)，更准确的说是
$$
e^{ix}
$$



其实就是某种Eigenfunction，甚至，是任意线性不变系统的Eigenfunction。

看这思路，人眼的光学成像近似是线性空间不变系统，如果有个函数是任意线性不变系统的Eigenfunction，那么必然也是人眼光学成像的Eigenfunction。

Otto. H. Schade在1956年把正弦视标引入眼科检查的时候，到底是怎么把这么远的两个概念结合到一起的？

为什么对比敏感度的视标亮度是正弦变化的？

因为正弦函数是线性不变系统的本征函数！

但是，为什么要用Eigenfunction，这得从对比敏感度讲起。

# 对比敏感度
这得从对比敏感度讲起。对比敏感度的检查方法是让患者看圆形的视标，视标中的条纹亮度按正弦变化，背景的亮度=视标的平均亮度。要求被试指出视标条纹的方向。

对比敏感度的报告是一张二维图片，也就是说有两个参数，一个是空间频率，一个是对比度。

对比敏感度测量的就是在不同空间频率下，眼睛可以看到的最低对比度是多少。




这张图水平方向是空间频率越来越高，垂直方向是对比度越来越低，是不是可以感觉到一个抛物线的痕迹，抛物线的上方是一片灰色，下面是有条纹的。

如果是sin变化的视标，那么对比度和空间频率都是可以算出来的。


三角函数的表示还记得吧，如果亮度的变化可以用 I(x) =A sin(B x )+C 来表示，

对比度contrast：

sin是在-1和+1直接变化，所以最大的亮度是Imax=A+C，最小的亮度Imin=-A+C。根据对比度的定义

contrast=(Imax-Imin)/(Imax+lmin)

contrast=2A/2C=A/C

空间频率frequency
就是在单位长度内，周期重复了多少次。显然B x=2kπ 的时候会重复，把x=1代入，B=2kπ, k=B/2π，所以空间频率

frequency=B/2π

前面说到，对比敏感度测量的时候，要给定一个空间频率，然后测量人眼分辨对比度的能力。如果给好了一个空间频率，而通过眼睛的屈光间质折射以后，空间频率变化了，就不好办了。

那么就是说一个视标图像，在经过任意像差的角膜、晶状体，在视网膜上成像以后，它的空间频率应当和经过一个理想无像差的眼睛一样，而对比度会有不同。

《为什么对比敏感度的视标亮度是正弦变化的》目录

0. 历史：http://www.15yan.com/story/jyk5ox6LzNF/

1.线性系统：http://www.15yan.com/story/36DkAcLTFcf/

2. 线性不变系统：http://www.15yan.com/story/2LE6VX5bRjW/

3. Eigenfunction： http://www.15yan.com/story/5bruOq9RA57/

4. 对比敏感度：http://www.15yan.com/story/g5Qkf83Rxgx/

5. 对比敏感度测量与Eigenfunction：http://www.15yan.com/story/fpT2SdWz7n5/
