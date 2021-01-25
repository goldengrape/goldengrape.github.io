<!--
.. title: 收纳学应用: 层次索引与LRU断舍离(下)
.. slug: Applications_of_shouna_2
.. date: 2020-10-20 0:00:06 UTC+08:00
.. tags: 
.. category:
.. link:
.. description:
.. type: text
-->

按照上集的方式进行收纳, 将所有的零碎物品装入同一型号的纸盒、纸箱, 并且建立索引文档以后, 就可以开始LRU收纳和LRU断舍离了. 

LRU, 是Least Recently Used的缩写, 即最近最少使用, 是一种缓存清理算法, 将闲置不用时间最长的内容清理掉. 

>尽管创新性高速缓存方案品种繁多，其中一些在适当的条件下甚至可以击败最近最少使用法，但是最近最少使用法（以及在该策略基础上做出的一些细微调整）仍然深受计算机科学家们的喜爱，并且在开发各种应用程序时得到不同程度的应用。----[《算法之美--指导工作与生活的算法》](https://book.douban.com/subject/30155731/)

<!-- TEASER_END -->

受到这本[《算法之美--指导工作与生活的算法》](https://book.douban.com/subject/30155731/)的启发, 我决定实施其中提到的「家庭生活中的“高速缓存”」方案, 

> 当你决定物品该扔还是该留时，最近最少使用原则可能是一个有效的指导原则，其效果比先进先出原则好得多。如果你现在还不时穿一穿上大学穿的T恤，那就没有必要把它扔掉。但是，你好久没穿过的那条格子裤该如何处理？还是把它送到旧货店吧。

## LRU收纳

准备新的纸盒, 称为缓存纸盒, 或者统一的容器, 比如[hengdm建议使用PVC鞋盒](https://twitter.com/hengdm/status/1318051349108420608) .

重新编号, 之前基础收纳时, 我使用的编号是从001到099, 那么新的编号系统可以从101到199. 当然你也可以使用A001-A999之类.

* 每日把工作台上的东西, 一股脑扔进一个缓存纸盒里, 缓存纸盒就放在桌旁即可. 
* 当第一个缓存纸盒内装满了以后, 用语音输入将内部的物品记录, 然后缓存纸盒封装, 放入附近的一个书架上. 
* 开启第二个缓存纸盒, 继续每日把工作台上的东西扔进新的缓存纸盒里, 直到装满, 不断重复. 
* 当书架上的缓存纸盒放满了, 就按序号移入更远更大的储藏空间, 比如柜子里面、阳台、甚至车库或者什么远程仓库. 

LRU的方式中最重要的变化是, 以使用物品的时间进行收纳, 而不是物品自身的属性, 也就是说不是按照类别, 这是非常反直觉的部分. 

LRU收纳的优势在于, 收拾东西时的成本极低, 不需要按照类别反复往返于工作台和各个储物空间. 东西乱, 在于懒得整理, 懒是因为麻烦, 把所有的物品一股脑扔进一个箱子, 算是最不麻烦的操作了. 

LRU收纳降低了收拾东西时的成本, 但一定程度上提高了取用物品时的成本, 不过按照“刚刚用过的东西还可能继续用到”的假设, 第二天工作需要的物品很大概率仍然就是在手边的缓存纸箱中. 但注意, 一旦装满封箱之前, 一定要进行索引记录, 用语音输入, 将劳动成本降到最低. 

## LRU收纳的弊端

体积压缩率低. 

物品是按照时间存储的, 而且有些物品会从早期的缓存盒中取出, 而不放入原缓存盒中. 那么就会有一些盒子并没有装满, 甚至可能比较空. 

体积的问题可以有两种改善方案, 一是使用统一型号的容器, 这样可以很整齐地码放在一起, 整整一面墙的纸盒, 很可能比左一个书架右一个立柜要清爽得多; 另一种改善, 就是扔, 也就是LRU断舍离. 

## LRU断舍离

按照时间进行收纳, 就可以按照时间进行断舍离了. 

随着时间的进展, 可以在1年、2年、3年的时间点, 去检查那些在早期序号纸盒里的东西, 比如基础收纳的001-099里, 可能很多东西就再也没有被拿出来过, 或者缓存纸盒已经编号到了399, 那么101纸盒里的东西可能也很久没用过了. 那么他们很可能是可以扔掉的. 