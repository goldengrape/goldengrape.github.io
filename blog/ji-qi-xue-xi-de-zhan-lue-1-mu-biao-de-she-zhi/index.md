<!--
.. title: 机器学习的战略(1)--目标的设置
.. slug: ji-qi-xue-xi-de-zhan-lue-1-mu-biao-de-she-zhi
.. date: 2017-12-19 01:22:33 UTC+08:00
.. tags: ML, 教程, 现代眼科医生知识扩展包
.. category: tutorial
.. link:
.. description:
.. type: text
-->

# 调整ML模型的战略

用来描述模型结构的, 比如是y=kx+b, 还是y=ax^2+bx+c, 可能还有y=ax^3+bx^2+cx+d, 叫做"超参数" **hyperparamter**

调整hyperparamter是一件很麻烦的事情, 以至于很多人把这件事叫做"炼丹". 你可能需要炼上七七四十九天才知道, 哦, 原来y=kx+b这个线性模型不合适啊. 所以除了具体的调整方法(战术), 你还需要战略方案.
<!-- TEASER_END -->

## Orthogonalization

正交化, 很学术的名词. 其实就是一次调一个东西, 别混在一起调整! 如果你的车方向盘和油门是关联在一起的, 那肯定就没法开了.

这大概是所有科研\研发的基本战略概念了.

# ML的目标设置

## 确定单一评价目标

用一个数来描述你的目标. 比如准确率, 其实是有两个数来描述的:
* Precision: 模型标定为阳性的数据(比如模型认为是猫的图片), 有多少实际是阳性的(图片真的是猫).
* Recall:  在阳性的数据中(图片中真的是猫), 有多少被模型找出来了

(**我特别讨厌用相似的名词去描述相近或者相反的概念, 每次我都弄混, 所以此处不出现真阳性假阳性之类的名词**)

显然是希望两个值都很高, 但是会碰到鱼和熊掌的问题
比如有两个模型:

| 分类器     | Precision     | Recall |
| :------------- | :------------- |:------------- |
|A|95%|90%|
|B|98%|85%|

那么用Precision与Recall调和平均数代替:

F1 score= 2/(1/Precision+1/Recall)

| 分类器     | Precision     | Recall | F1 score|
| :------------- | :------------- |:------------- |:------------- |
|A|95%|90%|92.4%|
|B|98%|85%|91.0%|

## 区分Satisficing 和 Optimizing metric

还是区分目标的事情, 你会希望准确率高, 又希望算得快, 还希望用计算资源少, 这几项很难同时达成, 于是要区分目标, 哪些是必须要满足的Satisficing metric, 满足条件就行了, 哪些是要尽量优化的, 越高越好的Optimizing metric.

比如甲方要求分类器能够在10秒内给出结果, 占用内存不超过10M, 准确率越高越好. 那么下面几个分类器:

| 分类器     | F1 score| 时间 | 内存|
| :-- | :-- |:--|:--|
|A|99%|20秒|5M|
|B|98%|9秒|9M|
|C|96%|3秒|5M|

显然选B方案.

**其实还是没钱!**

## train/dev/test set的分布
dev/test set是目标, 相当于靶子, 所以dev/ test set的分布要尽量接近真实场景. 如果立错了靶子就很麻烦.

比如要做手机照相识别的分类器app, 用从网上下载的图库可能就太清晰了, 图库通常是专业摄影师拍摄的, 而手机照片往往模糊\曝光不足\抖动. . . 各种问题, 如果dev/test set还是专业摄影师拍摄的图, 那么到用户手里的时候, 可能效果就不好.

## train/dev/test set的数量分配
dataset的数量=train+dev+test set的数量.
机器学习中dataset是越大越好, 在现在的机器学习项目中, dataset往往很大很大, 有了网络以后有大量的照片可以用. 那么dev/ test set的比例就不需要很高, 绝对数量足够就可以了.

如果dataset有1000k张图片, 那么
train: dev: test= 98%: 1%: 1%
test set大概10k张图片就可以了.

## 何时修正dev/test set和metrics
有时候你的模型看起来错误率很低, 准确性不错, 各项指标都很好, 但如果不慎挑出来一堆色情图片, 那这样的模型也需要忍痛割爱, 否则后患无穷.

如果出现了某些必须要满足的要求, 或者必须要避免的事件, 可以调整dev /test set来挪挪靶子, 或者在评价函数里面加上限定条件, 比如把色情图片作为罚分项目.


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
