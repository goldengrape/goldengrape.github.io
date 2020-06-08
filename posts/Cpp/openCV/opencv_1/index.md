<!--
.. title: OpenCV C++学习笔记(1): 读/写图像
.. slug: opencv_1
.. date: 2020-06-02 23:00 UTC+08:00
.. tags: 
.. category: 教程, opencv, cpp
.. link:
.. description:
.. type: text
-->

《OpenCV 4计算机视觉项目实战》第二章, 代码在[github](https://github.com/PacktPublishing/Learn-OpenCV-4-By-Building-Projects-Second-Edition/tree/master/Chapter_02)

<!-- TEASER_END -->

## 读写图像

opencv的图像数据存储在Mat类型的矩阵里. 颜色顺序是BGR.

读取图像使用[imread](https://docs.opencv.org/4.3.0/d4/da8/group__imgcodecs.html#ga288b8b3da0892bd651fce07b3bbd3a56)

比如
```C++
    Mat color=imread("lena.png");
    Mat gray=imread("lena.png", IMREAD_GRAYSCALE);
```
注意与书里不一样的是, 按照灰度读取时的标记是 ```IMREAD_GRAYSCALE```, 而不是```CV_LOAD_IMREAD_GRAYSCALE```. 当然也可以按照[官方文档里的例子](https://docs.opencv.org/4.3.0/db/d64/tutorial_load_save_image.html), 先读取彩色图像, 然后用cvtColor将彩色图转换成灰度图. 

```C++
Mat color=imread("lena.png",IMREAD_COLOR );
Mat gray;
cvtColor( color, gray, COLOR_BGR2GRAY );
```

写入图像的命令就是imwrite(文件名, 数据), 没什么太多要说的. 


