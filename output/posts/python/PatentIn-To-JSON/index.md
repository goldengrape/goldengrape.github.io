<!--
.. title: 将PatentIn文件转换成JSON文件的工具
.. slug: PatentIn-To-JSON
.. date: 2017-12-28 15:00:03 UTC+08:00
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->

## --兼论以自下而上的抽象应对不断改需求的PM

[Jupyter版本:](https://github.com/goldengrape/check_patentIn_sequence/blob/master/patentIn_to_json.ipynb)
或者更容易import的
[python版本:](https://github.com/goldengrape/check_patentIn_sequence/blob/master/patentIn_to_json.py)

只需要:
```python
from patentIn_to_json import patentIn_to_json
```
即可.
<!-- TEASER_END -->

这是[<序列一致性检验工具>](https://github.com/goldengrape/check_patentIn_sequence) 之中的一个组件. 很适合单独使用, 所以特别提出来说明一下.

一个程序员或者一个Nerd, 通常不能够容忍重复手工操作, 所以当有检查序列需求的时候, 我显然会写程序. 这可以用下面的图来表示.
![nerd.001](http://upload-images.jianshu.io/upload_images/29267-031eb2cdd79eba2d.jpeg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

然而在实际的生活工作中, 上图不一定总能实现, 特别是当你碰到一名反复多变的产品经理之时. (没错, 如果是在家编程, 提出需求的家属也就是产品经理).

如果需求不断地更改, 比如检查序列一致性的问题, 每次送来的文件都有格式上的细微差别, 于是每次送来的新文件都能触发一轮bug, 于是每次都要详细地查错debug, 于是付出的努力远远比手工操作多得多, 完全没有实现初始时打算省时省力的愿望.
![nerd.002](http://upload-images.jianshu.io/upload_images/29267-6dc0c384a93cccba.jpeg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

事情就会变得如同图2所示, 这会让一个人疯掉的.

幸好前一段时间粗略地刷过一多半[SICP](https://mitpress.mit.edu/sicp/), 也读了一遍[<黑客与画家>](https://book.douban.com/subject/6021440/), 知道产品经理不断改需求这件事情早在1984年就被反复提及了.

解决方案是自下而上地抽象, 这样打好了底层的基础, 一旦需求发生变化, 只需要在高层的抽象上进行灵活地改变, 而不必每次重头再来. 每一次debug或者重构的成本就会越来越低.

![nerd.003](http://upload-images.jianshu.io/upload_images/29267-ae858eeb2da30473.jpeg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

比如序列一致性的检验问题, 原来我是按照文本文件中的特征词, 用正则表达式进行切割, 分离, 然后分别找到序列的名称和序列字符串的列表, 再用字典将两者对应起来. 但文本文件中就是可能会出现错误, 比如关键词的变化, 比如关键项目的缺失, 一旦发生了就无法继续进行, 也很难找到问题所在.

现在的方案是如程序中所展示的, 先用正则表达式把txt文件统一转换成json, 实际上只是做很多的字符串替换, 比如把一对括号变成引号和冒号, 立刻就完成了字典键值之间的对应.

一旦完成了txt到json的转换, 就可以方便使用其他基于json的抽象工具, 比如pandas, 而处理缺项漏项在pandas中又有很多工具. 一下子就方便许多.

学好SICP真的有帮助, 看待问题的方式都不一样了. 顺便推荐一下[https://github.com/sarabander](https://github.com/sarabander) 这位做了各种版本的SICP电子书, 而且公式生成清晰. 大力推荐.
