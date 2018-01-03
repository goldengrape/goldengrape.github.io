<!--
.. title: macOS X 中的$PATH
.. slug: macos-x-zhong-de-path
.. date: 2018-01-03 20:38:31 UTC+08:00
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->

贪图享乐装了一个[oh-my-zsh](https://github.com/robbyrussell/oh-my-zsh), 结果装好以后突然发现在终端中常用的命令都找不到了, 什么source activate , jupyter , conda ,敲完了以后都是一句:
```
    zsh: command not found:
```

真是一脑门子汗呐. 感觉就是召唤了一个不太熟的魔兽, 看起来很强大, 但不知道如何驾驭之.

<!-- TEASER_END -->

# 问题:

问题出在了zsh在加载的时候没有加载合适的PATH, 在unix/linux/mac这类系统下, 有个$PATH, 负责存储调用命令时的搜索路径, 我本能地觉得这个东西很复杂, 一直刻意避开, 现在也没办法了, 只好硬着头皮学了学.

要看自己的$PATH, 可以

```
echo "$PATH"
```

返回的结果可能是:
```
/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:/Library/TeX/texbin:/opt/X11/bin
```

一串长长的字符串, 中间用:作为分隔. 里面记录了各种路径. 我启动zsh以后, 这个里面没有包含anaconda的路径, 导致我想运行anaconda中的命令会出错.

# 解决:

编辑$PATH.

在macOS上, 有两种方案可以编辑$PATH:

1. 在 /etc/paths.d 目录里添加.
1. 用编辑器往 ~/.bash_profile 文件里export.

后一种我仍然不太明白, 而且在我的电脑上好像也没成功. 我来说说第一种方案.

PATH是以文件的形式存储在/etc/paths.d这个目录中的, 要看当前已经存储的文件, 可以:
```
ls -l /etc/paths.d/
```

可能返回的结果是:

    -rw-r--r--  1 root  wheel  13 10 13  2015 40-XQuartz
    -rw-r--r--  1 root  wheel  22 10 13  2015 TeX

如果查看文件里的内容, 比如看40-XQuartz
```
cat /etc/paths.d/40-XQuartz
```

那么将看到

    /opt/X11/bin

也就是需要找到的路径. 那么仿照这个, 也建立一个文件, 文件里面保存上要添加的路径即可.

我还是习惯用atom作为编辑器, 所以:
```
sudo atom /etc/paths.d/anaconda3
```

输入密码后, atom会在这个目录下新建一个叫做anaconda3的文件, 并且打开处于可编辑状态.

于是我在这个文件里添加上我的anaconda3需要加入的path, 这个路径可以[从anaconda的faq里面查到](https://docs.anaconda.com/anaconda/faq#what-is-the-default-path-for-installing-anaconda)
```
/Users/goldengrape/anaconda3/bin
```

加入以后保存. 然后关闭终端, 再次重新打开, 这个路径就被加载好了, 不管是在bash下, 还是在zsh下都可以用了.

如果还有其他软件需要特定设定$PATH, 也可以用同样的办法建立文件, 写入路径. 我个人比较喜欢这种方式, 看着清楚, 也不太受到切换shell的影响.

* 参考:

[Mac OS X: Set / Change $PATH Variable](https://www.cyberciti.biz/faq/appleosx-bash-unix-change-set-path-environment-variable/)
