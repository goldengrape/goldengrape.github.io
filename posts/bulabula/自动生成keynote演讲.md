<!--
.. title: 自动生成Keynote演讲视频
.. slug: auto_keynote_presentation
.. date: 2018-8-26 10:00 UTC+08:00
.. tags: applescript, 教程, 现代眼科医生知识扩展包
.. category: applescript
.. link:
.. description:
.. type: text
-->

## 目的:

用mac上的系统语音, 自动播放keynote幻灯, 并且朗读keynote中的“演讲者备注”, 如果页面中有动画, 就依次播放完动画, 然后再切换到下一页.

<!-- <iframe width="560" height="315" src="https://www.youtube.com/embed/AOMDt7xrIU4" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe> -->

## 使用方法:
1. 到这个[gist页面](https://gist.github.com/goldengrape/eb4359a6467c5196435e469708c95f11), 点击Download zip, 将代码下载到电脑上, 然后解压缩得到“Simple Play and Say.scpt”文件
2. 制作好keynote, 保持当前文档打开状态
3. 双击打开“Simple Play and Say.scpt”文件, 然后运行脚本
4. QuickTime Player会自动录制屏幕播放过程. 然后可以保存或者导出成其他分辨率的视频.

这种方式可以快速生成演讲视频, 如果讲稿中有地方需要修改, 只要改动字符就可以了, 不必像对着镜头讲课录像那种必须要重新剪辑或者重新配音.

而且说个英文什么的也很方便, 只是中文语音目前只有“婷婷”可以用.

## 进阶使用方法:
<!-- TEASER_END -->
直接使用QuickTime进行屏幕录像的时候, 默认使用的是“内置麦克风”, 如果环境比较嘈杂, 那么背景音也会录下来.

解决的方法是让QuickTime进行“内录”, 也就是直接劫持声卡的声音. 有一个很久远的开源软件可以达成这个目的, [Soundflower](https://github.com/mattingalls/Soundflower/releases), 点击下载安装以后, 将出现两个新的声卡.

先打开一次QuickTime Player, 新建屏幕录像, 然后点击录像按钮旁边的展开箭头, 将麦克风设定为Soundflower(2ch)

![屏幕快照 2018-08-26 10.59.06](https://i.loli.net/2018/08/26/5b8217b2b8a7e.png)

QuickTime里面貌似设定一次以后就默认保持这种设置了.

然后在运行脚本播放keynote之前, 要将系统的声音输出也设定到Soundflower(2ch)虚拟声卡上. 方法是点击屏幕顶部菜单栏中的音量图标, 就可以直接修改了.

![屏幕快照 2018-08-26 11.02.25](https://i.loli.net/2018/08/26/5b821858cc1bf.png)

记得在重放的时候, 将声音的输出设备修改会“内置扬声器”, 否则就听不到声音了.

## 代码解释

代码修改自Sal Soghoian的[iwork & automation网站](https://iworkautomation.com/keynote/slide-presenter-notes.html)

我添加了使用QuickTime进行屏幕录像的几段.

之前一直无法解决自动播放动画的问题, 经过一上午的尝试(我可真无聊), 终于这样解决了:
```
repeat 10 times
    tell document 1
		set cNum to (get slide number of current slide)
    end tell
    if cNum is not equal to i then
		exit repeat
    else
		show next
		say "," -- I really don't know why I have to say something here, english comma is a sound of silence
    end if
end repeat
```
每个页面内“点击下一个”, 不超过10次, 如果你的动画太多, 可以修改这个数字. 但我建议还不如分成两页幻灯.

然后去判断现在是不是还在当前页面, 或者已经是切换到了下一张, 如果切换了, 就跳出循环, 如果还在这一页, 就继续“点击下一个”, 但如果仅仅这么写, 就会出现一口气连续点击了10次, 直接跳到结尾了.

我试过很多方法, 比如delay, do shell script "sleep " 之类, 都无法解决, 后来发现必须用say说点什么, 但又不想让在这里真的说点什么, 于是就说个逗号吧, 也算是某种“Sound of Silence”
