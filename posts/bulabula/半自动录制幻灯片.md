<!--
.. title: 半自动录制幻灯片配音
.. slug: semiautomatic_dubbing_slide
.. date: 2019-3-8 12:00 UTC+08:00
.. tags: 
.. category: 
.. link:
.. description:
.. type: text
-->

最近要做一批幻灯片的配音演讲. 之前用的[自动生成keynote演讲](../auto_keynote_presentation)方法突然不好用了, 因为似乎苹果偷偷更新了apple script的函数定义, 一大堆命令都无法识别了. 

但是自动生成配音演讲真的是很方便, 做网络课程的时候, 有什么地方需要更新改正时, 修改文字就好了. 即使是准备现场演讲, 提前生成配音听一遍, 也能够提前对演讲有一个预演, 知道哪些地方需要改进. 

虽然应该自己重新用python写一个, 但本着能拖一天是一天的拖延症思想, 先用现成的东西拼凑连接起来好了. 

于是有如下步骤:
<!-- TEASER_END -->

# 材料:

* iPhone/ iPad
* mac
* 数据线
* MTCoreAudio的AudioMonitor, [softpedia中下载](http://mac.softpedia.com/get/Developer-Tools/MTCoreAudio.shtml) 或mac自家的GarageBand 
* 讯飞阅读 app
* 耳机
* 作者本人

## 软硬件连接方法:

* 用数据线连接iPhone和mac, 解锁iPhone
* 到mac上, 应用程序->实用工具->“音频MIDI设置”, 打开“音频MIDI设置”, 找到自己的iPhone, 点击“启用”
![屏幕快照 2019-03-08 12.07.51](https://i.loli.net/2019/03/08/5c81eb5a0582d.png)

* 把下载下来的MTCoreAudio打开, 找到里面的AudioMonitor, 复制到应用程序中, 
![](https://cdn.guidingtech.com/media/assets/WordPress-Import/2016/01/Screen_Shot_2016-01-25_at_8_00_20_PM.png)

(图片应用自guidingtech.com)

* 插上耳机, 然后运行 Audio Monitor, 将input改成iPhone, 点击Play Through

![屏幕快照 2019-03-08 12.16.18](https://i.loli.net/2019/03/08/5c81eca50fd3f.png)

以上步骤就可以将iPhone里发出的声音作为mac上的音频输入, 并且同时接通音频输入和音响输出, 使自己可以监听到音频过程. 

注意如果不是使用的iphone作为输入和耳机作为输出, 而是用了内建话筒和音箱, 那么可能会引起尖锐的哮鸣.

## 操作流程

1. 撰写演讲脚本, 保存为txt文件.
2. 发送到iPhone上, 用讯飞阅读打开.
3. 打开做好的keynote, “录制幻灯片放映”
4. 点击红色的录音按钮, 倒数3秒后, 在讯飞阅读中播放朗读演讲脚本.
5. 自己听着朗读, 到该翻页的时候翻页. 是的, 这个过程是有人参与的, 所以说是半自动.
6. 播放完成后, 保存, keynote中文件->导出到->视频

# 结果与讨论

效果很好, 而且所有的动画也都可以流畅播放和录制, 如果再DJ一点, 还可以手动暂停语音朗读, 等着动画播放完成. 

建议先高速听一遍, 一边听一边把一些表达稍微修改, 比如数学公式的朗读可能有问题, 有些分词断句可能听起来很怪异, 必要时加个逗号或者空格. 

注意导出的视频文件是m4v后缀, 有些教学网站傻傻的只认mp4文件, 直接改后缀成mp4就行了. 不用再转码.

没找到讯飞朗读里如何人为做一些停顿. 逗号, 句号之类都只是寻常间断, 多个标点也不能把停顿延长.

把iphone作为mac的音频输入, 再同时监听真的很有趣. 好像可以玩很多东西

 