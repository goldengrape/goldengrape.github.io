<!--
.. title: uptodate汉化方法
.. slug: uptodate-zh-Hans
.. date: 2020-3-17 10:00 UTC+08:00
.. tags: 
.. category: 
.. link:
.. description:
.. type: text
-->

有个小技巧, 时间一长自己也容易忘, 所以记录下来:

1. 登陆英文版uptodate, 查询到需要的文章以后, 点击share, 然后发送给自己.
2. 收到email以后, 复制链接, 会得到这样的链接:
https://www.uptodate.com/contents/pathophysiology-clinical-manifestations-and-diagnosis-of-migraine-in-adults?csi=abcdabcd-1111-2222-3333-abcdabcdabcd&source=contentShare
3. 在contents/后面加入zh-Hans/, 得到:
https://www.uptodate.com/contents/zh-Hans/pathophysiology-clinical-manifestations-and-diagnosis-of-migraine-in-adults?csi=abcdabcd-1111-2222-3333-abcdabcdabcd&source=contentShare
4. 开启一个无痕浏览模式的页面, 将修改好的链接贴进去打开, 得到中文版. 

解释: 

* zh-Hans是简体中文, 如果需要其他语言, 如果有的话, 可以更换成其他语言代码, 参考[ISO 639-1 Language Codes](https://www.w3schools.com/tags/ref_language_codes.asp), 但我测试繁体中文zh-Hant失败. 
* 中文版的结果不是机器翻译得到, 是人工翻译后的结果, 与uptodate.cn相同. 
* 链接是静态的, 可以在微信或其他社交次网络上分享, 并且接收方可以直接打开看到内容, 但是,
* csi=后面的一串数字显然是对分享认证的32位Hash代码, 可能每个人每个内容都会不同, 其中可能带有与注册身份相关的信息. 
* 如果在英文版状态下登陆, 打开中文版的链接仍然显示是英文, 所以需要切换到一个无痕模式, 相当于未登陆. 