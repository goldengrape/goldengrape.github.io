<!--
.. title: 如何向成人灌输一个观点
.. slug: how-to-inception
.. date: 2018-01-21 16:30 UTC+08:00
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->

在上一篇["统计图整理"](../../python/dejunkifying-a-plot)中, 展示了如何把一个具有浓郁乡土气息的bar
![p0](https://i.loli.net/2018/01/21/5a644e647a799.png)
变成性冷淡的bar:
![p7](https://i.loli.net/2018/01/21/5a644e64a71b6.png)

大家的反馈主要是对Remove lines到direct label的那一部分不认同. 也就是从去掉grid, 去掉座标轴, 到直接将数据标注到bar上.
![p5](https://i.loli.net/2018/01/21/5a644e64a705b.png)

![p7](https://i.loli.net/2018/01/21/5a644e64a71b6.png)

专业设计师如西乔都认为["觉得水平线还是应该保留，目前有些影响可读性"](https://twitter.com/arthur369/status/954825055908843521), 其实我也有类似的感觉. 很可能这是大多数人的感觉.

在["统计图整理"](../../python/dejunkifying-a-plot)一文中我说,

>如果做乙方的话, 一定要花足够长的时间给甲方洗脑, 洗到less is more形成本能. 如果你省掉了什么时间, 一定会乘10花到工作时间上.

我只讲了目的, 没有讲解方法. 作为完整的课程, cousera这门课不仅仅讲解了如何作图, 实际上还悄悄演示了如何"洗脑".
<!-- TEASER_END -->

# 成人教育的特点

面向成人的教育与面向青少年的学校教育不同, 成人有自己的思想, 如果教师的观点与学生现存的观点相抵触, 是很难将教师的观点植入进学生心中的.

在cousera老师讲课的时候, 学生也是某种程度的"甲方", "应当保留水平线"是很多人预存的观点. 那么老师在讲课时, 要么停止在这一步之前, 不与学生发生冲突, 要么就要预先清除障碍, 为植入观点做准备.

# 过程简述

[课程视频](https://www.coursera.org/learn/python-plotting/lecture/qFnP9/graphical-heuristics-data-ink-ratio-edward-tufte), 可能需要选课或者至少旁听才能看到. 以文字简述之.

## 1. 连续建立认同感

在提出data-ink是不可或缺的, 和chart junk应当尽量抛弃这个原则以后, 先进行一组操作

* Remove Background Colors ->
* Remove redundant labels ->
* Remove Borders ->
* Reduce Colors ->
* Remove special effect ->
* Remove Shade

这些步骤中, 很容易取得学生们的认同. 其中在reduce colors时, 老师说明了作者目的是为了以培根与其他食物相比. 那么只保留培根的颜色作为突出是很容易接受的.

## 2. 设计问题

在cousera的视频上, 有课堂提问功能, 就是视频正在播放时突然停止, 显示出一道选择题或者填空题, 学生回答, 提交答案, 给予学生反馈以后, 视频再继续进行. 于是在这里,

突然出现了一个问题:
看下面的统计图, 请估计Bacon和Potato Chips之间的差距( ), 并估计Bacon与Pizza之间的差距( ).
![p5](https://i.loli.net/2018/01/21/5a644e64a705b.png)

这其实是个挺好玩的问题, 我相信您看到这个也会跃跃欲试猜测一下.

## 3. 引导推理

显然不论目测如何精确, 多多少少还是会有些误差的, 我目测的已经是相当准确了, 我当时估计Bacon和Potato Chips之间的差距=10, Bacon与Pizza之间的差距=240.

然后视频中给出反馈542-533=9, 533-296=237.

接着老师站出来说话了:

> 大家看, 虽然有水平线, 但这些水平线并不能精确帮我们分析差距啊. 好像也帮不上忙呢.

接着应当又重复一遍data-ink的定义, 强调是non-erasable core. (应当这样, 可惜实际上老师在这里没有做)

## 4. 得到目标结论

老师接着说:

> 既然水平线也帮不上忙, 那么所以, 不如就此去掉吧.
但去掉水平线以后跟y轴又不好比对, 那干脆把数据直接标注在每个柱子上.
这样虽然读者要计算一下. 但却可以准确获得信息哦.

# 复盘

面向成人的教育, 不可以直接进行观点的灌输. 需要由成人自己推理得出倾向, 然后在引导至目标观点上.

比如你想灌输的观点是D点, 那么需要:

1. 先给出基本概念, 然后从大家都认同的A点开始给基本概念感性认识,
2. 接着在B点上抛出问题,
3. 在C点引导大家一起推理, 推理时要引用预先设定的基本概念,
4. 最后由学生自行得出结论D.

看到了吧, 每一个课堂提问其实是精心策划的.

----
附课程字幕:
>3:30
There's still a lot of gridwork left in this image and it's a bit unclear what the value of this gridwork is, so we're going to drop it. Now grids can be valuable, but they're often just a distraction. For the moment though, study the image. What's the difference in the number of calories between bacon, our data point of interest, and say, potato chips or chili dogs?

插入随堂测验

>3:52
Just removing the lines doesn't make it easier to read. But the values of the data are pretty simple here. So let's directly label each bar in the graphic.

<!-- EOF -->
<!-- 其他图片
![p1](https://i.loli.net/2018/01/21/5a644e6417464.png)
![p2](https://i.loli.net/2018/01/21/5a644e643057d.png)
![p3](https://i.loli.net/2018/01/21/5a644e642c6df.png)
![p4](https://i.loli.net/2018/01/21/5a644e640b22d.png)
![p5](https://i.loli.net/2018/01/21/5a644e64a705b.png)
![p6](https://i.loli.net/2018/01/21/5a644e640b1d6.png) -->
