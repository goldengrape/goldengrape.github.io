<!--
.. title: 那些在线的jupyter
.. slug: na-xie-zai-xian-de-jupyter
.. date: 2017-12-18 03:19:31 UTC+08:00
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->

# Jupyter

如果你是python的初学者, 非常推荐Jupyter.

[Juypter](Jupyter.org)是一个交互式的编程环境,  号称
```
The Notebook has support for over 40 programming languages,
including Python, R, Julia, and Scala.
```
支持超过40种语言, 其中包括Python,  R,  Julia和Scala. 虽然除了Python, 目前提到的其他语言我还都不会, 但是看起来是很强大很有前途的样子.
<!-- TEASER_END -->

Jupyter的编程环境我很喜欢, 你可以写一段markdown图文并茂的说明, 再写一段代码, 然后单独运行刚刚写过的这一段代码, 看到结果, 调试代码, 改好以后再进行下一段.

最终完成的文本+代码, 是所谓的["文学编程"](https://zh.wikipedia.org/wiki/文学编程), 文字甚至图片说明作者的思路, 中间夹杂着代码, 来教导计算机进行操作. 这样带来了完美的可读性.

```
!不要! 相信什么"代码才是最好的注释".
那是穿格子衬衫背双肩背半夜三点还在写代码的专职程序员才相信的东西.
```

如果你不是一个每天必须写代码十几个小时的专业程序员, 而是利用代码去完成自己专业的特殊需求, 可能一个程序要间断好多天才能写完, 那么这种方式能够帮你迅速找到前几天的思路. 继续完成之前的作品.


# 在本地安装Jupyter(跳过吧, 别看)

Jupyter当然可以安装在本地, 安装好[Anaconda](https://www.anaconda.com/)以后, 相对比较容易安装jupyter了.  

但如果你之前只在windows上安装过商业软件, 一路点next, 或者在mac上从dmg中把应用程序直接拖动到文件夹里就可以运行. 那么安装anaconda, jupyter, 以及在运行jupyter时再安装各种python的依赖包, 是非常痛苦的.

完全不建议新手进行, 至于那些常年泡在[linux里面已经 "__久病成医__ "](https://twitter.com/bgm38/status/932512531251216385)的病友, 推荐你们试试.

# 在线的Jupyter

如果你是python的初学者, 非常推荐使用在线的Jupyter.

利用在线的Jupyter要轻松得多, 只需要有网络连接, 有浏览器就可以了. 我测试了mac版的Chrome, Safari, 甚至android上的Chrome和iOS上的Safari, Chrome, 都可以运行在线的Jupyter.

目前已经有这些服务:
## Cocalc
[https://cocalc.com](https://cocalc.com) ,
这是一个科学计算平台, 除了提供jupyter, 还提供了sagemath.
sagemath也是一个强大的数学计算工具, 可以当作一个开源的mathematica, 随手解个方程, 求个微分之列都很方便.

CoCalc已经安装好了大量的python包, 比如numpy, tensorflow, keras, pytorch. . .

Cocalc有免费版和付费版, 免费版没有额外的网络连接, 也就是说你无法在cocalc里面再访问其他网页, 比如你用jupyter写了一个网络服务程序, 那么是无法用在cocalc免费版里面的. 用git也会受限制. 没有网络连接最麻烦的是如果cocalc没有预装的包, 你是无法自行安装的. 不过如果确实是很常用有名的python包, 那么可以向cocalc网站的支持发个email, 他们的响应速度超级快, 很有可能就帮你装好了.

我写过[CoCalc的使用教程](https://goldengrape.github.io/Python-for-ophthalmologist/lesson_01_jupyter.html)

## Azure notebook

[https://notebooks.azure.com](https://notebooks.azure.com)
这是微软提供的在线jupyter服务, 财大气粗的微软提供的内存, cpu, 存储空间都不错.

很有特色的功能有二:
1. 方便一键clone, 看好其他人的做得不错的东西, 可以方便clone一份自己研究.
2. 可以从github导入, 只需要将看中的github repo页面添加, 就可以自动clone, 如果对方更新了, 自己这边也可以方便使用git pull

微软的这个服务是有网络连接的, 你可以远程下载数据或者导入其他的库. 因此如果出现没有预装的库, 可以自己手动安装. 但麻烦的是, 如果你的notebook停用1小时以后, 远程的server就会停止, 然后你之前安装的东西就会被清除(数据和文件不会), 所以如果有额外的库, 就需要在每次打开的时候预先再次安装一遍.

好在会有脚本可以做, 你可以参照这个[帖子](https://github.com/Microsoft/AzureNotebooks/issues/201#issuecomment-338466615)
```
到你的 library > settings > Environment
选择 ShellScript 然后选择 特定的脚本
保存
重启 server
```
安装pytorch的脚本[例子](https://github.com/Microsoft/AzureNotebooks/files/1404777/script.txt):
```
export PATH=~/anaconda3_410/bin:$PATH
conda install pytorch torchvision -c soumith --yes
```
安装其他的库, 只需要在anaconda里面搜索一下conda的安装方法, 然后替换上面脚本中的conda install pytorch那一段.

## 其他

* Mybinder
[https://mybinder.org/](https://mybinder.org/)
这个我也还没用过, 据说可以从github里面直接导入, 生成一个docker. 需要什么库的话, 好像也可以通过脚本预先声明, 不一定像azure notebook那样要反复安装.

* Google Colaboratory
[https://colab.research.google.com/](https://colab.research.google.com/)
这是Google的jupyter服务, 但目前还没有完全开放, 点击注册以后会有"您已成功加入到候补名单。一旦 Colaboratory 可供您使用，我们会立即发送电子邮件通知您。"

# 在移动设备上使用

主流的手机/平板浏览器, 上面的服务都可以访问, 编辑的时候稍微有点别扭, 特别是在小屏幕的时候, 操作也还是不够方便, 但如果外接键盘/蓝牙键盘也还是不错的.

除了内置的浏览器, 我还发现了专用的iOS app, [Juno](https://juno.sh/) 目前还处于testflight状态, 可以去他家网页上申请beta测试. Juno中还内置了Mybinder的demo. 如果你购买了cocalc付费版, 也可以开放出一个远程的jupyter server供Juno使用.

# 自己建立Jupyter在线服务

开源社区现在越来越友好了, 有可能的话, 你也可以在自己的服务器或者VPS上建立一个在线的Jupyter服务, 为自己/学生/客户服务. 但我这么怕麻烦的人, 本地电脑都懒得装, 所以我都没有测试过.

* Jupyter Hub: [https://github.com/jupyterhub/jupyterhub](https://github.com/jupyterhub/jupyterhub) 这是jupyter官方的服务器安装程序.

* Binder Hub:  [https://github.com/jupyterhub/binderhub](https://github.com/jupyterhub/binderhub)也是从属与jupyter官方的, 但是用docker技术封装, 大概安装调试会方便一些吧.

* Cocalc/sagemath: [https://github.com/sagemathinc/cocalc](https://github.com/sagemathinc/cocalc) 这个也是用docker的, 还带有sagemath.

ps.
如果你在本地计算机上安装了jupyter, 非常推荐下面这个插件, 能够在保存jupyter文件的时候, 同时保存同名的 .html 和 .py 形式的文件. 这样在其他的python程序中导入自己写的函数会非常方便. 也很容易在github page上发布文档.

[http://protips.maxmasnick.com/ipython-notebooks-automatically-export-py-and-html](http://protips.maxmasnick.com/ipython-notebooks-automatically-export-py-and-html)
EOF()
