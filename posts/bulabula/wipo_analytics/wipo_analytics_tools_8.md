<!--
.. title: 专利分析工具概述(8)文本挖掘
.. slug: WIPO_analytics_tools_8
.. date: 2019-12-07 12:08 UTC+08:00
.. tags: WIPO_analytics_tools, patent
.. category: patent
.. link:
.. description:
.. type: text
-->
## 文本挖掘

那里有很多文本挖掘工具，其中许多是免费或开源的。 这是我们发现的一些。
<!-- TEASER_END -->

### [Jigsaw Visual Analytics](http://www.cc.gatech.edu/gvu/ii/jigsaw/)

用于探索和理解文档集合。

![](https://wipo-analytics.github.io/images/overview/Jigsaw.png)

### [Weka](http://www.cs.waikato.ac.nz/ml/weka/) 

基于Java的文本挖掘软件。

![](https://wipo-analytics.github.io/images/overview/Weka.png)

### Word Trees

词树可用于对文本（如权利要求树）进行详细调查。 前两个示例摘自[WIPO专利态势报告准备指南](http://www.wipo.int/edocs/pubdocs/en/wipo_pub_946.pdf)。

### [Google Word Trees](https://developers.google.com/chart/interactive/docs/gallery/wordtree) 

Google Developers网站上的上提供了有关使用Javascript生成词树的说明。

![](https://wipo-analytics.github.io/images/overview/Word-Trees.png)

[Jason Davies](https://www.jasondavies.com/wordtree/) 词树生成器. 

![](https://wipo-analytics.github.io/images/overview/Word-Tree-Davies.png)

### [KH Coder](http://sourceforge.net/projects/khc/?source=directory)

免费软件，可进行定量内容分析/文本挖掘。

![](https://wipo-analytics.github.io/images/overview/KHCoder.png)

###R 和  `tm` 包

R中的`tm`软件包可访问多种文本挖掘工具。 有关软件包开发的介绍，请参见[这里](http://cran.r-project.org/web/packages/tm/vignettes/tm.pdf)。 在[R-bloggers](http://www.r-bloggers.com/?s=text+mining)上，还可以使用许多非常有用的教程进行文本挖掘。 有关分步方法的信息，请参见[Graham Williams (2014) Hands-On Data Science with R Text Mining](http://onepager.togaware.com/TextMiningO.pdf)。

有关R中文本挖掘工具的最新概述，请参阅[Fridolin Wild's (2014) CRAN Task View: Natural Language Processing](http://cran.r-project.org/web/views/NaturalLanguageProcessing.html) 其中列出了各种软件包及其用途。

请注意，许多文本挖掘程序包通常将重点放在生成单词上。 对于非学术目的，这不是很有用。 专利分析通常集中在提取和分析短语（ngram）上。 因此，应该寻找可提取短语并允许对其进行深度询问的工具。

### Python 和文本挖掘

使用Python进行文本挖掘有很多资源。 请注意，就文本挖掘资源而言，Python可能远远领先于R（直到我们被证明是错误的）。 但是，请注意，Python和R越来越多地结合使用以发挥其不同的优势。 这里有一些资源可以帮助您入门。

### [The Natural Language Toolkit (NTLK)](http://www.nltk.org) 

NTLK似乎是领先的软件包，几乎可以满足所有主要需求。 随附的书籍[《使用Python进行自然语言处理》](http://shop.oreilly.com/product/9780596516499.do)也可能值得考虑。 [Python Textmining软件包](http://www.christianpeccei.com/textmining/)。 这比巨型NTLK软件包要简单，但可能适合您的需求。

![](https://wipo-analytics.github.io/images/overview/ntlk.png)

该[详细教程](http://textminingonline.com/dive-into-nltk-part-i-getting-started-with-nltk)对于希望开始使用Python的NTLK包的用户可能会有所帮助。

### 其他文本挖掘资源 

有关更多的文本挖掘工具，请参阅[20个最佳免费文本挖掘软件工具](http://www.predictiveanalyticstoday.com/top-free-software-for-text-analysis-text-mining-text-analytics/) 。

对于其他免费文本挖掘工具，请尝试一些语料库语言学网站，例如[The Linguist List](http://linguistlist.org:8888/sp/SearchWRListing-action.cfm?subclassid=7223&SearchType=LF&WRTypeID=2)，此[列表](http://www.uow.edu.au/~dlee/software.htm)(译者注: 此链接已失效, [archive上有缓存](https://web.archive.org/web/20160305120900/http://www.uow.edu.au/~dlee/software.htm) )或此[列表](http://ucrel.lancs.ac.uk/tools.html)。 请记住，这些工具中的大多数都是为语言学家而设计的，并且可能有很多工具可能很古老了。但是，即使是简单的一致性工具，例如[AntConc](http://www.laurenceanthony.net/software/antconc/) ，也可以在过滤大量文档以提取有用信息方面发挥重要作用。

某些分析工具，例如[VantagePoint from Search Technology Inc.](https://www.thevantagepoint.com) 已专门开发和改编用于处理专利数据，并提供了[vpinstitute](http://vpinstitute.org/wordpress/vp-marketplace/)。 还有许多可用于专利分析的定性数据分析软件工具，例如[MAXQDA](http://www.maxqda.com), [NVivo](http://www.qsrinternational.com/products_nvivo.aspx),  [Atlas TI](http://atlasti.com) 和 [QDA Miner](http://provalisresearch.com/products/qualitative-data-analysis-software/)。 但是，[QDA Miner Lite](http://provalisresearch.com/products/qualitative-data-analysis-software/freeware/)（仅限Windows）除外，尽管它们提供免费试用，但它们不属于我们关注的免费或开源软件类别。

