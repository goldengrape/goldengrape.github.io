<!--
.. title: 机器学习的战略(2)--错误率
.. slug: ji-qi-xue-xi-de-zhan-lue-2-cuo-wu-lu
.. date: 2017-12-19 01:22:47 UTC+08:00
.. tags: ML, 教程, 现代眼科医生知识扩展包
.. category: tutorial
.. link:
.. description:
.. type: text
-->

# 与人类相比较
机器学习的很多任务, 比如识别图像, 听语音, 都是人类非常擅长的. 所以这些任务来说人类的错误率都相当低. 当然人类也分人, 看眼底图的还是得后节大夫, 找普通人看也还是错误率很高的, 最高的准确率应该是一组后节专家讨论会诊后得到的.
<!-- TEASER_END -->

理论上识别的错误率会有一个极限低值, 叫Bayes optimal error. 按照极限低值的定义, 那么肯定是比人类要低的, 但也不一定能够达到0, 在有些人类擅长的项目上, 不妨可以近似将人类的错误率当作bayes optimal error.

# 错误率分析
训练好的模型, 可以测定某一模型在dataset中的错误率, 重要的是3个数:
* bayes optimal error, 这是极限值, 不可测, 但在图像识别上可以近似用人类错误率替代.
* train error, 模型用在train set上的错误率
* dev error, 模型用在dev set上的错误率

有这三个数就好办了. 之前含混不清, 我连中文译名都不想给的bias 和 variance 终于可以定义了:
* bias=train error - bayes optimal error
* variance=dev error - train error

比如某个任务, 人类可以达到1%的错误率,

**模型A**, train error=7%, dev error=8%
那么:

* bias=7%-1%=6%
* variance=8%-7%=1%

显然这样的bias太高了, 模型还没练好, 欠拟合了.

**模型B**, train error=1.5%, dev error=7.5%

那么:

* bias=1.5%-1%=0.5%
* variance=7.5%-1.5%=6%

显然是variance太高了, 过拟合了. 模型"记住"了train set的内容.

# 降低错误率的策略
先算错误率
* bias=train error - bayes optimal error(~人类错误率)
* variance=dev error - train error

bias又被成为avoidable error, 可改善的错误率.

## 降低bias
* 试试更大的模型, 比如神经网络层数更多, 每层的神经元更多之类.
* 延长训练时间
* 调整优化算法, 比如试试更华丽的momentum, RMS prop, ADOM.
* 换更华丽的模型, 卷积神经网络CNN. RNN

## 降低variance
* 更多的数据, 更多的数据, 更多的数据
* Regularization, 就是加一些约束条件, 使得拟合出来的函数平滑一些, 不要那么扭曲妖娆.
* 换更华丽的模型, CNN, RNN. 从2012年到现在, 甚至未来几年, 各种神经网络就像选秀一样, 差不多每个月都能有新的选手出现.

此处推荐一下[机器之心](https://www.jiqizhixin.com/)的网站和公众号. 一些重要论文会有概述.

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
