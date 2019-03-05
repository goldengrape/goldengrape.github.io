<!--
.. title: 拍摄开花过程
.. slug: flower-blossom
.. date: 2019-3-5 22:00 UTC+08:00
.. tags: lifescience
.. category: 
.. link:
.. description:
.. type: text
-->

自己养的栀子花好不容易要开花了. 

于是用相机记录下来:
![](../../../images/flower_blossom.gif)

再记录一下拍摄过程:
<!-- TEASER_END -->

# 材料与方法:

## 工具:
* 待开放栀子花,
* Nokia X6手机,
* 三脚架, 手机夹子
* Android
上的[Open Camera App](https://apkpure.com/cn/open-camera/net.sourceforge.opencamera): 这是一个很强悍的相机app, 能够自定义很多参数.
* [可外接电源的LED补光灯](https://item.taobao.com/item.htm?id=574484611225), 这几天在做另一个项目, 买了一堆网红主播用品.
* [FFmpeg](https://www.ffmpeg.org/), 这是一个开源命令行软件. 在mac上用homebrew完全安装ffmpeg要费些功夫, (开源软件嘛, 一步安装到位就太不矜持了), [要先brew tap](https://trac.ffmpeg.org/wiki/CompilationGuide/macOS) 然后再[安装各个options](https://gist.github.com/Piasy/b5dfd5c048eb69d1b91719988c0325d8) 
## 摆放

![IMG_2273](https://i.loli.net/2019/03/05/5c7e87ec2fa1e.jpg)

## 拍摄参数设定
![Screenshot_20190305-223636](https://i.loli.net/2019/03/05/5c7e8ab0f22d9.png)
* 连拍模式: 无限
* 连拍模式间隔: 目前我设定的是30秒

## 软件处理
使用ffmpeg合成图像.

* 将目录里的所有jpg图像合成为视频, 帧速率=30

`ffmpeg -framerate 30 -pattern_type glob -i '*.jpg' flower.mp4`

* 实测发现画面太大, 于是只截取画面中的一部分(宽=2200, 高=2200, x起点=800, y起点=700)

`ffmpeg -framerate 30 -pattern_type glob -i '*.jpg' -vf "crop=2200:2200:800:700" flower.mp4`

* 微信朋友圈只有10秒, 所以提高速度, 其中setpts=10/实际时间

`ffmpeg -i flower.mp4 -b:v 2000k -filter:v "setpts=0.05714286*PTS" output.mp4`

# 结果与讨论

## 结果:

未处理的拍摄样张:
![IMG_20190305_065624_DRO](https://i.loli.net/2019/03/05/5c7e8fbfe5da4.jpg)

处理后的视频:

![](../../../images/flower_blossom.gif)

## 讨论
花开过程大约是2天, 一共拍摄了5200多张, 照片总容量达到了12G, 原本担心ffmpeg处理这么大的量会吃力, 没想到还是很容易就完成了. 

平均来说, 每30秒拍摄一张有点短, 造成数据量很大, 不过反正ffmpeg处理起来也不吃力, 但如果使用常规的软件来处理, 比如photoshop之类, 有可能会吃不消. 

但花瓣并不是匀速打开的, 最外层的花瓣类似是弹开的样子, 特别是第4片花瓣, 30秒之内张开了60度以上. 所以如果拍摄间隔设定太久, 就可能捕捉不到. 

关于摆放位置, 现在觉得应该把镜头正对花的中心, 而不应该从侧面拍摄, 会有一半的花瓣看不见. 还是应该尽可能把镜头靠近, 使花占主体部分, 而不是后期剪裁, 感觉花朵本身的分辨率还是欠缺. 

背景颜色变化明显, 是因为日光的原因. 晚上由补光灯照明, 白天日光造成的影响很明显. 补光灯应该再亮一些, 噪点还是太明显. 我不知道如果完全遮蔽日光, 使用人造光源照明, 是否会对开花过程有影响. 毕竟LED的光谱与日光还是有很大不同. 

