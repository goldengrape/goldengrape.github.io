<!--
.. title: OpenCV C++学习笔记(0): Mac下安装
.. slug: opencv_0
.. date: 2020-06-02 21:00 UTC+08:00
.. tags: 
.. category: 教程, opencv, cpp
.. link:
.. description:
.. type: text
-->

一直想写一个video see-through的程序, 用头戴显示器通过摄像头看外面, 以前用python写过, 但是延迟太明显. 于是去学了C++, 但也一直没有动手, 最近写毛笔字时开始给自己录像, 于是又有了很多视频需要剪切、调整、变形, 这些操作肯定是不愿意手动的, 于是打算用OpenCV, 然后继续嫌弃python太慢, 既然已经学了C++, 那干脆把OpenCV的C++版本学会好了. 

于是一边查一边写, 写一句查一句, 觉得效率太低, 反正磨刀不误砍柴工, 干脆找本书认真学OpenCV好了, 目前买了本[《OpenCV 4计算机视觉项目实战》](https://www.amazon.cn/dp/B07VDQ2BMT) 来看. 

首先是安装. 我觉得开源软件如果提供一个远程安装指导的付费服务, 一定能产生巨巨巨巨巨大的GDP. 一开始折腾了一整天, 也没搞定一句```#include <opencv2/opencv.hpp>```

<!-- TEASER_END -->

我没按照书上的方法从头编译, 而是使用了homebrew. 而且我在mac上用Xcode作为IDE, 要在Xcode上运行C++的opencv, 坑还是很多. 以下详述之, 注意下面是C++版本的opencv安装过程, python的用anaconda还是比较简单的, 我不知道安装好python版本的, 是否可以在C++上直接调用, 反正我是重新装了一个版本:

我的系统是:
> macOS Mojave 10.14.6
> Xcode 11.3.1
> 选择的OpenCV是4.3.0_3

* 一定要先把以前安装过的痕迹都先清理干净. 比如我的/usr/local目录下, 不知道什么时候已经有个opencv的目录, 后来造成了无尽的麻烦, 务必先删删删, 把/usr/local和/usr/local/lib里面带有opencv字样的先都删了, 或者至少先改个其他名字. 
* 打算通过homebrew安装, 如何安装homebrew而不出错, 又是一堆血泪, 此处就不再赘述了, 反正我很久以前就装好了homebrew.
* 用homebrew安装: ```brew install opencv``` 我这里安装上的是4.3.0_3, 命令虽然只有一句, 开源软件, 当然不可能一帆风顺, 否则岂不很没面子. 我在安装时说ffmpeg不对付, 于是只好先拆掉ffmpeg, 再运行一遍```brew install opencv```

用homebrew装好了opencv以后, 会安装在```/usr/local/Cellar/opencv/4.3.0_3```里面, 最后的数字就是版本号了, 不知道以后更新的时候会怎么办, 反正目前是这样了. 

然后打开Xcode, 继续踩坑. 

* 打开Xcode, 新建一个project, C++的程序一般是选择macOS-Command Line Tool, 比如我建了一个叫cv_learn的project. 

* 到Build Setting里, 搜索“search path”
![屏幕快照 2020-06-02 22.02.41](https://i.loli.net/2020/06/02/DGhYZTxurH5OlSU.png)
* 找到Header Search Paths, 点击前面的三角, 出现Debug和Release, 在Debug里点个"+", 然后输入```/usr/local/Cellar/opencv/4.3.0_3/include/``` , 如果你安装的是其他版本, 后面的数字可能会不同. 注意选择上“recursive”, 最终显示出来的是```/usr/local/Cellar/opencv/4.3.0_3/include/**``` 
* 然后找到Library Search Paths, 也是去Debug里, 添加上```/usr/local/Cellar/opencv/4.3.0_3/lib/``` 注意选择上“recursive”
* 再去Build Phases
![屏幕快照 2020-06-02 22.07.14](https://i.loli.net/2020/06/02/XGjP61m7MUWHFT5.png)
* 点开Link Binary With Libraries前面的小三角▶️
* 点+号以后, 再Add Other..., 然后Add Files, 弹出文件选择框以后, 按/号, 输入```/usr/local/Cellar/opencv/4.3.0_3/lib/```, 就可以看到一大堆libopencv_xxxxxx.dylib的文件
![屏幕快照 2020-06-02 22.10.39](https://i.loli.net/2020/06/02/MZJmYgdyrAwKq9h.png)

* 按说应该需要什么选什么, 我嫌麻烦, 就一股脑都选上了, 然后open

至此才算是大功告成. 如果你没搞定, 我也不知道为什么. 我建议是一定尽量保持干干净净的状态来装, 以前装过的opencv相关的, 尽量删掉. 

可以参考这一篇https://www.jianshu.com/p/876aadfae6d9 他的过程跟我比较类似.