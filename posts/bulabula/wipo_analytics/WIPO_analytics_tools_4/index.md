<!--
.. title: 专利分析工具概述(4) 数据可视化
.. slug: WIPO_analytics_tools_4
.. date: 2019-12-07 12:04 UTC+08:00
.. tags: WIPO_analytics_tools, patent
.. category: patent
.. link:
.. description:
.. type: text
-->

## 数据可视化

如果您不熟悉数据可视化，建议您看看耶鲁大学的Edward Tufte的著名著作[《定量信息的视觉展示》](http://en.wikipedia.org/wiki/Edward_Tufte) 。 他[对Powerpoint的使用和滥用的批评](https://www.inf.ed.ac.uk/teaching/courses/pi/2016_2017/phil/tufte-powerpoint.pdf) 很有趣而且很有见地。 Stephen Few的作品也很受欢迎，例如[Show Me the Numbers：Designing Tables and Graps to Enlighten](http://www.analyticspress.com/smtn.php)。

<!-- TEASER_END -->

请记住，数据可视化首先是与观众的交流。这涉及到如何交流以及选择清晰交流方式。在很多情况下，专利分析和可视化的结果将是报告和演示。演讲者应阅读Tufte对[powerpoint演示文稿](https://www.inf.ed.ac.uk/teaching/courses/pi/2016_2017/phil/tufte-powerpoint.pdf)的评论。您可能还想看看Nancy Duarte的[Resonate](http://resonate.duarte.com/#!page0)，以获得有关完善演示和讲故事的想法。该风格可能不适合所有人，但[Resonate](http://resonate.duarte.com/#!page0)包含非常有用的信息和见解。离线资源中, 可以将Katy Borner的[《科学地图集：可视化我们所知道的内容》](https://mitpress.mit.edu/books/atlas-science) 这本书作为可视化科学活动历史的绝佳指南，其中还包括专利活动发展史的可视化。请记住，有效的可视化需要实践。

如果您是数据可视化的新手，请访问[Tableau Public](https://public.tableau.com/s/gallery) 和[我们的介绍章节](http://poldham.github.io/tableau-patents/), 它是个不需要任何编程知识的好地方。 此列表中的其他一些工具类似于Tableau Public（部分是因为Tableau是市场领导者)。我们还将在本节的最后提供一些可视化概述网站的指示，在这些网站上，你可以找到关于数据可视化的新鲜和有趣的东西。

###[Google Charts](https://developers.google.com/chart/interactive/docs/gallery)

- 创建一个Google帐户以访问Google Spreadsheets和其他Google程序
- 查看[Google Charts图册](https://developers.google.com/chart/interactive/docs/gallery)和[API](https://developers.google.com/chart/interactive/docs/reference)
- 有关在R中使用Google Charts的概述，请参阅[此处](http://cran.r-project.org/web/packages/googleVis/vignettes/googleVis.pdf)的 `GoogleVis` 软件包及其示例。
- 有关通过Python使用Google图表的概述，请参见[google-chartwrapper](https://code.google.com/p/google-chartwrapper/) 或者 [Python Google Charts](http://python-google-charts.readthedocs.org/en/latest/#)

![](https://wipo-analytics.github.io/images/overview/google_sheets_addon.png)

###[Tableau Public](https://public.tableau.com/s/)

[这里](http://poldham.github.io/tableau-patents/) 提供了有关使用Tableau Public进行专利分析和可视化入门的深入讲解。 您的专利数据清洗后，Tableau Public是一种强大的工具，可以用您的数据开发交互式仪表板和地图，并将其与其他数据源组合。请记住，根据定义，Tableau Public数据是公共数据，不应与敏感数据一起使用。

![](https://wipo-analytics.github.io/images/tableau/dashboard_completed.png)

该工作簿可以[在线查看](https://public.tableau.com/profile/wipo.open.source.patent.analytics.manual#!/).

### R 和 RStudio

R是一种统计编程语言，用于处理各种不同类型的数据。 它还具有功能强大的可视化工具，包括提供与Google Charts，[Plotly](https://plot.ly)等接口的`packages`。 如果您对使用R感兴趣，我们建议您使用RStudio，可以在[此处](http://www.rstudio.com/) 下载。 整个《 WIPO开源专利分析手册》是使用Rmarkdown在RStudio中编写的，用于输出Web，.pdf和演示文稿的文章。 如此暗示，R不只是关于数据可视化。 要开始使用R和RStudio，请尝试[DataCamp](https://www.datacamp.com/) 上的免费教程。 我们将在其他章节和在线文章中更详细地介绍R。

受到[Leland Wilkinson作品](https://en.wikipedia.org/wiki/Leland_Wilkinson)的启发，作为“图形语法”方法的一部分，RStudio和其他开发人员创建了可提供非常有用方法的软件包 可视化和映射数据。 下面的链接将带您进入一些最受欢迎的数据可视化软件包的文档。

1. [ggplot2](http://cran.r-project.org/web/packages/ggplot2/index.html)
2. [ggvis](http://cran.r-project.org/web/packages/ggvis/index.html)
3. [ggmap](http://cran.r-project.org/web/packages/ggmap/index.html)
4. [googleVis](http://cran.r-project.org/web/packages/googleVis/index.html)

在以后的章节中，我们将更深入地介绍`ggplot2` 和 `ggvis`。 在此之前，请先参阅R-Bloggers上[ggplot2的章节](http://www.r-bloggers.com/search/ggplot2)，和 [ggvis的章节](http://www.r-bloggers.com/?s=ggvis)。 Datacamp提供了有关使用ggvis的免费教程，可以在[此处](http://www.r-bloggers.com/ggvis-tutorial-become-a-data-visualization-expert-with-rstudio/ ) 访问。 有关某些顶级R包的更广泛概述，请参见Qin Wenfeng最近的[awesome R列表](https://github.com/qinwf/awesome-R). 

### Shiny

[RStudio](http://www.rstudio.com/ )的Shiny是R的Web应用程序框架。这意味着您可以从R输出表和可视数据，例如将上述工具中的表和可视化数据输出到网络上。

![](https://wipo-analytics.github.io/images/overview/Shiny.png)

R用户的[Shiny apps](http://shiny.rstudio.com) 允许创建在线交互式应用程序（最多5个免费）。 有关示例，请参见[图库](http://shiny.rstudio.com/gallery/)。 有关更多示例和教程，请参见[RBloggers](http://www.r-bloggers.com/search/shiny) 。 

[Radiant](http://vnijs.github.io/radiant/index.html)是R中基于浏览器的商业分析平台。它基于Shiny，但专门针对商业分析。

![](https://wipo-analytics.github.io/images/overview/Radiant.png)

有关Radiant的一系列入门视频，请参见[这里](http://vnijs.github.io/radiant/tutorials.html)。

###[IBM Many Eyes](http://www-01.ibm.com/software/analytics/many-eyes/)

您需要注册一个免费帐户才能真正了解其含义，请尝试[此页面](http://www-969.ibm.com/software/analytics/manyeyes/) ，然后选择右上角的注册。

![](https://wipo-analytics.github.io/images/overview/manyeyes.png)

### 其他可视化工具

- [Tulip](http://tulip.labri.fr/TulipDrupal/): C ++中的数据可视化框架

- [SigmaJS](http://sigmajs.org/): 专门用于图形绘制的JavaScript库。 它允许创建交互式静态和动态图. 
- [Kendo UI](http://www.telerik.com/download/kendo-ui-web-open-source): 创建用于响应式可视化的小部件。 
- [Timeline](http://timeline.knightlab.com/): KnightLab（西北大学）是一种允许创建交互式时间线的工具，并提供40种语言的版本。  
- [Miso Project](http://misoproject.com/): 开源工具包，有助于创建交互式叙事和数据可视化(译者注: 原网站域名已经待售了, 但是仍然可以在github上找到[代码包和遗迹](https://github.com/misoproject/))
- [Sci2](https://sci2.cns.iu.edu/user/index.php): 学习科学的工具集。
- [Simile Widgets](http://www.simile-widgets.org) 从MIT的SIMILE项目衍生出来的用于叙事的Web小部件。 
- [jqPlot](http://www.jqplot.com). 一个基于jQuery的开源绘图插件。
- dipity用于时间线（免费和高级服务）(译者注: dipity似乎已经关闭了, 参考[这篇文章](https://dropinblog.com/blog/what-happened-to-dipity-com/))

其他更多数据可视化工具和启发, 请参考[visualizing.org](http://www.visualizing.org/) 和 [Open Data Tools](http://opendata-tools.org/en/visualization/)

