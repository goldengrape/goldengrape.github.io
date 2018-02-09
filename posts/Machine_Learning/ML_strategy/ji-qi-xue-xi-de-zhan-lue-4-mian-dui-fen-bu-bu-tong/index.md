<!--
.. title: 机器学习的战略(4)--面对分布不同
.. slug: ji-qi-xue-xi-de-zhan-lue-4-mian-dui-fen-bu-bu-tong
.. date: 2017-12-19 01:23:16 UTC+08:00
.. tags: ML, 教程, 现代眼科医生知识扩展包
.. category: tutorial
.. link:
.. description:
.. type: text
-->

这一部分我在做练习题的时候老是错, 我都不是很确定自己理解明白了. 有必要的话最好还是回到课程原始视频中听老师亲自讲.
<!-- TEASER_END -->

# tran set/ dev set的分布不同

机器学习是需要大量数据喂出来的, 但有时候你很难获得大量最终应用场景需要的数据, 比如识别猫的照片, 从网上很容易下载比如可以找到200k, 但从手机中找到拍摄的照片相对要少一些比如可以找到10k. 因此也没法保证dev/test set和train set的数据分布是一致的.

## 不建议的方法
不要把下载来的数据和手机中的数据随机混合后分成train /dev/test set.

## 建议的方法
至少保证dev / test set中的数据是来自于目标应用场景的. 如果还剩下些手机照片的数据可以混合到train set中

# 分布不同时的错误率分析

bias=train error - bayes error
variance= dev error- train error

既然dev set和train set的分布都不同, 那么肯定variance显得很大, 但是否真的就是因为过拟合了还是因为分布不同导致?

解决方案是把train set里面再分出一小部分train_dev set, 这一部分的data set不要用在训练中, 用来检测的.

那么:
* bias=train error - bayes error
* variance= train_dev error- train error
* mismatch= dev error - train_dev error

就可以单独把各个错误率区分出来了, 还是使用bias和variance来分析是欠拟合还是过拟合. mismatch的部分要单独考虑.

# 分布不同时的误差分析

还是先做手工标注, 看看mismatch的原因到底是怎样的. 有些可以用一些技术手段解决, 比如螺旋桨战斗机机炮打断螺旋桨这种事情.

当然理想的解决方案还是找到足够多的目标场景数据了. 实在是找不到, 也许能够人工生成, 比如语音+噪音=有噪音环境的语音. 但是人工生成的时候要小心谨慎:

* 人工生成的数据很可能多样性不足, 比如从赛车游戏中提取图像进行自动驾驶训练, 理论上不错, 但实际上车型很少, 可能只有20多种车辆样式.
* 即使人眼看不出有什么差别, 在数据上不一定是相同的. 人工生成的数据可能只占了真实场景分布中的很小一部分.

----
# 参考资料:
* 机器学习的战略合集目录:

0. [基础概念](../ji-qi-xue-xi-de-zhan-lue-0-ji-chu-gai-nian/)
1. [目标设置](../ji-qi-xue-xi-de-zhan-lue-1-mu-biao-de-she-zhi/)
2. [错误率](../ji-qi-xue-xi-de-zhan-lue-2-cuo-wu-lu/)
3. [误差分析](../ji-qi-xue-xi-de-zhan-lue-3-wu-chai-fen-xi/)
4. [面对分布不同](../ji-qi-xue-xi-de-zhan-lue-4-mian-dui-fen-bu-bu-tong)
5. [迁移学习](../ji-qi-xue-xi-de-zhan-lue-5-qian-yi-xue-xi)
6. [end-to-end](../ji-qi-xue-xi-de-zhan-lue-6-end-to-end/)

* 课程链接:
[Structuring Machine Learning Projects](https://www.coursera.org/learn/machine-learning-projects/home/welcome)

* 参考视频:
莫烦的"[有趣的机器学习](https://morvanzhou.github.io/tutorials/machine-learning/ML-intro/)"系列科普视频, 制作精良讲解清晰, 非常推荐.  
