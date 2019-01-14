<!--
.. title: 用Gollum建立wiki
.. slug: gollum-wiki
.. date: 2019-1-15 2:00 UTC+08:00
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->

__目的:__ 建立一个文献阅读笔记.

我想要一个看文献记录笔记的工具, 由于有http://sci-hub.tw  很方便找到全文, 而且我并不需要严格的引文管理/插入这样的操作, 所以只需要记录文献的标题和DOI即可. 在阅读中的笔记, 用blog不太合适, 因为还不完全是一个时间线的模式, 一篇文献可能从不同的角度, 在不同时间阅读的时候, 会产生不同的内容, 所以要动态更新. 文献中引用的知识或者信息, 可能还有交叉引用的可能. 于是我打算用wiki来做这件事情.

__方法:__ 建立一个wiki
<!-- TEASER_END -->

现在建立这类的工具, 必须有一份本地的, 有一份云端的. 单纯本地, 长时间不写, 就不知道丢到哪里去了; 单纯云端, 那天服务商倒闭/ 付费/ 降权/ 导入导出, 也是一堆麻烦.

所以, 必须有本地一份, 远端一份. 本blog也是如此.

我选择的本地应用是gollum, 远端是github.

1. 按照gollum的[官方安装说明](https://github.com/gollum/gollum/wiki/Installation)进行操作, mac上按官方homebrew方式安装成功. (真是难得的开源软件, 居然一次成功)
1. 有一个中文文件/目录名称的bug, 所以补充安装`gem install gollum-rugged_adapter`
1. github上随便建一个github repository, 到wiki页面, 找到wiki的git地址, (与repo本身的地址是不同的), 然后git clone到本地
1. 运行`gollum --mathjax  --adapter rugged`, 启动本地服务
1. 用浏览器打开 localhost:4567
1. 用markdown语法直接写文档
1. 如果对wiki不熟, 新建一个页面使用`[[文件名]]`的方式直接写出来就可以了. save以后双击就可以产生新的页面.
1. 写好以后用git命令add,commit,push到远端

本地以markdown的.md文件形式保存, 使用git push 推到远端.
当使用gollum --mathjax启动时, 支持$$包裹的LaTeX数学公式.
远端github那边是否能够正常显示LaTeX我不在乎.(迟早吧, 要不太可耻了)

文献按照领域归类在不同的页面路径之下, 文献笔记的页面中记录文献的标题和DOI, 以及指向sci-hub的全文链接. 文献中的图片需要记录原始文献中的Figure编号, 如果有html全文, 则指向原始文献页面中的图片地址, 如果没有html全文, 则在PDF中截图, 并将截图存放在网上免费的公共图库中. 如果图片丢失, 可以从原文中查找.

__结果:__

整个过程还挺容易的.

__讨论:__

Gollum作为一个开源软件,

* 居然按照原生说明一次安装成功,
* 居然在国内运行良好不用换源,
* 居然只遇到一个中文bug, 锅还是别人的.

怎么说呢, 实在是太不矜持了.

如果不想自己麻烦, 还有其他网友推荐的服务:

* [Zotero](https://www.zotero.org/)
* [Hackmd](https://hackmd.io)






<!-- EOF -->
