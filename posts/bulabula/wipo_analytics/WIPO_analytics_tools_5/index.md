<!--
.. title: 专利分析工具概述(5)网络可视化
.. slug: WIPO_analytics_tools_5
.. date: 2019-12-07 12:05 UTC+08:00
.. tags: WIPO_analytics_tools, patent
.. category: patent
.. link:
.. description:
.. type: text
-->

## 网络可视化

网络可视化软件是用于可视化科学和技术领域中的参与者的重要工具, 尤其适用于研究参与者之间的关系。对于专利分析，它可以用于多种目的，包括：

<!-- TEASER_END -->

1. 可视化特定领域的申请人和发明人或科学研究人员的网络。 这是一个合成生物学工作的[例子](http://journals.plos.org/plosone/article?id=10.1371/journal.pone.0034368) ，该网络由有关合成生物学文章的大约2,000位作者组成。

![](https://wipo-analytics.github.io/images/overview/synbio.png)

2.使用国际专利分类(IPC)和合作专利分类（CPC）可视化技术领域及其关系。 WIPO以前的工作开创了使用大规模专利网络分析来确定[动物遗传资源专利状态](http://www.wipo.int/patentscope/en/programs/patent_landscapes/reports/animal_gr.html)。

下图显示了数十万份专利文件的合作专利分类号(CPC)和国际专利分类号(IPC)的网络地图，其中包含对多种农场动物（牛，猪，绵羊等）的引用。 节点是描述技术领域的CPC / IPC分类号。 群集显示紧密链接的文档，这些文档共享相同的分类号，可以称为“模块”或群集。 关于动物遗传资源状态报告的作者使用该网络作为探索性工具来提取和检查群集中相关性的文件。丢弃了诸如烹饪设备和畜牧业（动物房屋等）之类的群集。 作者后来使用网络映射来探索和分类各个群集。

![](https://wipo-analytics.github.io/images/overview/animals.png)

3.可视化专利文档中的关键术语网络以及它们与其他术语的关系，作为探索和完善分析的一部分。 在这种情况下，作者使用词干将相似的术语彼此聚类，以了解上述与动物育种有关的动物新品种的内容。

![](https://wipo-analytics.github.io/images/overview/breeds_cluster.png)

这样，网络可视化既可以被视为用于定义关注对象的探索工具，也可以作为最终结果展示（例如，在特定区域中定义的参与者网络）。

### [Gephi](https://gephi.github.io)

Gephi是基于Java的开源网络生成软件。 它可以处理大型数据集（能到多大取决于您的计算机）以产生强大的可视化效果。

![](https://wipo-analytics.github.io/images/overview/Gephi.png)

可能会遇到的一个问题是如何安装正确的Java版本的问题, 特别对是Mac用户。 但0.9版以上似乎已解决了此问题。

要在R中创建 `.gexf` 网络文件，请尝试[gexf](http://cran.r-project.org/web/packages/rgexf/index.html) 程序包, 其示例代码和源代码在[此处](https://bitbucket.org/gvegayon/rgexf/wiki/Home)。 在Python中，尝试使用[pygexf](https://github.com/paulgirard/pygexf)库，有关Java，Javascript C ++和Perl等其他任何内容，请参见[gexf/format/](https://gephi.org/gexf/format/)。

### [NodeXL](https://www.smrfoundation.org/nodexl/)

对于那些Excel的死忠用户来说，[NodeXL](https://www.smrfoundation.org/nodexl/) 是一个可以用来可视化网络的插件。 它工作得不错。(译者注: 据维基百科记载, NodeXL分成了免费版和收费版两种, 原代码网站被杀毒软件警告, 本文已经替换成新的链接)

![](https://wipo-analytics.github.io/images/overview/NodeXL.png)

### [Cytoscape](http://www.cytoscape.org/what_is_cytoscape.html) 

[Cytoscape](http://www.cytoscape.org/what_is_cytoscape.html)是另一个网络可视化程序。 它最初是为生物网络和相互作用的可视化而设计的，但与许多其他生物信息学工具一样，它可以应用于更广泛的可视化任务。

![](https://wipo-analytics.github.io/images/overview/cytoscape.png)

我们主要有使用Gephi的经验，但是Cytoscape值得一试。 Cytoscape可在Windows，Mac和Linux上使用。

### [Pajek](http://mrvar.fdv.uni-lj.si/pajek/)

这是最古老，最成熟的免费网络工具之一，并且仅Windows（或通过虚拟机运行）。 它广泛用于文献计量学，可以处理大型数据集。 这是个人喜好问题，但是Gephi之类的工具可能会取代Pajek，因为它们更灵活。 但是，Pajek可能在精度，可重现性的便利性, 以及轻松保存等方面具有重要优势, Gephi作为Beta版程序可能在上述方面有所欠缺。

![](https://wipo-analytics.github.io/images/overview/Pajek.png)

对于喜欢Gephi外观的用户，也可以将数据从Pajek导出到Gephi。

###[VOS Viewer](http://www.vosviewer.com/Home)

来自莱顿大学的VOS Viewer与Gephi和Cytoscape相似，但也呈现不同类型的景观（与纯网络节点和边缘视觉效果相反）。 最新版本还可以与Gephi和Cytoscape对话。 值得测试不同的视觉显示选项, 以及处理Web of Science和Scopus书目数据的能力。

![](https://wipo-analytics.github.io/images/overview/VOSviewer.png)

###[Hive Plots](http://www.hiveplot.net)

我们并不完全确定Hive Plot的构成。 但是，我们对目标很同情。 网络可视化的目的应该是弄清复杂性……而不是“哇，看，我做了类似意大利面条的东西”（尽管通常是过程的一部分）。 因此，我们发现由BC Cancer Agency基因组科学中心的Martin Krzywinski开发的Hive Plots很有趣。
(译者注: 我也不知道原文到底想表达啥)

![](https://wipo-analytics.github.io/images/overview/HivePlots.png)

专为大型网络设计，用于Hive绘图的软件包[pyveplot](https://pypi.python.org/pypi/pyveplot/) 和 [hiveplot](https://github.com/ericmjl/hiveplot)。 对于R，有 HiveR ，CRAN上的文档在[此处](http://cran.r-project.org/web/packages/HiveR/index.html)。

在结束对网络映射工具的讨论时，还必须注意，网络可视化需要导出为图像。 这意味着还需要图像处理软件。 诸如[GNU图像处理程序或GIMP](http://www.gimp.org) 之类的开源工具非常适合并且易于使用。 在使用标签的地方，应特别注意小心文本，以确保在不同计算机上显示的一致性。这类的任务可以在诸如GIMP之类的工具中执行。

有关网络可视化的其他来源，请参见[FlowingData](http://opendata-tools.org/en/visualization/)。 也可以尝试[Visual Complexity](http://www.visualcomplexity.com/vc/) (译者注: 中国大陆访问似乎有困难, 不知为何)和[visualising data](http://www.visualisingdata.com/index.php/resources/) 作为灵感来源。

