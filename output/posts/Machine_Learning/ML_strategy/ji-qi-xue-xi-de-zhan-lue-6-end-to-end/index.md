<!--
.. title: 机器学习的战略(6)--end to end
.. slug: ji-qi-xue-xi-de-zhan-lue-6-end-to-end
.. date: 2017-12-19 01:23:43 UTC+08:00
.. tags: ML, 教程, 现代眼科医生知识扩展包
.. category: tutorial
.. link:
.. description:
.. type: text
-->

# 端到端学习 end-to-end Learning

这个也是吓人.  读书人, 相煎何太急.

end-to-end的一端是原始数据, 另一端是想要的结果. 比如也许从一张眼底照片+FFA直接给出眼底激光应该打哪里, 或者说中文直接给出翻译好的英文字幕. 从一端到另一端中间本来是有很多研究过程在里面的,
<!-- TEASER_END -->

* 中文语音->音频信号增强降噪->音节提取->转成文字->翻译->英文字幕,
* 眼底照片+FFA->数微血管瘤, 渗出->形成糖尿病视网膜病变诊断->分期->判定新生血管->规划激光点位置->开打

每个环节都有一堆PhD论文, 有一堆临床经验, 现在突然有一部分问题可以直接跳过中间环节, 从一端直接获得另一端的结果. 有时候学术研究也堪比柯达胶卷, 明明自己很努力也没做错什么, 整个领域突然就废了.

不过好在目前还不是所有的问题都可以end-to-end, 而且也不是end-to-end就效果很好. 有些问题加个中间环节反而可以更有效.

课程中的例子是:
* 门禁的人脸识别, 一种是直接从图像->身份ID的end-to-end, 另一种是图像->标记出人脸->剪裁图片人脸放大居中->身份ID. 后者的效果更好.
* 另一个例子是从X光片看儿童发育, 直接从图像->年龄的效果不如图像->提取分离骨骼图像->骨骼尺寸->年龄, 而且其中骨骼尺寸->年龄是可以从正常值的统计得出的.

# 是否使用end-to-end

优点:
* 完全来自于数据, 机器学习"总结"出来的规律是客观数据所反映的, 不是人想象出来的, 用不着讨论是"木火土金水"还是"金木水火土"
* 用不着太多手工设计.

缺点:
* 需要大量大量大量大量的数据.
* 排除了手工设计的组件.
    * 手工设计组件并非坏事, 人类的推理归纳还是对知识的扩展有很大意义.
    * 而且, 从我做发明的经验来看, 很多公司要求避免使用比较"黑箱"的深度学习方法, 大概很难查错吧.

是否用end-to-end的关键在于, 已经拥有的data数量是否已经可以 **足够** 反映出问题的复杂性. 足够的定义就只好靠经验和实践了.

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
