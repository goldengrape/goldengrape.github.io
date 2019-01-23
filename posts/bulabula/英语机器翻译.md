<!--
.. title: 好好学6个月英语, 还是等半年看看机器翻译的水平?
.. slug: Study-English-or-wait-for-machine-translation
.. date: 2019-1-15 21:00 UTC+08:00
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->

如题.

现在机器学习实在进步太快, 好用的工具层出不穷. 列举一下目前使用的工具:

* 浏览网页:

浏览的要求就是看起来快, 大概意思清楚就可以了, 所以我不使用那种查单词的. 而是直接翻译成中英对照的, 现在用的是[彩云小译](http://caiyunapp.com/) , 浏览网页用量比较大, 所以付费订阅中, 每个月1$

* 看文献:

当然主要是医学文献, 有sci-hub看全文非常方便, 只需要把sci-hub.tw/ 加在文献页面网址的前面即可, 这样就能够下载PDF了.

(更新: 我发现很多人不理解把scihub加在文献页面前面的意思)

比如: 在pubmed上查到一篇文献, 网址是:
`https://www.ncbi.nlm.nih.gov/pubmed/30651639/` 

那么通过sci-hub找到的全文网址就是: 
 `sci-hub.tw/https://www.ncbi.nlm.nih.gov/pubmed/30651639/ `

此处要强力推荐这个[TransGod体验版](https://fanyi.transgod.cn/) 专职的医学文献机器翻译, 机翻的可读性还是不错的. 能够机翻PDF, 然后转换成word文件, 不但维持原格式, 连表格都原位翻译, 连上标下标都按原位翻译.

* 写作

我的英语能力, 大概是听>说>>读>=写. 所以有两个辅助工具,

  * 一个是Google Translate, 写好中文看英文, 如果英文翻译得不好, 多半是中文表达不够清楚, 改中文.
  * 另一个是[grammarly](https://app.grammarly.com/), 这个有[Chrome的插件](https://chrome.google.com/webstore/detail/kbfnbcaeplbcioakkpcpgfkobkghlhen), 能够检查出一些语法和拼写错误. 很奇怪的, Google Translate得到的结果里还是时常会有语法错误, 最常见的是丢失冠词. 按说RNN生成的序列这种问题应该概率很低.

现在还缺少比较好用的:

* 专利机器翻译. 不过专利这种东西, 即使用中文写的, 也不是很好懂的. 我自己的发明, 看专利我也不是很明白. 所以, 最好有个“专利语”到“日常口语”, 哪怕是“工程师语”的机器翻译也行.

* 语法检查工具. 每年全球各种英语考试那么多, 改错题也那么多, 不能拿来当语料库么.

以上这些工具, 配合[用Gollum建立的wiki笔记工具](../gollum-wiki), 读文献吐槽文献很爽.

补充一下医学文献的快速浏览过程:

1. 打开[pubmed](https://pubmed.gov/)检索文献
2. 如果有html的全文, 则在文献的右侧有PMC Full Text(free)的图标![图标](https://static.pubmed.gov/portal/portal3rc.fcgi/4183432/img/3977009). 可以直接点击阅读, PMC的阅读器非常棒, 参考文献会放到相应段落旁边, 看综述时非常舒服. 此时可以点击[彩云小译的插件按钮](https://chrome.google.com/webstore/detail/lingocloud-interpreter/jmpepeebcbihafjjadogphmbgiffiajh?hl=zh-CN), 进行中英文对照翻译. 简要浏览, 遇到细节再看英文是具体怎么说的. 
  优选PMC的阅读器, 因为彩云小译有些网页解析有问题, 比如对于JAMA的网站只能翻译前几段, 后面的似乎就忘记了.
3. 如果没有html全文, 在pubmed的网址前面加入sci-hub.tw/ 下载PDF文件, 然后送进[TransGod](https://fanyi.transgod.cn/)里面, 翻译完成后下载word文档浏览译文.
