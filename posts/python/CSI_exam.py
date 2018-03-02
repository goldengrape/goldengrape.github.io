
# coding: utf-8

# 2018年刑侦推理试题: 
# ![question.jpeg](https://i.loli.net/2018/03/01/5a982103b9db2.jpeg)
# <!-- TEASER_END -->

# # 解题思路
# 
# 以此题为例, 做一个简单的python小教程. 
# 
# ## 提取"第x题的答案"
# 首先, 观察题目中经常出现的说法是: "第x题的答案"怎样怎样, 那么常用的一个过程就是要提取第x题的答案
# 
# 在python中可以使用的一个数据结构叫做列表list, 列表使用方括号括起来的一些元素, 要提取其中的内容用列表名[序号]就可以提取了. 比如

# In[1]:


sample=[0.1, 1.2, 2.3, 3.4, 4.5] # "#"号后面的部分是注释, 不会进入计算, 我后面会在程序中使用注释说明
sample[2] # 注意python的计数是从第0项开始的, 所以第2项是2.3而不是1.2


# 如果用数字0, 1, 2, 3来表示ABCD的话, 就可以把所有的答案放进一个列表里, 提取某一题的答案就是提取列表中的第几项, 注意python的列表是从第0项开始计数的, 为了读题中不引起混淆, 我将列表的第0项设定成空项. 

# In[2]:


# 举例, 假设第1题到第5题的答案分别是AABDC, 用0, 1, 2, 3来表示ABCD
sample_answer=[_, 0, 0, 1, 3, 2]
# 提取第3题的答案
sample_answer[3]


# ## 第1题
# 这道题的答案是: A.A, B.B, C.C, D.C
# 
# 题目中没有给出限定, 所以暂时先不管它

# ## 第2题
# 第5题的答案是: A.C, B.D, C.A, D.B
# 
# 在第2题里, 如何描述A->C,B->D, C->A, D->B的映射关系呢? 可以用一个python一个数据结构叫做字典. 
# 字典是用{ }括起来的一组元素, 每一个元素里有一个key:value的数据对, 表示从key到value的映射
# 
# 那么要表示如何描述A->C,B->D, C->A, D->B的映射关系, 可以建立一个字典: 

# In[3]:


a2_dict={0:2,# A.C
         1:3,# B.D
         2:0,# C.A
         3:2}# D.B
a2_dict[1] # 字典内容的提取, 是使用字典名[key],就可以提取出value


# 用0, 1, 2, 3代表ABCD
# * 如果第二题选A, 那么就是说第5题的答案是C, 也就是a2_dict[0]的值2
# * 如果第二题选B, 那么就是说第5题的答案是D, 也就是a2_dict[1]的值3
# * 如果第二题选C, 那么就是说第5题的答案是A, 也就是a2_dict[2]的值0
# * 如果第二题选D, 那么就是说第5题的答案是B, 也就是a2_dict[3]的值2
# 
# 假定我们已经知道了所有的答案, 放在answer这个列表里, 那么第2题的答案是answer[2], 第5题的答案是answer[5], 
# 
# 那么第2题的答案所对应的值就是a2_dict[ answer[2] ], 判断第2题是不是做对了, 就要看
# ```python
# a2_dict[ answer[2] ]==answer[5]
# ```
# 是真还是假
# 
# 我将这个判断过程写成一个"函数", 这个函数负责看第2题是否做对了. python的函数定义是用
# ```python
# def 函数名(参数表): 
#     空4格写函数内容
#     return 返回结果
# ```

# In[4]:


def test2(answer):
    a2_dict={0:2,# A.C
             1:3,# B.D
             2:0,# C.A
             3:2}# D.B

    return a2_dict[ answer[2] ]==answer[5]


# In[5]:


# 一般写好一个函数, 应当测试一下是否写对了. 
print(test2([_,1,2,3,4,5])) # 应当为假
print(test2([_,1,0,3,4,2])) # 应当为真, 假定第2题的答案是0, 对应第5题的答案是2


# ## 第3题
# 以下选项中哪一题的答案与其他三项不同:
# A. 第3题, B. 第6题, C. 第2题, D. 第4题
# 
# 当然我们可以去一个一个比对, 但python中对列表有一个简单的判断命令叫in,如果元素在这个列表中, 那么in命令就返回真, 否则为假. 
# 
# 如果把第3题, 第6题, 第2题, 第4题的答案放在一个列表中, 那么有
# ```python
# a3_list=[ answer[3], answer[6], answer[2], answer[4] ]
# ```
# 
# * 如果选A, 那么就看answer[3] in [            answer[6], answer[2], answer[4] ]是否为假
# * 如果选B, 那么就看answer[6] in [ answer[3],            answer[2], answer[4] ]是否为假
# * 如果选C, 那么就看answer[2] in [ answer[3], answer[6],            answer[4] ]是否为假
# * 如果选D, 那么就看answer[4] in [ answer[3], answer[6], answer[2]            ]是否为假
# 
# 为了产生一个没有某一项的列表, 我们可以将列表中的某一项pop出去, 剩下的a3_list. 所以: 
# 

# In[6]:


def test3(answer):
    a3_list=[answer[3], answer[6], answer[2], answer[4]]
    # 先提取出来要检查的项
    refer=a3_list[ answer[3] ]
    # 在把这一项从列表里pop掉
    a3_list.pop( answer[3] )
    
    # 看看要检查的项是否在剩下的列表中
    return not(refer in a3_list )


# In[7]:


print(test3([_,1,2,3,4,5,6])) # 应当是真
print(test3([_,1,0,0,0,5,0])) # 应当是假


# ## 第4题
# 
# 以下选项中哪两题的答案相同: 
# 
# * A. 第1,5题 
# * B. 第2,7题
# * C. 第1,9题
# * D. 第6,10题
# 
# 这道题其实和第2题的思路一样, 建立一个映射关系的字典, 
# ```python
#     a4_dict={0:[1,5],
#              1:[2,7],
#              2:[1,9],
#              3:[6,10]}
#           ```
# 然后验证题目中所说的东西即可. 
# * 如果选A, 那么看a4_dict[0]中的两项[1, 5], 
#    * 其中1是a4_dict[0]这个列表的第0项, 第1题的答案就是```answer[ a4_dict[0][0] ]``` , 
#    * 其中5是a4_dict[0]这个列表的第1项, 第5题的答案就是```answer[ a4_dict[0][1] ]```
# * 如果选B, 那么看a4_dict[1]中的两项[2, 7], 
#    * 其中2是a4_dict[0]这个列表的第0项, 第2题的答案就是```answer[ a4_dict[0][0] ]``` , 
#    * 其中7是a4_dict[0]这个列表的第1项, 第7题的答案就是```answer[ a4_dict[0][1] ]```

# In[8]:


def test4(answer):
    a4_dict={0:[1,5],
             1:[2,7],
             2:[1,9],
             3:[6,10]}
    
    return answer[ a4_dict[ answer[4] ][0]] == answer[ a4_dict[ answer[4] ][1]]


# In[9]:


print( test4([_,1,2,3,0,5,6,7]) ) # 应当为假
print( test4([_,1,2,3,0,1,6,7]) ) # 应当为真


# ## 第5题
# 以下选项中哪一题的答案与本题相同
# * A. 第8题,
# * B. 第4题,
# * C. 第9题,
# * D. 第7题
# 
# 想必已经越来越熟练了, 先建立一个映射关系字典: 
# ```
#     a5_dict={0:8,
#              1:4,
#              2:9,
#              3:7}
#              ```
# 本题的答案当然就是answer[5], 
# * 如果选A, 那么就是看第8题的答案, 也就是answer[ a5_dict[0] ]
# * 如果选B, 那么就是看第4题的答案, 也就是answer[ a5_dict[1] ]

# In[10]:


def test5(answer):
    a5_dict={0:8,
             1:4,
             2:9,
             3:7}
    return answer[5] == answer[ a5_dict[ answer[5] ] ]


# In[11]:


print(test5([_,1,2,3,4,0,6,7,0])) # 应当为真, 第5题的答案与第8题都是A
print(test5([_,1,2,3,4,1,6,7,0])) # 应当为假, 第5题的答案选的是B, 但与第4题的答案不同


# ## 第6题
# 以下选项中哪两题的答案与第8题相同
# * A. 第[2,4]题,
# * B. 第[1,6]题,
# * C. 第[3,10]题,
# * D. 第[5,9]题. 
# 
# 出题人已经开始重复自己了, 这道题和第4题区别不大. 
# 
# 建立一个映射字典: 
# ```
#     a6_dict={0:[2,4],
#              1:[1,6],
#              2:[3,10],
#              3:[5,9]}
#              ```
#              
# 第8题的答案当然是answer[8],
# * 如果选A, 那么answer[8]应当等于a6_dict[0]中的第2, 4题的答案, 
#     * 其中2是```a6_dict[0][0]```, 第2题的答案也就是``` answer[a6_dict[0][0]]```
#     * 其中4是```a6_dict[0][1]```, 第4题的答案也就是``` answer[a6_dict[0][1]]```

# In[12]:


def test6(answer):
    a6_dict={0:[2,4],
             1:[1,6],
             2:[3,10],
             3:[5,9]}
    return (answer[8] == answer[a6_dict[ answer[6] ][0]] == answer[a6_dict[ answer[6] ][1]] )


# In[13]:


print(test6([_,1,0,3,0,5,0,7,0])) # 应当为真, 第6题选了A, 第8题的答案是A, 第2, 4题也选的是A
print(test6([_,1,0,3,0,5,1,7,2])) # 应当为假, 第6题选了B, 第8题的答案是C, 第1, 6题选的不是C


# ## 第7题
# 此十道题中, 被选中次数最少的选项字母为: 
# * A. C,
# * B. B, 
# * C. A, 
# * D. D
# 
# 先建立个映射字典: 
# ```
#     a7_dict={0:2,
#              1:1,
#              2:0,
#              3:3}
#              ```
# 这道题开始有新花样了, "选中次数最少的字母", 那就要统计一下每个字母都被选中了多少次啊. 
# 
# 列表里有个.count(value)方法, 可以统计出value在列表中出现了多少次. 所以: 
# * 字母A在答案中出现的次数=answer.count(0)
# * 字母B在答案中出现的次数=answer.count(1)
# * 字母C在答案中出现的次数=answer.count(2)
# * 字母D在答案中出现的次数=answer.count(3)
# 
# 最少, 可以用min(列表)来表示, 那么各个字母出现次数中最少的数量: 
# min( [answer.count(0),answer.count(1),answer.count(2),answer.count(3) ] )

# In[14]:


def test7(answer):
    a7_dict={0:2,
             1:1,
             2:0,
             3:3}
    return answer.count(a7_dict[answer[7]]) == min( [answer.count(0),answer.count(1),answer.count(2),answer.count(3) ] )


# In[15]:


print(test7(["",1,2,3,4,5,6,0,8,9,10])) # 应当为真, 这里面所有的字母都只出现了1次
print(test7(["",1,2,3,4,5,6,1,8,9,10])) # 应当为假, 1出现了两次, 比其他都多


# ## 第8题
# 以下选项中, 哪一题的答案与第1题的答案在字母中不相邻: 
# * A. 第7题, 
# * B. 第5题, 
# * C. 第2题, 
# * D. 第10题
# 
# 先建个映射关系: 
# ``` 
# a8_dict={0:7,1:5,2:2,3:10}
# ```
# 
# 这道题说的是字母不相邻, 我们已经用数字0123表示字母ABCD了, 那么相邻, 就是相差为+-1喽, 或者是减完以后平方=1. python用```**```表示平方, 用```!=```来表示不等于
# 
# 第一题的答案是answer[1], 
# * 如果选A, 那么有```(answer[1]-answer[7])**2 !=1 ```
# * 如果选B, 那么有```(answer[1]-answer[5])**2 !=1 ```

# In[16]:


def test8(answer): 
    a8_dict={0:7,1:5,2:2,3:10}
    return (answer[1]-answer[ a8_dict[answer[8]] ])**2 !=1


# In[17]:


print(test8([_,1,2,3,4,5,6,7,0])) #应当为真, 第8题选了A, 第1题的答案是1, 与第7题的答案7不相邻
print(test8([_,4,2,3,4,5,6,7,1])) #应当为假, 第8题选了B, 第1题的答案是4, 与第5题的答案5相邻


# ## 第9题
# 已知"第1题与第6题的答案相同" 与 "第x题与第5题的答案相同" 的真假性相反, 那么X为: 
# * A. 第6题 
# * B. 第10题 
# * C. 第2题
# * D. 第9题
# 
# 建立映射关系: 
# ```
# a9_dict={0:6,1:10,2:2,3:9}
# ```
# 
# "第1题与第6题的答案相同", 这句话的逻辑值是answer[1]==answer[6]
# 
# 真假性相反用not表示
# 
# * 如果选A, 那么X=6,  第6题与第5题的答案相同的逻辑值是answer[6]==answer[5],   那么not(answer[6]==answer[5])==(answer[1]==answer[6])
# * 如果选B, 那么X=10, 第10题与第5题的答案相同的逻辑值是answer[10]==answer[5], 那么not(answer[10]==answer[5])==(answer[1]==answer[6])
# 

# In[18]:


def test9(answer):
    a9_dict={0:6,1:10,2:2,3:9}
    return not(answer[a9_dict[answer[9]]]==answer[5])==(answer[1]==answer[6])


# In[19]:


print(test9([_,1,2,3,4,5,6,7,8,0,10])) # 应当为假, 第9题选了A, 第1题与第6题不同, 那么第6题应该和第5题相同才是真假性相反, 这里不满足
print(test9([_,1,2,3,4,6,6,7,8,0,10])) # 应当为真, 第9题选了A, 第1题与第6题不同, 那么第6题应该和第5题相同才是真假性相反


# ## 第10题
# 在此10道题中, ABCD四个字母出现此处最多与最少者的差为: 
# * A.3
# * B.2
# * C.4
# * D.1
# 
# 我们已经胜利在望, 发现出题人也没有太多花招了. 这题和前面第7题很相似, 只是第7题计算了最少, 这里要计算最多了. 
# 
# 既然最少可以用min(列表)来表示, 那么各个字母出现次数中最少的数量: min( [answer.count(0),answer.count(1),answer.count(2),answer.count(3) ] )
# 
# 那么最多当然用max(列表)来表示, 于是各个字母出现次数中最多的数量: max( [answer.count(0),answer.count(1),answer.count(2),answer.count(3) ] )
# 
# 建立映射关系: 
# ```
# a10_dict={0:3,1:2,2:4,3:1}
# ```

# In[20]:


def test10(answer):
    a10_dict={0:3,1:2,2:4,3:1}
    answer_count_list=[answer.count(0),answer.count(1),answer.count(2),answer.count(3) ] 
    diff= max( answer_count_list ) - min( answer_count_list )
    return a10_dict[answer[10]]==diff


# In[21]:


print(test10(["",1,2,3,4,5,6,7,8,9,0])) #应当为假, 第10题选了A, 最大最小要相差3, 但每个字母只出现了一次, 最大最小相差是0
print(test10(["",1,1,1,4,5,6,7,8,9,0])) #应当为真, 第10题选了A, 最大最小要相差3, 选1出现了3次, 选2, 3都没有, 最大最小相差是3


# # 穷举
# 现在已经把上面10道题的判定函数都写好了. 要求解的答案就是要令上述10道题的判别函数都返回真的情况. 
# 
# 10道单选题, 每道题可能有4种答案, 一共的可能性是
# $$
# 4^{10}=1048576
# $$
# 
# 看起来也不大, 所以就穷举好了. 最简单的方式就是for循环. 虽然也还有其他生成穷举序列的方法, 但本着"想到解法就先实现出来看看"的敏捷开发思路. 先用for循环吧. 
# 
# 所谓for循环, 就是让一个变量依次取得列表中的所有值

# In[22]:


choice=[0,1,2,3]
test1=True
answer=[]
for a1 in choice:
    for a2 in choice:
        for a3 in choice:
            for a4 in choice:
                for a5 in choice:
                    for a6 in choice:
                        for a7 in choice:
                            for a8 in choice:
                                for a9 in choice:
                                    for a10 in choice:
                                        answer=["",a1,a2,a3,a4,a5,a6,a7,a8,a9,a10]
                                        if (True==
                                            test1==
                                            test2(answer)==
                                            test3(answer)==
                                            test4(answer)==
                                            test5(answer)==
                                            test6(answer)==
                                            test7(answer)==
                                            test8(answer)==
                                            test9(answer)==
                                            test10(answer)):
                                            print(answer)
print("That's all")


# # 答案: 
# ![answer.jpg](https://i.loli.net/2018/03/01/5a9821ddb1dc7.jpg)
# 
