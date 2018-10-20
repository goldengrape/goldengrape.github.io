<!--
.. title: MD5密码生成器的iOS捷径版本
.. slug: MD5-pwd-creator-iOS-shortcut
.. date: 2018-10-20 12:00:00 UTC+08:00
.. tags: lifescience
.. category: lifescience
.. link:
.. description:
.. type: text
-->

这是我很久以前做的一个[密码生成器](https://github.com/goldengrape/md5-password-creator), 之后我还一直在用它来管理我的密码. 有了iOS捷径以后, 发现“捷径”里面也有哈希运算, 于是就顺手戳了一个.

[点这里获取捷径](https://www.icloud.com/shortcuts/d65bc3750eae4925b0faaf9a81333671)
在导入时, 可能会要求“加盐”, 也就是一段混淆用的字符串, 如果您以前用过我的密码生成器, 请和原来设定的一样, 如果没用过, 那么可以随意设定一段话, 只要在导入各个iOS设备时保持一样的输入就可以了.

然后保存到主屏幕就可以生成一个类似单独app的图标, 每次需要输入密码时打开它, 输入主密码和网站/应用名, 它就可以计算出一个子密码, 并且同时复制到剪贴板上, 只需要再粘贴到密码输入框里就可以了.

有兴趣详细了解的继续看:
<!-- TEASER_END -->

以前的核心代码就这一小段:
```javascript
var rawString = ($("srcbox1").value || '')
			+ (salt)
			+ ($("srcbox2").value || '')
			+ ($("version").value || '');
var str_md5 = md5(rawString);
var str_base64=b64encode(str_md5);
```

密码=base64(md5( 主密码+盐+网站名+版本) )

在iOS捷径中, 变量是可以为一个列表的, 可以用“添加到变量”, 将内容加入到列表中,

字符串的合并使用的是“合并文本”, 如果传入的是一个列表变量, 就是把列表中的文本join起来.

捷径中没有找到字符串切片的函数, 但有“匹配文本”, 可以用上正则表达式, 取出前N个字符的正则表达式就是```^[0-9a-zA-Z]{1,N}```

其他没有什么好解释的了, 为了和以前密码生成器的结果一致, 我使用的是“2012sprint/2012summer...”这样的字符串作为版本, 您可以根据自己的需求修改.
