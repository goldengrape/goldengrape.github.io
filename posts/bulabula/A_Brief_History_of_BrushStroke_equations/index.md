<!--
.. title: 笔法方程略史
.. slug: A_Brief_History_of_BrushStroke_equations
.. date: 2020-3-13 10:00 UTC+08:00
.. tags: 
.. category: 
.. link:
.. description:
.. type: text
-->

书法是物理学, 有1个基本定律, 剩下的可以推导的。

>基本定理：写完一笔以后, 笔应该恢复到能够写下一笔的状态。

也就是说, 一笔写完以后, 由于笔的弹性, 笔应该回到初始状态, 笔锋是处于聚拢状态的。不妨称为“回归律”

化简毛笔的模型, 比如只有5根笔毛或者只有9根笔毛, 中间一根是笔芯, 周围的是副毫, 就可以用有限元方法去分析如何行笔能够在转弯后仍然可以满足“回归律”

![侧锋](/images/侧锋.png)

这是一组微分方程。

![平衡方程](https://wikimedia.org/api/rest_v1/media/math/render/svg/73f442cfbeea809acf608ff41224843fb3183855)

![几何方程](https://wikimedia.org/api/rest_v1/media/math/render/svg/31a8b23ce59e2b417a7d0a560909a9ccbc78b2c1)

![本构方程](https://wikimedia.org/api/rest_v1/media/math/render/svg/163451c0ebe1094a548260aee0d59fc9ab074add)

![摩擦力](https://wikimedia.org/api/rest_v1/media/math/render/svg/9f03be93e92e75d6d0fcf50266ef23199d147762)

...

一个平凡解是转向时笔回到垂直状态, 再转向.
![正锋](/images/正锋.png)

>这些微分方程的可行解, 就叫做笔法. 

王羲之一共解出了9个!

这9个解一直秘不传人, 就好像3次方程求根公式，只在家族中一代一代流传。一直传到王羲之的第七代孙王法极, 也就是智永禅师，智永是和尚, 没有子嗣, 所以把9个解传给了虞世南. 从此把笔法方程传给了外人. 

虞世南->陆柬之->陆彦远->张旭

张旭是关键节点, 收了很多学生

![屏幕快照 2020-03-13 09.50.31](https://i.loli.net/2020/03/13/pjtBUFfI251KMXo.png)

其中还有一个分支是空海, 空海又将笔法方程式带到了日本. 

最后这9个解函数, 用[文言文编程](https://wy-lang.org/)记载在韩方明《授笔要说》和张怀瓘《玉堂禁经》里面, 叫做“九用”, 但可惜这只是头文件, 仅仅定义了函数声明的基本信息和测试样例. 函数文件还没有被发现. 

> 一曰頓筆，摧鋒驟衄是也，則努法下腳用之。

> 二曰挫筆，挨鋒捷進是也，下三點皆用之。

> 三曰馭鋒，直撞是也；有點連物則名暗築，「目」、「其」是也。

> 四曰蹲鋒，緩毫蹲節，輕重有準是也，「一」、「乙」等用之。

> 五曰 𨀛鋒，駐筆下衄是也；夫有趯者，必先𨀛之，「刀」、「﹝橫勾﹞」是也。

> 六曰衄鋒，住鋒暗挼是也；烈火用之。

> 七曰趯鋒，緊御澀進，如錐畫石是也。

> 八曰按鋒，囊鋒虛闊，章草磔法用之。

> 九曰揭筆，側鋒平發。「人」、「天」腳是也，如鳥爪形。

九用除去平凡解，剩下的如果手工解非常复杂，所以张旭建立了八个神经网络训练模型, 史称“始弘八法”.

这八个训练模型分别叫：侧，勒，努，趯，策，掠，啄，磔.

> 側不得平其筆，

> 勒不得臥其筆，

> 弩不得直，

> 趯須𨀛其鋒，

> 策須背筆，

> 掠須筆鋒，

> 啄須臥筆疾罨，

> 磔須【走歷】筆。

后世尊为“永字八法”

参考资料:

* 聚焦王羲之﹝下﹞: [https://www.youtube.com/watch?v=S_b9NXsWOaU](https://www.youtube.com/watch?v=S_b9NXsWOaU) 或 [https://www.bilibili.com/video/av40312839?p=5](https://www.bilibili.com/video/av40312839?p=5)

* 張旭的筆法: [http://www.chinese-artists.net/huangjian/works/19860205zhangxu/index.html](http://www.chinese-artists.net/huangjian/works/19860205zhangxu/index.html)

