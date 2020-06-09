<!--
.. title: OpenCV C++学习笔记(3): 视频读写
.. slug: opencv_3
.. date: 2020-06-09 9:00 UTC+08:00
.. tags: 
.. category: 教程, opencv, cpp
.. link:
.. description:
.. type: text
-->

有坑
```C++
VideoWriter::fourcc('m', 'p', '4', 'v')
```
<!-- TEASER_END -->


## 视频读取

从文件取得视频和从摄像头取得视频是一样的, 先新建一个```VideoCapture cap;```

VideoCapture 的初始化可以直接
VideoCapture Cap(文件名或者摄像头ID) 也可以用cap.open(文件名)来定义.

一旦初始化好VideoCapture, 就可以使用get来获取各种视频的信息. [这里](https://docs.opencv.org/master/d4/d15/group__videoio__flags__base.html#gaeb8dd9c89c10a5c63c139bf7c4f5704d)有列出超多. 

例如:

```C++
float width = cap.get(CAP_PROP_FRAME_WIDTH)
float height = cap.get(CAP_PROP_FRAME_HEIGHT)
```
当然, 反过来也可以set, 主要是用在摄像头读取上的. 

```C++
capA.set(
    CAP_PROP_FOURCC, 
    VideoWriter::fourcc('M', 'J', 'P', 'G'));
capA.set(CAP_PROP_FPS, 30);
capA.set(CAP_PROP_FRAME_WIDTH,frame_width);
capA.set(CAP_PROP_FRAME_HEIGHT,frame_height);
```
据说在读取摄像头时fourcc使用'M', 'J', 'P', 'G'能够达到很高的读取速度. 

在读取视频时, 一般是要建立一个循环
```C++
Mat frame;
while(true){
    bool bSuccess = cap.read(frame); 
    if (bSuccess == false){
         cout << "Found the end of the video" << endl;
         break;
        }
}
cap.release();
```

## 视频写入

**此处有坑!!!**

```C++
VideoWriter oVideoWriter(
    output_filename, 
    VideoWriter::fourcc('m', 'p', '4', 'v'),
    fps, Size(width,height), true);    
```
这个fourcc是个非常诡异的东西, 用4个字母缩写来表示视频文件存储时使用的编码, 要想安心使用mp4文件格式, **目前测试的结果只能是用小写的mp4v的4个字符, 别的都没搞定**.


在写入视频时, 通常是在读取视频的基础上进行处理后再保存, 一帧一帧写入就可以. 比如
```C++
Mat frame;
while(true){
    bool bSuccess = cap.read(frame); 
    if (bSuccess == false){
         cout << "Found the end of the video" << endl;
         break;
        }
    oVideoWriter.write(frame);
}
cap.release();
oVideoWriter.release();
```
记得最后要release()