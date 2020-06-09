<!--
.. title: OpenCV C++学习笔记(6): 颜色识别定位
.. slug: opencv_6
.. date: 2020-06-09 12:00 UTC+08:00
.. tags: 
.. category: 教程, opencv, cpp
.. link:
.. description:
.. type: text
-->

在 opencv-srf 网站上, 有一个[颜色检测和物体跟踪](https://www.opencv-srf.com/2010/09/object-detection-using-color-seperation.html)的示例. 使用inRange来检测颜色, 并且Moments类来追踪这个颜色的物体. 

这个例子只能追踪**一个**物体, 如果有多个同样颜色的物体, 用Moments只能找到这些物体最外面的框, 把这些物体当作一个, 找到他们的中心. 但这不是我想要的. 所以只好临摹了另外一个示例, 将两个凑在一起, 达成了目的.

<!-- TEASER_END -->

首先, RGB颜色, 或者说OpenCV里用的BGR颜色空间, 并不适合颜色检测, 应该先转换到HSV颜色空间, 这样只控制Hue就可以来选择颜色了. 

```C++ 
cvtColor(imgOriginal, imgHSV, COLOR_BGR2HSV);
```

不同颜色的数值大约是: 
* Orange  0-22
* Yellow 22- 38
* Green 38-75
* Blue 75-130
* Violet 130-160
* Red 160-179

然后就可以使用inRange来把边界条件之间的东西找出来. 注意边界是HSV颜色空间的坐标, 所以要用low=Scalar(H_low,S_low,V_low)和 high=Scalar(H_high,S_high,V_high)来预先定义好. 

```C++
inRange(imgHSV,low,high,imgThresholded); 
```
然后是图形学里常规操作: 

* 先缩后胀, 去除小体
```C++
erode(
    imgThresholded, 
    imgThresholded, 
    getStructuringElement(MORPH_ELLIPSE, Size(5, 5)) );
dilate(
    imgThresholded, 
    imgThresholded, 
    getStructuringElement(MORPH_ELLIPSE, Size(5, 5)) );
```

* 先胀后缩, 去除小孔
```C++
dilate(
    imgThresholded, 
    imgThresholded, 
    getStructuringElement(MORPH_ELLIPSE, Size(5, 5)) );
erode(
    imgThresholded, 
    imgThresholded, 
    getStructuringElement(MORPH_ELLIPSE, Size(5, 5)) );
```

如果是跟踪一个物体, 现在屏幕上就应该只有一个亮斑了.

![ObjectTracking](https://i.loli.net/2020/06/09/fAhrQPzXkltS9pC.png)

但我要追踪是多个同样颜色的物体. 于是还临摹了下面一段, 这是从[OpenCV官网用等高线标记物体的示例](https://docs.opencv.org/3.4/da/d0c/tutorial_bounding_rects_circles.html)中摘抄的. 

这个示例用等高线把物体多个标记出来. 我觉得可用. 

![](https://docs.opencv.org/3.4/Bounding_Rects_Circles_Source_Image.jpg)
![](https://docs.opencv.org/3.4/Bounding_Rects_Circles_Result.jpg)

```C++
Mat threshold_output;
vector<vector<Point> > contours;
vector<Vec4i> hierarchy;
threshold( imgThresholded, threshold_output, 200, 255, THRESH_BINARY );

findContours(threshold_output, contours, hierarchy, RETR_TREE, CHAIN_APPROX_SIMPLE, Point(0, 0) );
    
//    找到圆心
vector<vector<Point> > contours_poly( contours.size() );
vector<Point2f>center( contours.size() );
vector<float>radius( contours.size() );
Point2f point_center=Point2f(0,0);
for( size_t i = 0; i < contours.size(); i++ ){
    approxPolyDP( Mat(contours[i]), contours_poly[i], 3, true );
    minEnclosingCircle( contours_poly[i], center[i], radius[i] );
    point_center +=center[i];
}
point_center /= int(center.size());
```
所以先用inRange把同一颜色的物体找出来, 然后再用findContours分别找到各个物体的外圈, 用minEnclosingCircle找到每个物体的最小包围圈, 赋值给center. 

由于我还想给这些center按时钟位置排个序, 所以我又找了一下这些center的平均中心点. 