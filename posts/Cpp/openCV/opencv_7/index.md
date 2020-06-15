<!--
.. title: OpenCV C++学习笔记(7): 命令行解析
.. slug: opencv_7
.. date: 2020-06-10 12:00 UTC+08:00
.. tags: 
.. category: 教程, opencv, cpp
.. link:
.. description:
.. type: text
-->

OpenCV里有个CommandLineParser, 可以用来解析命令行, 方便不少.

首先要定义一个keys:

``` C++
const char* keys =
{
    "{help      |   | print this message}"
    "{@input i  |   | input video file}"
    "{@output o |   | output video file}"
    "{low       |35 | low value}"
    "{high      |100| high value}"
};
```

两根竖线里面是默认值

然后在```int main(int argc, const char * argv[])```里面, 要声明一个

```C++
    CommandLineParser parser(argc, argv, keys);
```

接着就可以处理parser里的东西了, 

* 判断一个参数有没有, 可以用```parser.has(参数名)```
* 取得参数值, 可以用```parser.get<类型>(参数名或者序号)```

比如, 单独写一个函数来处理这些参数, 用传引用的方法来传递获取的参数值. 

```C++
bool get_CLI(CommandLineParser &parser,
             String &filename,
             String &output_filename){
    
    parser.about("change video color and contrast");
    //If requires help show
    if (parser.has("help"))
    {
        parser.printMessage();
        return true;
    }
    
    filename= parser.get<String>("@input");
    if (parser.has("@output")){
        output_filename=parser.get<String>(1);
    }else{
        output_filename=
        filename.substr(0,filename.length()-4)+
        "_changed.MP4";
    }
    return false;
}
```