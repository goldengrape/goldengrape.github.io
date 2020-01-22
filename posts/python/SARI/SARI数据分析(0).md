<!--
.. title: SARI数据分析(0)
.. slug: SARI_data_analysis
.. date: 2020-1-22 12:00:00 UTC+08:00
.. tags: SARI
.. category: 
.. link:
.. description:
.. type: text
-->

貌似最近只有待在家里了, 看着漫天飞舞的官方消息、民间消息. 突然有个想法, 不知道是否可以根据现有的SARI数据外推一下, 看看到底疫情能够持续多久, 高峰大概何时, 以决定何时能够自由外出就餐和游玩之类. 

万事开头, 先查文献:

这一篇文献回顾了研究SARS和MERS的流行病学模型:

> Epidemic Models of Contact Tracing: Systematic Review of Transmission Studies of Severe Acute Respiratory Syndrome and Middle East Respiratory Syndrome, [全文](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6376160)

里面列出了7个模型: 

15. Peak C.M., Childs L.M., Grad Y.H., Buckee C.O. Comparing nonpharmaceutical interventions for containing emerging epidemics. Proc Natl Acad Sci U S A. 2017;114:4023–4028. [全文](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5393248/)
16. Feng Z., Yang Y., Xu D., Zhang P., McCauley M.M. Timely identification of optimal control strategies for emerging infectious diseases. J Theor Biol. 2009;259:165–171. [全文](https://sci-hub.tw/10.1016/j.jtbi.2009.03.006)
17. Klinkenberg D., Fraser C., Heesterbeek H. The effectiveness of contact tracing in emerging epidemics. PLoS One. 2006;1:e12. [全文](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1762362/)
18. Chen S.C., Chang C.F., Liao C.M. Predictive models of control strategies involved in containing indoor airborne infections. Indoor Air. 2006;16:469–481. [全文](https://sci-hub.tw/10.1111/j.1600-0668.2006.00443.x)
19. Fraser C., Riley S., Anderson R.M., Ferguson N.M. Factors that make an infectious disease outbreak controllable. Proc Natl Acad Sci U S A. 2004;101:6146–6151. [全文](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC395937/)
20. Lloyd-Smith J.O., Galvani A.P., Getz W.M. Curtailing transmission of severe acute respiratory syndrome within a community and its hospital. Proc Biol Sci. 2003;270:1979–1989. [全文](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1691475/)
21. Becker N.G., Glass K., Li Z., Aldis G.K. Controlling emerging infectious diseases like SARS. Math Biosci. 2005;193:205–221. [全文](https://sci-hub.tw/10.1016/j.mbs.2004.07.006)

研究的特点概述:

---

|作者|	Lloyd Smith et al. | Fraser et al. | Becker et al. | Chen et al. |Klinkenberg et al. | Feng et al. |Peak et al. |
|:--|:--|:--|:--|:--|:--|:--|:--|
|年份|2003|2004|2005|2006|2006|2009|2017|
|模型|基于人口的随机 SEIR 区间模型|基于 Agent 的离散时间仿真模型|基于 Agent 的分支过程与家庭层传递模型|基于人口的: 基于 Von Foerster 方程的控制模型|基于 Agent 的离散时间仿真模型|基于人口: SEIR 区域模型|基于 Agent 的 SEIR 区域分支模型|
|研究的 Co-V|SARS|SARS|SARS|SARS|SARS|SARS|MERS|
|自我报告的局限性|1. 模型中没有考虑超级扩散事件, 2. 模型中没有考虑医院中的非感染病人|由于未能通过接触追踪确定疾病发生之间的相关结构，导致接触追踪效力的过高估计|未考虑不同干预措施对感染动态的影响|模型没有考虑传播异质性，如不同的社会接触混合等|1. 模型在追踪或隔离之前只考虑传播,  2. 这种模式没有将医院和社区的环境结合起来|1. 将就诊率与诊断概率相结合,2. 被隔离的个体被假定在整个潜伏期的一半时间。| 研究重点关注疫情的早期阶段。|

---
立个Flag,

接下来我将试着研读这些文献, 重现其中的模型, 并按照新公布的数据进行参数估计和外推. 本人并非公共卫生专业, 数学也一般, 仅供自娱自乐. 完成不了, 就算了.

