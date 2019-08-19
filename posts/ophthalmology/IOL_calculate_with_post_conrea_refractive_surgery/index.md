<!--
.. title: 角膜屈光手术后IOL计算
.. slug: IOL_calculate_with_post_conrea_refractive_surgery
.. date: 2019-8-19 12:00:00 UTC+08:00
.. tags: ophthalmology
.. category: ophthalmology
.. link:
.. description:
.. type: text
-->

角膜屈光手术, 包括但不限于Lasik, Lasek, PRK, 半飞秒, 全飞秒……, 做完之后多年, 如果出现了白内障, 要换人工晶体. 这时直接代入常规的人工晶体公式是不行的. 要使用新的计算方法.

好在发明新的人工晶体计算公式是名利双收的好事, 于是过去15年, 至少出现有30种以上的公式. 然后还有更多的临床研究, 对比各种公式的优劣. (医学领域的“什么值得买”)

最近读了一篇这样的对比综述, [Intraocular lens power calculation in eyes with previous corneal refractive surgery](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6053834/)

## python实现

于是把其中的各种公式重新用python写了一遍. 代码放在github上: 
[https://github.com/goldengrape/IOL_calculate_with_post_corneal_refractive_surgery](https://github.com/goldengrape/IOL_calculate_with_post_corneal_refractive_surgery
)

<!-- TEASER_END -->

而且, 这次我是练习使用ipywidget做成了交互式的jupyter笔记本. 可以使用滑动条或者填空格来填入参数, 可以实时显示出结果.

例如:
<!-- TEASER_END -->![屏幕快照 2019-08-19 11.54.42](https://i.loli.net/2019/08/19/hJucql4jdELfyxv.png)

但是要实现交互, 在github的ipynb静态渲染不行, 必须要一个能够真正计算的空间才行. 虽然理论上mybinder.org提供了从github直接导入的功能, 但实际上用起来特别慢, 还没搞定. 

因此, 要想测试交互式的功能, 国内只好使用azure notebooks了. 我也放了一份: [https://notebooks.azure.com/goldengrape/projects/iol-calculation-lasik/html/IOL_calc.ipynb](https://notebooks.azure.com/goldengrape/projects/iol-calculation-lasik/html/IOL_calc.ipynb) 点击硕大的**绿色Clone按钮**, 给自己Clone一份, 就可以运行交互了. 

![屏幕快照 2019-08-19 12.48.07](https://i.loli.net/2019/08/19/8p3TeWOG5Alfdcs.png)

## 读后感

阅读带有公式的论文, 还是应该自己亲手复现一下.即使是这个领域的经典文章, 里面也有很多错误. 比如: 

* [BESSt公式](https://sci-hub.tw/10.1016/j.jcrs.2006.08.037)的文献里, 这个r没有定义, 猜测应该是rF.
![BESSt公式](https://i.loli.net/2019/08/19/KS6T4azZOhjdLv9.png)

* [Double K SRK/T公式](https://www.ncbi.nlm.nih.gov/pubmed/14670413)的文献里, rpre2和Cw2的2都应该是上标, 是平方.
![double K](https://i.loli.net/2019/08/19/UJnhDqfbxR7eGgF.png)

到不完全是吹毛求疵, 而是你直接对着文献敲代码运行结果肯定是错的. 也许有一天强AI能够自行阅读医学文献的时候, 一定会惊异人类的容错能力. 这也算是人类的自我保护吧.

另外, 有些公式的来源真是...我复现Hoffer Q公式的时候, 发现还有tan K这样的过程, 对角膜曲率K求正切? 什么道理, 这量纲不对啊. 是不是印错了? 于是[仔细读原文](https://sci-hub.tw/10.1016/S0886-3350(13)80338-0).

![Haigis](https://i.loli.net/2019/08/19/Xch1WpuDea6kJ42.png)

原来是Hoffer老先生觉得之前的回归曲线不直, 看起来像tangent曲线, 于是用卡西欧fx-8500G图形计算器开始试, 试啊试, 直到凑出来的公式符合曲线的形态(by trial and error, until a formular produced the desired curve).

上古文献里的八卦真多.

# excel实现

考虑到真正的眼科医生, 是不大可能认真看python程序的, 也不大可能真的去点一下azure notebooks上的clone按钮, 更不可能有一天自己写个处理数据的程序, 用import把我写好的公式导入. 

(是的, 我了解你们, 看看“什么值得买”类的评测才是临床看病的正经事, 至于原理不重要, 实现反正机器都有内置的. 我对你们很绝望, 但我仍然爱你们)

所以我随手写了个[excel文件](https://github.com/goldengrape/IOL_calculate_with_post_corneal_refractive_surgery/raw/master/IOL_calc.xlsx).
里面包含了Double K SRK/T、SRK/T、 Hoffer Q、Haigis、Haigis L、Shammas、BESSt公式, 以及一个简单的术后K值转换公式. (原来VB的函数和python差不多, 几乎可以复制粘贴)

![excel](https://i.loli.net/2019/08/19/H8hRcxvlanGTspz.png)

只要像引用普通的excel函数那样使用就可以了. 如果遇到要处理几百个病人数据, 对比上面这些公式的结果, 又懒得一个一个往IOL Master或者PentaCam机器里输入, 那么就可以用这个excel文件了. 

但这些公式只是绑定到这个文件里的, 暂时我还没搞定如何弄成一个可以导入到公式库里面的东西. 

**以上开源小代码, 作为医师节小礼物送给各位同道. 祝医师节快乐.**