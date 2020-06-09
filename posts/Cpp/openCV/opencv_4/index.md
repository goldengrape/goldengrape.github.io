<!--
.. title: OpenCV C++学习笔记(4): 4点投影变换
.. slug: opencv_4
.. date: 2020-06-09 10:00 UTC+08:00
.. tags: 
.. category: 教程, opencv, cpp
.. link:
.. description:
.. type: text
-->

真正有趣的东西来了, 总算开始学到了用ffmpeg搞不定的事情. 就是用OpenCV写个类似office lens那样的东西, 把倾斜的平面给抻直. 或者准确的说, 是把源图上的4个点, 映射到目标图上的4个点. 

![trans](https://i.loli.net/2020/06/09/SK6PBipY4jnOWTR.jpg)

<!-- TEASER_END -->

[OpenCV官方的warpPerspective示例](https://docs.opencv.org/master/de/dd4/samples_2cpp_2warpPerspective_demo_8cpp-example.html)就非常好. 

定位用的四个点分别存储在vector中.
```C++
vector< Point2f> roi_corners;
vector< Point2f> dst_corners(4);
```
原图上的四边形是roi_corners, 而变形图上的四个角, 就是dst_corners

有了这两组点之后, 就可以求出一个映射矩阵:
```C++
Mat H = findHomography(roi_corners, dst_corners);
```
这是一个3x3的矩阵, 对于原图上一点(roi_x, roi_y), 通过映射矩阵H, 可以算出其在变形图上的位置(dst_x,dst_y): 

si[dst_x, dst_y, 1] = H * [roi_x, roi_y, 1]

其中si是个归一化的系数, 相当于乘出来以后的第三项. 这里的乘法是矩阵乘, 也可以把矩阵乘法展开, 写成:

* dst_x = (H00 * x + H01 * y + H02 * 1) / (H20 * x + H21 * y + H21 * 1);
* dst_y = (H10 * x + H11 * y + H12 * 1) / (H20 * x + H21 * y + H21 * 1)

但通常是整个图像转换, 不需要手工一个点一个点求映射, 而是使用warpPerspective直接转换:

```C++
Mat warped_image;
warpPerspective(
    original_image, 
    warped_image, 
    H, 
    warped_image_size);
```

指定原始图像original_image, 建立一个空的目标图warped_image, 指定其大小warped_image_size, 使用这个warpPerspective就可以了. 