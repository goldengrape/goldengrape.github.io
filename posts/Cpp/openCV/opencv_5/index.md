<!--
.. title: OpenCV C++学习笔记(5): 原位做4点投影变换
.. slug: opencv_5
.. date: 2020-06-09 11:00 UTC+08:00
.. tags: 
.. category: 教程, opencv, cpp
.. link:
.. description:
.. type: text
-->

[OpenCV官方的warpPerspective示例](https://docs.opencv.org/master/de/dd4/samples_2cpp_2warpPerspective_demo_8cpp-example.html)用一个窗口进行选区, 用另一个窗口进行显示: 

![trans](https://i.loli.net/2020/06/09/SK6PBipY4jnOWTR.jpg)

但我觉得这样有点麻烦, 不太适合移动端、小屏幕的操作. 于是做了一点改进, 使我可以在一个窗口内直接操作图像.

<!-- TEASER_END -->


![2020-06-09 13-14-58.2020-06-09 13_17_31](https://i.loli.net/2020/06/09/gDPiLcaWx9UMKZ2.gif)



下面的过程说起来有点绕. 反正变换的控制在于找到两组对应点, 在原始图上的o_corner, 和在变形图上的d_corner. 
```
vector<Point2f> d_corner(4);
vector<Point2f> o_corner(4);
```

在使用两个窗口进行控制+显示时, 变形图上的d_corner就是4个角, 是不变的. 但如果在一个窗口内控制, 就不能是不变的点了. 

先假定已经有一个映射矩阵H, 和它的逆矩阵H_inv, 一开始的时候, 原始图像和变形图像是相等的, 那么这两个矩阵就都是单位矩阵. 

现在用鼠标点中变形图中的位置(x,y), 那么就可以找到在原始图中这个点对应的位置(ox, oy), 当鼠标按住拖动到(xt, yt)时, 含义就是将原始图中的(ox,oy)映射到了(xt,yt).

比如, 鼠标控制的是```vector<Point2f> d_corner;```中的第3点, 那么```d_corner[3]=Point2f(x,y);```, 我写了一个函数来求对应的```o_corner[3]```

```C++
void point_warp(
    Point2f &p_target, 
    const Point2f &p, 
    const Mat &H){
//    映射矩阵H是一个3x3的矩阵,
//    s*[p_target.x, p_target.y, 1]= H * [p.x, p.y, 1]
//    乘出来以后要对第三项归一化
    Mat p_vector = (Mat_ <double>(3, 1) << p.x,p.y, 1);
    p_vector = H * p_vector;
    p_target.x=(float)(p_vector.at<double>(0)/
                       p_vector.at<double>(2));
    p_target.y=(float)(p_vector.at<double>(1)/
                       p_vector.at<double>(2));
}
```

这里用到的公式就是
```s[d_x, d_y, 1] = H * [o_x, o_y, 1]```

其中s是一个归一化系数, 就是第三项. 这是要反过来求的, 要用上H的逆矩阵H_inv, 所以实际上是:
```s[o_x, o_y, 1] = H_inv * [d_x, d_y, 1]```

其中Mat类里, 要访问单个元素(像素)的数值, 可以使用```.at<类型>(行, 列)```的方式来访问. 因为之前使用findHomography求出来的H矩阵似乎是一个double类型的, 所以这里其他的向量最好也先使用double类型. 如果使用float会出错. 

所以流程就是:

* 鼠标在变形图上(x,y)点按下,
```d_corner[selected_corner_i]=Point2f(x,y);```

* 计算出原始图上的对应点位置
```C++
point_warp(
    o_corner[selected_corner_i],
    d_corner[selected_corner_i],
    H_inv);
```

* 鼠标开始拖动, 移动到新的(x,y)位置, 此时新的: 
```d_corner[selected_corner_i]=Point2f(x,y);```

* 根据新的o_corner和d_corner分别计算映射矩阵H和逆矩阵H_inv:
```C++
H = findHomography(o_corner, d_corner);
H_inv= findHomography(d_corner, o_corner);
```

* 在根据映射矩阵H, 将原始图映射到变形图上
```C++
Mat warped_image;
warpPerspective(img, warped_image, H, Size(width,height));
```
完整的代码, 放在[gist中](https://gist.github.com/goldengrape/b666a0e822f6da7b56c0c626b7b140a5)





