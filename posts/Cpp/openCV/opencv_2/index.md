<!--
.. title: OpenCV C++学习笔记(2): Mat数据结构
.. slug: opencv_2
.. date: 2020-06-04 12:00 UTC+08:00
.. tags: 
.. category: 教程, opencv, cpp
.. link:
.. description:
.. type: text
-->

opencv用了一种Mat的矩阵来存储图像数据, Mat看起来很神秘, 尤其是在处理图片局部的时候, 很神秘, 我一直想把两个摄像头拍摄的画面合并到一张图上显示, 查了很多, 才大概弄明白一点. 

<!-- TEASER_END -->

## Mat

图像数据都是存储在矩阵里的, 或者说是二维数组, OpenCV中封装在Mat里. 

Mat里可以装一张图, 也可以装视频中的一帧. 

初始化一个Mat: 

```C++
Mat two_cap=Mat::zeros(Size(frame_width*2,frame_height), CV_8UC3);
```

* 语法和matlab里的zeros初始化差不多, 虽然还有其他的初始化方式, 但一开始就赋上初始值, 把0都填上还是好习惯, 
* 用```Size(宽, 高)```来定义比较容易按图片来理解, 否则row和col每次搞得我很晕, 横竖经常分不清楚. 
* ```CV_8UC3```是最常用的0-255整数, 三种颜色.

## ROI

感兴趣区域, 最简单的是矩形区域:

```C++
Rect r1 = Rect(0,0,frame_width,frame_height);
Rect r2 = Rect(frame_width, 0, frame_width, frame_height);
```

定义了感兴趣区以后, 就可以直接调用这一块位置, 有点类似于数组的切片. 

这时候, Mat作为左值也可以, 作为右值也可以. 

比如可以
```C++
two_cap(r1)=0;
```
也可以
```C++
Mat frame=two_cap(r1)
```

## 但是!

Mat在复制的时候是浅复制, 
```C++
mat_target(r1)=mat_source;
```
mat_target里面并没有好好被mat_source中的数据替换. 要达成目的, 应该使用copyTo,

```C++
mat_source.copyTo(mat_target(r1))
```

## demo

以下是照着各种demo简单写的一个双摄像头显示, 本来是想写个简单的video see through, usb摄像头的延时居然达到了200ms, copyTo的速度不影响, 可能是OpenCV里套了太多GUI的锅, 也可能是硬件的问题. 


```C++
#include <iostream>
#include <string>
#include <sstream>
using namespace std;

// OpenCV includes
#include <opencv2/opencv.hpp>
#include <opencv2/core.hpp>

using namespace cv;

int main( int argc, const char** argv )
{
    
    int frame_width=640;
    int frame_height=480;
    
    VideoCapture capA(1), capB(2);
    
    if (capA.isOpened() == false || capB.isOpened() == false)
    {
     cout << "Cannot open the video cameras" << endl;
     cin.get(); //wait for any key press
     return -1;
    }

    capA.set(CAP_PROP_FOURCC, cv::VideoWriter::fourcc('M', 'J', 'P', 'G'));
    capB.set(CAP_PROP_FOURCC, cv::VideoWriter::fourcc('M', 'J', 'P', 'G'));
    capA.set(CAP_PROP_FPS, 30);
    capA.set(CAP_PROP_FRAME_WIDTH,frame_width);
    capA.set(CAP_PROP_FRAME_HEIGHT,frame_height);
    capB.set(CAP_PROP_FPS, 30);
    capB.set(CAP_PROP_FRAME_WIDTH,frame_width);
    capB.set(CAP_PROP_FRAME_HEIGHT,frame_height);

    
    Mat two_cap=Mat::zeros(Size(frame_width*2,frame_height), CV_8UC3);
    Rect r1 = Rect(0,0,frame_width,frame_height);
    Rect r2 = Rect(frame_width, 0, frame_width, frame_height);
    
    string window_name="double webcam";
    namedWindow(window_name);
    Mat frameA;
    Mat frameB;
    
    while (true)
    {
//     read frame from webcam
     bool bASuccess = capA.read(frameA);
     bool bBSuccess = capB.read(frameB);

     //Breaking the while loop if the frames cannot be captured
     if (bASuccess == false || bBSuccess == false )
     {
      cout << "Video cameras are disconnected" << endl;
      cin.get(); //Wait for any key press
      break;
     }
     
     //show the frame in the created window
        frameA.copyTo(two_cap(r1));
        frameB.copyTo(two_cap(r2));
     imshow(window_name, two_cap);
     
     if (waitKey(1) == 27)
     {
      cout << "Esc key is pressed by user. Stop the video" << endl;
      break;
     }
    }
    capA.release();
    capB.release();
    return 0;
}
```