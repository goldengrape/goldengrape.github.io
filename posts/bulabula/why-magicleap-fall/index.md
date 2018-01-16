<!--
.. title: 见微知著: Magic Leap为什么会失败
.. slug: why-magicleap-fall
.. date: 2018-1-16 16:30 UTC+08:00
.. tags: ophthalmology
.. category:
.. link:
.. description:
.. type: text
-->

Magic Leap取得了大量投资以建立基于光纤扫描的数字光场技术. 试图利用该技术解决调节集合反射的问题.

经过6年的研发, Magic Leap自称将于2018年推出实体产品 Magic Leap One
![](https://www.vrandfun.com/wp-content/uploads/2017/12/magic-leap-one-ar-headset.jpg)

但是, 根据magic leap于[6 Apr 2016发布的一条twitter](https://twitter.com/magicleap/status/717390550429786113):
"When you start building tech with the body in mind, magical things happen. Step one: study the eye."
![](https://pbs.twimg.com/media/CfSu50CW8AEt39K.jpg)


**图中大量的参数标注是错误的!** 这样粗心或无知的公司不可能按照预期将高质量的产品投放市场上. 投资人对数字光场技术的期望必将收到严重打击, 并将积极寻找替代技术.

那么, 正确的眼球光学参数应当是怎样的?

<!-- TEASER_END -->

|项目|Magic Leap标注|Gullstrand模型眼|吐槽|
| :---- | :---- |:----|:----|
|位置|       
|角膜前表面|0       |0 |参考原点|
|角膜后表面|1.15| 0.5|错太离谱, 猪眼才这么厚|
|前房深度|3.54|3.6|这项看着还行|
|晶体后表面|7.60|7.2|晶体这么厚, 还是看着像猪眼|
|黄斑位置|24.75|24|眼轴每长1mm误差带来约+3D近视|
||||
|曲率半径||||
|角膜前表面|7.98|7.7|前面太凸|
|角膜后表面|6.22|6.8|后面太平|
|晶体前表面|10.20|10.0||
|晶体后表面|-6.17|-6.0||
||||
|光学参数|||由于上面的结构参数差别, 导致光学参数大不相同了. |
|第一主点位置|1.54|1.348|
|第二主点位置|1.86|1.602|
|第一焦点位置|-15.59|-15.707|
|第二焦点位置|24.75|24.387|
|第一节点位置|7.30|7.078|
|第二节点位置|7.62|7.332|
|第一焦距|-17.13|-17.055|
|第二焦距|22. 89|24.387|

正常值来自于Gullstrand模型眼在调节放松时的状态, 引用自2014年AAO教材Basic and Clinical Science Course (BCSC)第三卷Clinical Optics. 当动用调节时在实体参数上只有晶体的曲率和前表面位置发生变化.  

[Allvar Gullstrand](https://en.wikipedia.org/wiki/Allvar_Gullstrand)前辈1911年获得了诺贝尔奖, 并于1905年霸气地阻止了爱因斯坦的相对论获诺贝尔奖.

![Gulsstrand](https://upload.wikimedia.org/wikipedia/commons/thumb/7/79/Allvar_Gullstrand.jpg/412px-Allvar_Gullstrand.jpg)

这些还只是比较了在光轴上的参数, 还有比如角膜直径被标成12-13, 人眼的角膜是10-11, 猪眼才13.

如果你觉得Gullstrand模型眼太古老, 也可以去Zemax上找到[如何建立人眼光学模型的教程](http://customers.zemax.com/os/resources/learn/knowledgebase/how-to-model-the-human-eye-in-zemax), 参数上会有一些差别, 比如角膜厚度是0.55, 这个更接近人体测量值. 但即使有差别, 也不至于把厚度差到猪眼上去.








<!-- EOF -->
