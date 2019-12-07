<!--
.. title: 专利分析工具概述(2)数据清洗工具
.. slug: WIPO_analytics_tools_2
.. date: 2019-12-07 12:02 UTC+08:00
.. tags: WIPO_analytics_tools, patent
.. category: patent
.. link:
.. description:
.. type: text
-->

## 数据清洗工具

###[Open Refine](http://openrefine.org) (以前叫Google Refine)

数据分析和可视化的基本规则是：“垃圾进=垃圾出”。 如果您的数据最初没有经过清洗，那么分析或可视化的结果很垃圾也不要感到惊讶。
<!-- TEASER_END -->

用[Open Refine](http://openrefine.org)（以前称为Google Refine）清洗专利数据的详细使用信息，请参见[这里](http://poldham.github.io/openrefine-patent-cleaning/) 。 对于专利分析，Open Refine是清理申请人和发明人姓名的重要免费工具。

![](https://wipo-analytics.github.io/images/openrefine/OpenRefine-download.png) 

许多平台都提供数据清理功能，并且可以在Open Office或Excel中进行很多基本清理。但Open Refine是清洗专利中姓名字段的最便捷工具。 特别是，它对于拆分和清洗成千上万的专利申请人和发明人姓名非常有用。

(译者注, 申请人名称还算可控, 数据清洗很多平台可以直接提供. 但发明人的姓名千差万别, 如果涉及多个语种则很麻烦, Open Refine是很好的工具)

(译者的怨念: 
例如 ROFFMAN H JEFFREY, 有可能写成 ROFFMAN JEFFREY H; ROFFMANN J.H.; ROFFMAN J.; JIEFURII Eichi Rofuman; 洛夫曼; 罗夫曼; 骆杰夫. 尤其是台湾智慧財產局的译名“**`骆杰夫`**”, 同时包含了 Roffman 和 Jeffrey 中的音节. 智慧財產局的同学你们怎么想的??)