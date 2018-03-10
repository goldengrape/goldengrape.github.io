<!--
.. title: Mac上双击打开jupyter文件
.. slug: double-click-open-ipynb
.. date: 2018-3-7 19:00 UTC+08:00
.. tags: python,
.. category:
.. link:
.. description:
.. type: text
-->

jupyter的文件是.ipynb文件, 实际上是纯文本写的json, 但要按可编辑可运行的方式打开它, 有几种方式:

1. 在命令行运行jupyter notebook 文件名
    * 或者在命令行运行jupyter lab 文件名
1. 用nteract打开
1. 在atom里安装jupyter notebook package, 然后用atom打开.

第一种最佳, 但不方便, 我不是常规打开终端的. 第二种有时候特慢, 而且如果没有设置好kernel的话, 运行jupyter文件总是容易报错. 第三种大概比第二种略差, 而且我每次装这个package的时候都会被杀毒软件拦下来.

我很希望有个能够双击打开.ipynb文件的方式. 打开以后还能够正常编辑和运行. 上推一问. 果然在[@xuanyuanzhiyuan](https://twitter.com/xuanyuanzhiyuan/status/971321483896213504)和[@kyleehee](https://twitter.com/kyleehee/status/971317968822038528)的指导下成功了. 写blog以记录之.
<!-- TEASER_END -->

1. 打开Automator(现在中文叫'自动操作')

1. 新建->应用程序
![屏幕快照 2018-03-07 17.58.12](https://i.loli.net/2018/03/07/5a9fc9e347028.png)
1. 选取"资源库"->"实用工具"->"运行AppleScipt"
![屏幕快照 2018-03-07 17.58.33](https://i.loli.net/2018/03/07/5a9fc9e2c3842.png)
1. 在右侧"运行AppleScipt"栏里写下:

```AppleScipt
on run {input}
   set the_path to POSIX path of input
   set cmd to "jupyter notebook " & quoted form of the_path
   tell application "System Events" to set terminalIsRunning to exists application process "Terminal"
   tell application "Terminal"
      activate
      if terminalIsRunning is true then
         do script with command cmd
      else
         do script with command cmd in window 1
      end if
   end tell
end run
```
![屏幕快照 2018-03-07 17.59.37](https://i.loli.net/2018/03/07/5a9fc9e29141c.png)
注意"jupyter notebook "末尾一定要有空格. 也可以使用jupyter lab, 看你喜欢. 但前提一定是在进入终端以后可以直接运行jupyter的状态, 如果你需要用anaconda先切换到某个环境下再用jupyter, 那么需要在前面加上另一条do script, 引号里是你需要先运行的命令, 比如要启动myenv这个环境, 平时可能需要输入的是```source activate myenv```, 注意一条命令以后貌似需要delay一下, 后面的数字看情况.
```AppleScipt
do script "source activate myenv"
deply 3
do script with command cmd
```
加入以后完整的是这样的:
```AppleScipt
on run {input}
   set the_path to POSIX path of input
   set cmd to "jupyter notebook " & quoted form of the_path
   tell application "System Events" to set terminalIsRunning to exists application process "Terminal"
   tell application "Terminal"
      activate
      if terminalIsRunning is true then
         do script "source activate myenv"
         deply 3
         do script with command cmd
      else
         do script "source activate myenv" in window 1
         deply 3
         do script with command cmd in window 1
      end if
   end tell
end run
```

5. 保存成一个.app文件. 就成了一个应用程序了. 放进应用程序文件夹, 例如叫jupyter_launcher.app
1. 随便找个.ipynb文件, 右键->显示简介->打开方式->其他, 在应用程序里找到jupyter_launcher,
![屏幕快照 2018-03-07 18.50.54](https://i.loli.net/2018/03/07/5a9fc9e29a031.png)
1. 然后选择"全部更改"

全套完成, 以后就可以双击直接打开jupyter文件了. 会自动先打开一个终端, 然后用jupyter notebook运行, 文件在浏览器里可以显示和编辑并且运行.

* 参考:
https://superuser.com/questions/139352/mac-os-x-how-to-open-vim-in-terminal-when-double-click-on-a-file

<!--
.. title: Mac上双击打开jupyter文件
.. slug: double-click-open-ipynb
.. date: 2018-3-7 19:00 UTC+08:00
.. tags: python,
.. category:
.. link:
.. description:
.. type: text
-->

jupyter的文件是.ipynb文件, 实际上是纯文本写的json, 但要按可编辑可运行的方式打开它, 有几种方式:

1. 在命令行运行jupyter notebook 文件名
    * 或者在命令行运行jupyter lab 文件名
1. 用nteract打开
1. 在atom里安装jupyter notebook package, 然后用atom打开.

第一种最佳, 但不方便, 我不是常规打开终端的. 第二种有时候特慢, 而且如果没有设置好kernel的话, 运行jupyter文件总是容易报错. 第三种大概比第二种略差, 而且我每次装这个package的时候都会被杀毒软件拦下来.

我很希望有个能够双击打开.ipynb文件的方式. 打开以后还能够正常编辑和运行. 上推一问. 果然在[@xuanyuanzhiyuan](https://twitter.com/xuanyuanzhiyuan/status/971321483896213504)和[@kyleehee](https://twitter.com/kyleehee/status/971317968822038528)的指导下成功了. 写blog以记录之.
<!-- TEASER_END -->

1. 打开Automator(现在中文叫'自动操作')

1. 新建->应用程序
![屏幕快照 2018-03-07 17.58.12](https://i.loli.net/2018/03/07/5a9fc9e347028.png)
1. 选取"资源库"->"实用工具"->"运行AppleScipt"
![屏幕快照 2018-03-07 17.58.33](https://i.loli.net/2018/03/07/5a9fc9e2c3842.png)
1. 在右侧"运行AppleScipt"栏里写下:

```AppleScipt
on run {input}
   set the_path to POSIX path of input
   set cmd to "jupyter notebook " & quoted form of the_path
   tell application "System Events" to set terminalIsRunning to exists application process "Terminal"
   tell application "Terminal"
      activate
      if terminalIsRunning is true then
         do script with command cmd
      else
         do script with command cmd in window 1
      end if
   end tell
end run
```
![屏幕快照 2018-03-07 17.59.37](https://i.loli.net/2018/03/07/5a9fc9e29141c.png)
注意"jupyter notebook "末尾一定要有空格. 也可以使用jupyter lab, 看你喜欢. 但前提一定是在进入终端以后可以直接运行jupyter的状态, 如果你需要用anaconda先切换到某个环境下再用jupyter, 那么需要在前面加上另一条do script, 引号里是你需要先运行的命令, 比如要启动myenv这个环境, 平时可能需要输入的是```source activate myenv```, 注意一条命令以后貌似需要delay一下, 后面的数字看情况.
```AppleScipt
do script "source activate myenv"
deply 3
do script with command cmd
```
加入以后完整的是这样的:
```AppleScipt
on run {input}
   set the_path to POSIX path of input
   set cmd to "jupyter notebook " & quoted form of the_path
   tell application "System Events" to set terminalIsRunning to exists application process "Terminal"
   tell application "Terminal"
      activate
      if terminalIsRunning is true then
         do script "source activate myenv"
         deply 3
         do script with command cmd
      else
         do script "source activate myenv" in window 1
         deply 3
         do script with command cmd in window 1
      end if
   end tell
end run
```

5. 保存成一个.app文件. 就成了一个应用程序了. 放进应用程序文件夹, 例如叫jupyter_launcher.app
1. 随便找个.ipynb文件, 右键->显示简介->打开方式->其他, 在应用程序里找到jupyter_launcher,
![屏幕快照 2018-03-07 18.50.54](https://i.loli.net/2018/03/07/5a9fc9e29a031.png)
1. 然后选择"全部更改"

全套完成, 以后就可以双击直接打开jupyter文件了. 会自动先打开一个终端, 然后用jupyter notebook运行, 文件在浏览器里可以显示和编辑并且运行.

* 参考:
https://superuser.com/questions/139352/mac-os-x-how-to-open-vim-in-terminal-when-double-click-on-a-file

----
[My Press.one Signature](https://press.one/file/v?s=4e99e642621a7c01ada7d1ab124068ff803c553cab40e30808c5509f20ef33c90658bb61c60e96af12374f5eb40b0719fdffef99c6627811b68d68a3c37b64890&h=a35b8dd4dbfb7e521c41eaa53d0875b3cf53a426f911ae666bcd0302ccd4721c&a=79c1846bc532ec0cf61ad0f1f5604a80a1387aca&f=P1&v=2)
