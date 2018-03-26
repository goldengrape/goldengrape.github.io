
# coding: utf-8

# 快要被Pandas搞疯了. 各种奇技淫巧太多, 
# 
# 我觉得pandas, 或者说python的”大数据"处理技巧两种: 
# 
#     a0. 确定你需要的数据文件是什么名字
#     a1. 去stackoverflow搜数据文件名字看看教程. 
#     a2. 如果不能满足自己的要求, 提个问题, 然后等一周. 
# 
# 或者: 
# 
#     b0. 自己查文档埋头苦干一周
# 
# 通常前者的解决方案效果优于后者, 而且代码更为优雅易读. 
# 
# 例如: 
# 
# 你发现自己研究的数据来自 City_Zhvi_AllHomes.csv (From the [Zillow research data site](http://www.zillow.com/research/data/) there is housing data for the United States. In particular the datafile for [all homes at a city level](http://files.zillowstatic.com/research/public/City/City_Zhvi_AllHomes.csv), ```City_Zhvi_AllHomes.csv```, has median home sale prices at a fine grained level.)
# 
# 那么, 只需要在StackOverFlow上[搜索City_Zhvi_AllHomes.csv](https://stackoverflow.com/search?q=City_Zhvi_AllHomes.csv) 即可. 
# 
# <!-- TEASER_END -->
# 

# # 但我还是喜欢有理有据的解决
# 
# 作业题中是美国各个城市的房价, 城市分两类, 一类是有大学的, 一类是没大学的, 那么看看这两类城市房价的区别, 
# 
# 可以取得的数据集是各个城市的房价, 是一个DataFrame, 还有一个是大学城名称的DataFrame. 但这两个DataFrame都是MultiIndex的, index中包含州的名字和城市的名字. 
# 
# 所以问题就是对于MultiIndex的两个DataFrame, 如何取得交集和补集. 注意数据的Index有关系, 但数据内容可不一定有关系. coursera上讨论区中[高票支持的回答](https://www.coursera.org/learn/python-data-analysis/discussions/weeks/4/threads/n6epwLCKEeewNAofllqCYg)里各种奇技淫巧, 各种奇技淫巧. 而且你如果用他的方法, 在不同的python/pandas版本貌似出来的结果是不同的. 
# 
# 不调用原始题目了, 用一个简化模型来说明. 

# ## 建立两个MultiIndex的DataFrame
# 
# 分别是s1和s2, 一会儿求他们的交集和差集. 
# 
# S1:
# 
# |first | second |       |
# |----|----|----|
# |bar |   one|       0.502489|
# |    | two|       1.061737|
# |baz   | one|      -0.207277|
# |       |two|       2.042837|
# |foo    |one|      -0.792736|
# |       |two|      -0.204785|
# |qux    |one|       1.596757|
# |       |two|      -0.585016|
# 
# S2: 
# 
# |first | second |       |
# |----|----|----|
# |bar   | one   |    0.553635|
# |foo   | two    |   1.049258|
# |cool  | three   | -1.059016|
# 

# In[3]:


import pandas as pd
import numpy as np
arrays1 = [['bar', 'bar', 'baz', 'baz', 'foo', 'foo', 'qux', 'qux'],
          ['one', 'two', 'one', 'two', 'one', 'two', 'one', 'two']]
tuples1 = list(zip(*arrays1))
index1 = pd.MultiIndex.from_tuples(tuples1, names=['first', 'second'])
s1 = pd.Series(np.random.randn(len(tuples1)), index=index1)
s1


# In[5]:


arrays2 = [['bar', 'foo', "cool"],
          ['one', 'two', "three"]]
tuples2 = list(zip(*arrays2))
index1 = pd.MultiIndex.from_tuples(tuples2, names=['first', 'second'])
s2 = pd.Series(np.random.randn(len(tuples2)), index=index1)
s2


# 现在要求解:
# s1, s2中index的交集, 差集. 
# 
# 可以参考[Python For Data Analysis ](https://pda.readthedocs.io/en/latest/chp5.html)
# ![](https://pda.readthedocs.io/en/latest/_static/cover.jpg)
# 
# 索引方法和属性
# * append	链接额外的索引对象，产生一个新的索引
# * diff	计算索引的差集
# * intersection	计算交集
# * union	计算并集
# * isin	计算出一个布尔数组表示每一个值是否包含在所传递的集合里
# * delete	计算删除位置i的元素的索引
# * drop	计算删除所传递的值后的索引
# * insert	计算在位置i插入元素后的索引
# * is_monotonic	返回True，如果每一个元素都比它前面的元素大或相等
# * is_unique	返回True，如果索引没有重复的值
# * unique	计算索引的唯一值数组
# 
# 当然, 如果你完全相信他, 那就上当了. 我反复说过, 开源社区有一定的**反社会倾向**, 不能不信, 也不能全信. 比如我想用的最重要的这个差集的计算方法, 如果用diff就报错了. 要用difference.
# 
# 要回到pandas的文档中找证据: [pandas.Index.difference](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.Index.difference.html)

# In[7]:


idx1 = pd.Index([1, 2, 3, 4])
idx2 = pd.Index([3, 4, 5, 6])
idx1.difference(idx2)


# 如果你想把MultiIndex的例子简单代入
# ```python
# s1.difference(s2)
# ```
# 那么又错了. 反社会倾向, 注意. 
# 
# Pandas文档中的例子里idx1和idx不是DataFrame, 而是index. 被反社会以后, 我还得承认是自己看错了. 
# 
# 所以: 

# In[16]:


s1.index.difference(s2.index)


# 求解两个集合的交集: 

# In[17]:


s1.loc[s1.index.intersection(s2.index)]


# 从集合s1中扣除s2, 剩下的差集

# In[18]:


s1.loc[s1.index.difference(s2.index)]

