<!--
.. title: 描红字帖
.. slug: copybook-for-shufa
.. date: 2018-5-26 23:00 UTC+08:00
.. tags: Art
.. category:
.. link:
.. description:
.. type: text
-->

练毛笔字, 自觉练习进度缓慢, 于是决定采用训练神经网络的方式训练神经. 假设人脑具有足够强的泛化能力, 那么训练的最优策略就是用重复数据强化训练, 先迅速达成过拟合, 然后睡上一觉可能就自动调优了.

一个意外的发现, 激光打印机是可以打印宣纸的, 只要把宣纸裁剪成A4纸接近的大小, 按长轴折上一两次, 然后送进打印机, 就可以打印了. 当然容易卡纸, 发生率在10%~20%左右. 卡纸了以后小心取出来就是, 目前还没有碎在打印机里.

于是我自制了一个描红字帖.
<!-- TEASER_END -->

我的练习用宣纸, 折叠两次后大约是17cm X 35cm, 于是我按照这个尺寸做的字帖, 第一列是减淡后的原字, 第二列是笔画的骨架, 第三列是空白.

示例是这样的:
![字帖骨架](https://i.loli.net/2018/05/26/5b098168f1dc8.jpg)

每个字先贴进PowerPoint, 然后用"删除背景"将字体背景去掉, 调成适当大小后每6个字一组合, 组合之后另存为图片, 就有了第一列的图, 然后用skimage里的skeletonize把骨架生成出来, 注意这仅仅是从笔画外形得出的骨架, 如果两笔有重叠还是分不出来的, 只能作为提示用,

生成字体骨架的代码如下:
```python
from skimage.morphology import skeletonize
from skimage import io
import os

def ske(filename):
    fname, file_extension = os.path.splitext(filename)
    data=io.imread(filename)[:,:,-1]>0.5
    skeleton = skeletonize(data)
    ske = 1-skeleton/skeleton.max()
    out_name="ske_"+fname+".png"
    io.imsave(out_name,ske)
    return
```

最后再做成一个PowerPoint文件, 手工制作, 所以只做了几页, 够我练习一阵了. [下载此文件. ](https://mega.nz/#!rDhinKzb)

强化训练的时候, 就可以翻来覆去地写了, 比如:

* 从左到右, 按行来写;
* 从左到右, 按列来写;
* 从右到左, 按行来写;
* 从右到左, 按列来写.

一张宣纸裁出的四张正好写完.

<!-- EOF -->
