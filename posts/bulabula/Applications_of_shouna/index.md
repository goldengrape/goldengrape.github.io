<!--
.. title: 收纳学应用: 层次索引与LRU断舍离(上)
.. slug: Applications_of_shouna
.. date: 2020-9-30 0:00:06 UTC+08:00
.. tags: 
.. category:
.. link:
.. description:
.. type: text
-->

在以前的《收纳学导论》中, 我们已经介绍了“收纳”这个词汇的含义：

* __收__，是将多个物体限制活动度，使之无法与其他交互。
* __纳__，是将多个物体集中，降低所暴露的表面积。

在本讲中, 将对《收纳学导论》中的理论知识进行实际应用. 本讲使用的是收纳活动强度最高的__搬家__过程. 在搬家活动中, 为了方便运输, 需要将居家物品进行高强度的收纳, 而到达新居以后, 又要将物品恢复到使用状态. 以下详述之. 

![屏幕快照 2020-09-30 01.36.04](https://i.loli.net/2020/09/30/HdLNu2SKwGIqhpr.png)


<!-- TEASER_END -->

## 收拾过程

### 以高熵对抗拖延

搬家时可能有家具, 家具是物品聚集的场所, 是可以暂存物品的场所, 是各种物品可以缓存的位置. 

先消灭它们. 如破釜沉舟.

当先拆除了家具了以后, 所有的物品便无处藏身, 屋子里也无容身之处. 此时就是收纳背水一战之时, 唯有破釜沉舟, 才能一鼓作气, 否则再而衰三而竭, 陷入绵绵不绝的拖延之中. 

### 同时摆开

搬家是唯一可以断舍离的时间段, 只有在搬家时才能对自己拥有的物品做一次完整的检视, 因此要务必珍惜这一场景. 在搬家收拾中, 物品的形状和用途是两个非平行的向量, 有些时候甚至是正交的. 如果仅仅以最小体积作为目标, 则装进一个盒子里的不一定是相关的, 反之亦然. 所以在收纳时往往需要折衷, 而且在给定形状的箱子内放入最多的物品, 本来就是一个非常困难的问题, 需要反复试错. 于是就可能出现如下场景: 

* 如果向一个容器中依次装入物体, 有N个待选物, 放入一个后, 发现不合适取出再拿下一个, 这样的复杂度为O(N^2)
* 但如果有M个容器, 有N个待选物, 拿出一个后, 放入其中某一个合适的容器, 则复杂度很可能降低至O(N)

因此, 在面前同时摆开若干容器是有益的. 

### 层次

> __收__，是将多个物体限制活动度，使之无法与其他交互。

__纸箱里面可以套纸盒.__

物品如果直接放入纸箱, 物品之间还可以互相交互, 其熵远远大于先放入纸盒在装入纸箱. 

在实际操作中, 推荐:

* 3号纸箱(430mmx210mmx270mm)
* T4飞机盒(250mmx200mmx70mm)

考虑到纸的厚度, 一个3号纸箱中可以装入5-6个T4飞机盒, 如果装入太紧, 可能很难取出, 所以需要在最后一个盒子装入前先放入一截绳子, 方便拽出. 

### 索引

要使用物品, 需要先找到它. 也就是获得它的位置, 可以直接目视找到它的实体, 也可以找到记录它位置的数据. 

显然是用CTRL+F找数据更方便. 

在收纳时, 就要有一个数据表, 其中记录着每个物体的位置. 听起来是个很大的工程, 但如果做好了层次收纳, 并且有合适的工具, 这个并不困难. 

* 对每个纸箱命名
* 对纸箱内的每个纸盒命名
* 对每个纸盒内的物品进行记录

命名很随意, 我使用的是《千字文》命名纸箱, 用数字序号命名纸盒, 例如:

* __天__
  * 001
    手写板, 体感摄像头...

记录的过程可以是在纸盒装满时, 只需要用语音输入工具一边看着一边念出物品的名字即可. 开始时可以只使用markdown文件进行记录, 因为在vscode中使用markdown可以很方便对不同目录层级进行折叠, 这样输入与查找时都不算凌乱, 日后对于markdown也比较容易再转换成json甚至csv数据表. 


