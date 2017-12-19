<!--
.. title: 机器学习的战略(3)--误差分析
.. slug: ji-qi-xue-xi-de-zhan-lue-3-wu-chai-fen-xi
.. date: 2017-12-19 01:23:01 UTC+08:00
.. tags: ML, 教程, 现代眼科医生知识扩展包
.. category: tutorial
.. link:
.. description:
.. type: text
-->

我觉得这一部分是导师指导/监督学生实验时应该出手的部分.

# 误差分析
这是个手工分析操作技巧了. 老师在课程中不断强调不要看不起手工分析, 一是人类看图识别的效率很高, 看上100张图很快就搞定了, 二是在分析过程中还有助于产生直观的印象, 再次利用人类强大的识别能力来解决问题.
<!-- TEASER_END -->

方法是:
* 从 **dev set** 中, 找100个被标记错误的图片, 人眼看, 手工数.
* 怎么数呢? 要列一张表, 要比较容易编辑扩展的, 我觉得excel之类的就不错.


|  图片编号  | 这是狗   |狮子老虎     |图片太模糊 |Instagram滤镜|备注 |
| :------------- | :------------- |:------------- |:------------- |:------------- |:------------- |
| 1      | +1       |||+1||
| 2      |        ||+1|+1||
| 3      |       |+1|+1||下雨天|
| ...      |       |...|...|||
| 合计      | 8% |43%|61%|12%||

有了这样的表格, 就很容易分析应该在哪些方面改进了.

# 标注错误
dataset的图片标注通常也是由人类来完成的, 也可能有各种不小心的错误, 如果你发现dataset中的图片有标注错误怎么办?

* 随机出现的错误, 算了不管.
* 系统性的错误, 比如大量的白狗被标记成了猫
    * 进行误差分析，看看标注错误有多大影响
    * 如果影响很大, 在dev / test set中一起改
    * 如果有精力, 也注意那些识别"正确"的图
    *  train set中的标注错误可改可不改.

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
