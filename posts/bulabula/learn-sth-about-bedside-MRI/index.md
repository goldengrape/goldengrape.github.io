<!--
.. title: 学习床旁核磁的知识
.. slug: learn-sth-about-bedside-MRI
.. date: 2020-8-18 12:00 UTC+08:00
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->

在medgadget看到床旁核磁的新闻: [https://www.medgadget.com/2020/08/swoop-portable-mri-cleared-in-u-s-for-bedside-scans.html](https://www.medgadget.com/2020/08/swoop-portable-mri-cleared-in-u-s-for-bedside-scans.html)

![](https://www.medgadget.com/wp-content/uploads/2020/08/hyperfine.jpg)

这家叫[HyperRefine](https://www.hyperfine.io/)的机器通过了FDA的认证. 

真是很厉害, 印象中做核磁还必须是在一间电磁屏蔽的屋子里, 现在居然已经可以推到床旁去做了. 

其他科的同学也觉得不错:
> “神经内外科的兄弟们不用再抬着气管插管的昏迷病人过床了”
> 
>  “移动CT、核磁对于急性卒中救治非常重要，尤其是院前转运途中就可以实施，将大大节省时间，增加时间窗内溶栓和取栓受益人群。值得期待。”

和放射科的同学聊了聊. 

> “这款hyperfine用的是0.06T的永磁体, 成像效果可能和我们熟悉的超高场强相去甚远“
> “最早普及的mr也需要0.2T吧，很模糊，扫描时间也长。但是1.5T以上的超高场强肉眼看上去都差不多了。“
> “目前hyperfine的策略貌似是先训练AI识别图像“

感觉这才是深度学习的正道, 用算法弥补硬件, 产生曾经不可能的应用场景.

## 原理资料

于是来了兴趣. 简单检索了一下. 

Hyperfine的主要技术方案在WO2020028257A2 这个专利里, 
全文:
[https://worldwide.espacenet.com/patent/search/family/067659966/publication/WO2020028257A2?q=pn%3DWO2020028257A2](https://worldwide.espacenet.com/patent/search/family/067659966/publication/WO2020028257A2?q=pn%3DWO2020028257A2)

用了U-net, NVN, GNVN几个深度学习网络, U-net以前见过, 是先压缩, 然后再展开成高分辨率, 在AI for Medical Diagnosis课程里提到过:  [https://www.bilibili.com/video/BV1JT4y1g74P?p=34](https://www.bilibili.com/video/BV1JT4y1g74P?p=34)

GNVN具体的算法描述在这篇论文: [https://msofka.github.io/pdfs/schlemper-miccai19.pdf](https://msofka.github.io/pdfs/schlemper-miccai19.pdf)

类似的技术还可以用在超声和CT上, 发明人之一Michal Sofka, 同时还在给其他几个公司提供算法. [https://msofka.github.io/](https://msofka.github.io/)

采样扫描的顺序不是横竖扫, 可能是三角形或者其他什么形状的网格.

专利中提到用来训练的数据集其实不大, 只有1200个 https://www.humanconnectome.org/study/hcp-young-adult/document/1200-subjects-data-release 当然可能在实际上市之前还能再找到些数据. 

## 潜在的局限

虽然觉得是很了不起的事情, 但对临床医生提示一下: 小心使用了机器学习、深度学习、AI的设备, 所见到的图像不一定是“真实”获得的, 有可能是机器“**脑补**”的. 比如之前说华为的手机可以拍到月亮, 但是拿着对着盘子拍, 也能补上月亮的环形山. 

类似的, 如果在训练用的高清数据集里, 眼球的图像都是完整的, 在眼眶附近出现的总是一个完整的圆环, 在低分辨率的情况下, 比如有几个像素缺失了, 或者这个区域看不清楚, 机器可能就按照高清数据集里常见的方式进行填补, 于是就把眼眶附近“画”出一个完整的圆环. 但如果这个病人有个穿通伤, 恰好就在一两个像素的范围内有异常, 而在训练用的数据集里这种情况很少, 或者压根没出现过, 深度学习就会把这一两个像素当作是噪声, 用一个完整的眼环给替代掉.

目前已知它的数据集只用了1200张, 即使是大量也只可能是几万张十几万张图, 毕竟放射科大夫们很贵. 分配到每一个病种、或者说每一种图像细节的数量会更低一些. 比如十万张核磁, 里面有1千张眼球破裂伤的, (其实就不少了, 每天1个得收集3年多呢), 对于AI来说, 如果看不清楚, 就蒙一个完整眼球, 这样的准确率还可以高达99%. 如果是疾病诊断之类, 可以用ROC曲线来矫正准确率, 但如果是图像细节恢复, 可能挺难的. 还只能用类似准确率的方式描述, 那么面对发生率较低的细节判读时, 临床医生要小心. 