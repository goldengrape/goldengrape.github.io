<!--
.. title: 专利分析工具概述(7)地理信息制图
.. slug: WIPO_analytics_tools_7
.. date: 2019-12-07 12:07 UTC+08:00
.. tags: WIPO_analytics_tools, patent
.. category: patent
.. link:
.. description:
.. type: text
-->

## 地理信息制图

除了无所不在的[Google地图](https://www.google.com/maps/) 或众所周知的[Google 地球](https://www.google.co.uk/intl/en_uk/earth/) 我们认为值得仔细研究其他服务。
<!-- TEASER_END -->

### [OpenStreetMap](http://www.openstreetmap.org/#map=5/51.500/-0.100)

正当流行. 

![](https://wipo-analytics.github.io/images/overview/OpenStreetMap.png)

### [Leaflet](http://leafletjs.com)

一个非常流行的用于交互式地图的开源JavaScript库

![](https://wipo-analytics.github.io/images/overview/Leaflet.png) 

可通过API访问。 R用户可以使用`leafletr`软件包, 并通过[R-bloggers](http://www.r-bloggers.com/?s=leaflet)上的教程进行练习。 对于Python用户，请在[此处](https://github.com/python-visualization/folium)或[此处](https://pypi.python.org/pypi/folium) 尝试`folium` 

### [Tableau Public](https://public.tableau.com/s/)

上面已经提到过。 Tableau Public使用“开放式街道地图”来创建交互式图形的强大组合，这些图形可以链接到以各种细节级别进行地理编码的地图。 请参见[有关合成生物学的科学文献示例](https://public.tableau.com/profile/poldham#!/vizhome/SyntheticBiologyScientificLandscape/SyntheticBiologyTrends) 。

Tableau Public可能是开始使用专利数据创建地图的最简单方法。 下面的地图是使用自定义地理编码制作的，并将数据连接到出版国和科学出版物的标题。

![](https://wipo-analytics.github.io/images/overview/tableaumap.png)

要查看交互式版本，请尝试此[页面](http://public.tableau.com/profile/poldham#!/vizhome/SyntheticBiologyScientificLandscape/SyntheticBiologyTrends)。 在Tableau Public中可以轻松创建简单而有效的地图。

### [QGIS](http://www.qgis.org/en/site/)

在所有主要平台上可运行的非常流行且复杂的软件包。

![](https://wipo-analytics.github.io/images/overview/QGIS.png)

使用QGIS，Oldham和Hall等人参考了深海位置（如热液喷口），绘制了海洋科学研究和专利文件的全球地理位置（请参阅[Valuing the Deep](https://www.researchgate.net/publication/273139809_Valuing_the_Deep_Marine_Genetic_Resources_in_Areas_Beyond_National_Jurisdiction))。 这是基于科学文献的文本挖掘得出的，海洋中科学研究位置的低分辨率QGIS地图。

![](https://wipo-analytics.github.io/images/overview/valuing1.png)

### [Geonames.org](http://www.geonames.org). 

geonames不是一个地图程序，而是一个非常有用的数据库，它包含来自世界各地的地理参考地名以及RESTful [web服务](http://www.geonames.org/export/web-services.html)。 如果您需要获取大量地点的地理参考数据，那么这应该是您的第一站。 在R中可以使用[`geonames`](https://cran.r-project.org/web/packages/geonames/geonames.pdf)访问地理名称, 在Python，Ruby，PHP等中也可以。

![](https://wipo-analytics.github.io/images/overview/GeoNames.png)

### [iCharts](http://icharts.net/product/web-data-visualization)

免费和高级数据可视化服务：

![](https://wipo-analytics.github.io/images/overview/icharts.png)

### [OpenLayers3](http://openlayers.org)

OpenLayers3允许您将自己的图层添加到OpenStreetMap和其他数据源，如果您要创建自己的图层，则可能会非常有用。 它还有API和教程。

![](https://wipo-analytics.github.io/images/overview/OpenLayer.png)

### [CartoDB](https://cartodb.com/gallery/)

免费和付费帐户，带有精美的示例库. 

![](https://wipo-analytics.github.io/images/overview/CartoDB.png)

### [d3.js](http://d3js.org)

一个用于处理数据和文档的javascript库。 这是Web上其他一些经常提到的可视化工具背后的库。

![](https://wipo-analytics.github.io/images/overview/D3.png)

### [Highcharts](http://www.highcharts.com)

非商业用途免费, 也有各种付费plan。

![](https://wipo-analytics.github.io/images/overview/highcharts.png)

### [Datawrapper](https://datawrapper.de)

完全开源的服务，用于使用数据创建图表和地图。 大型报纸广泛使用，因此图形看起来很熟悉。 您可以在[此处](https://github.com/datawrapper/datawrapper)中创建一个帐户或从Github fork。 有免费选项和付费选项。

![](https://wipo-analytics.github.io/images/overview/Datawrapper.png)

###[Plotly](https://plot.ly/feed/)

Plotly是免费的，并且具有用于R，Python和Matlab等客户端的API，是一种越来越受欢迎的免费服务，它使用上述D3.js库以及企业版。 Plotly越来越受欢迎，并且具有适用于Python，Matlab，R，Node.js和Excel的一系列API客户端。 Plotly的易用性以及从各种环境中访问的便利性是其不断增长的成功的主要原因。

![](https://wipo-analytics.github.io/images/overview/Plotly.png)

