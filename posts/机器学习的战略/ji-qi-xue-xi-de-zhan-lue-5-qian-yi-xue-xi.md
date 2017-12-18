<!--
.. title: 机器学习的战略(5)--迁移学习
.. slug: ji-qi-xue-xi-de-zhan-lue-5-qian-yi-xue-xi
.. date: 2017-12-19 01:23:31 UTC+08:00
.. tags: ML, 教程, 现代眼科医生知识扩展包
.. category: tutorial
.. link:
.. description:
.. type: text
-->

# 迁移学习

好激动, 这是整个机器学习里面最激动人心最吸引人的部分了. 知道了迁移学习这事情以后, 我才比较理解为什么整个课程一直没有进入各种fancy的CNN, RNN之类的神经网络结构, 而仅仅就是把层次多一点的神经网络称为深度神经网络.
<!-- TEASER_END -->

迁移学习是说, 可以用训练好的神经网络稍微改改, 用自己的数据来训练最后几层. 比如可以用ImangeNet的优胜者模型, 类似GoogleNet, VGG之类, 这些网络模型是用来分类常规图像的, 比如阿猫阿狗, 但是可以固定前面层次的参数, 留出最后一两层的全连接神经网络, 用自己的数据, 比如眼底图片或者放射科影像来训练.

这时候训练的数据量不需要很大, 至少不必像ImageNet那样的大量数据集了. 因为前面一些层次的神经元往往是用来提取图像的低级特征的, 类似提取边缘之类的.

如果只训练了最后一个全连接层觉得效果不够好, 可以再逐渐加层次. 也就是把训练好的模型(如VGG)当作标准的特征提取器或者域变换操作, 先对数据进行预处理, 然后送进自己的神经网络.

补充说一下, 由于迁移学习常用, 所以很多机器学习的框架例如tensorflow \ pytorch都有所谓的model zoo. 知名的模型已经都摆在zoo里面供大家挑选了.  

这里面需要注意的是, 迁移学习用的模型数据形式至少要和目标是一样的, 比如用ImageNet竞赛获奖模型, 那么至少应该是用来看图的.

然后, 吴恩达老师举例子的时候, 目标dataset的数据量终于从100k的数量级降到1k的数量级了. 突然觉得有希望能做东西了有没有.

# 多任务学习
这一部分离我远一些, 兴趣不大. 大概在自动驾驶的场景里比较多.

与单独识别一张照片里有猫还是没猫不一样. 可以同时训练在图像里找到多个目标, 比如是否有红灯\是否有行人\是否有其他车辆, 这些事情要放在一起学, 不要单独训练是否有红灯, 再用另一组dataset训练是否有行人, 因为拆分了任务就很难保证足够大的dataset, 效果会差一些.

----
update

迁移学习也是有代价的, 继承深度神经网络的处理能力时, 也会继承神经网络内在的"错觉", 我觉得错觉比bug更能解释问题的所在. 从成本考虑, 我觉得未来肯定越来越多的应用是使用迁移学习来的, 被继承的深度神经网络只会是有限的几个. 会有一些针对性的错觉被发现, 甚至还可能会有共有的错觉.

参考[Even Artificial Neural Networks Can Have Exploitable 'Backdoors'](https://www.wired.com/story/machine-learning-backdoors/ )

----
# 参考资料:
* 机器学习的战略合集目录:

0. [基础概念](http://www.jianshu.com/p/605bb2d6da5e)
1. [目标设置](http://www.jianshu.com/p/e5f2d53493ff)
2. [错误率](http://www.jianshu.com/p/9ec8e8c7b58c)
3. [误差分析](http://www.jianshu.com/p/b841fc1f7c40)
4. [面对分布不同](http://www.jianshu.com/p/4e1ad322deb5)
5. [迁移学习](http://www.jianshu.com/p/e2993f594767)
6. [end-to-end](http://www.jianshu.com/p/92bf4af48804)

* 课程链接:
[Structuring Machine Learning Projects](https://www.coursera.org/learn/machine-learning-projects/home/welcome)

* 参考视频:
莫烦的"[有趣的机器学习](https://morvanzhou.github.io/tutorials/machine-learning/ML-intro/)"系列科普视频, 制作精良讲解清晰, 非常推荐.  
