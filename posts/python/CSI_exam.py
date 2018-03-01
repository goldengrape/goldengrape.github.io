
# coding: utf-8

# 2018年刑侦推理试题: 
# ![question.jpeg](https://i.loli.net/2018/03/01/5a982103b9db2.jpeg)
# <!-- TEASER_END -->

# # 解题思路
# 
# 没啥, 就是暴力穷举, 看看是不是所有的条件都符合

# In[1]:


import numpy as np

def CSI_check(a1,a2,a3,a4,a5,a6,a7,a8,a9,a10):
    allanswer=[_,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10]
    # 1. 这道题的答案是: 
    # 2. 第5题的答案是: 
    a2_a5_dict={0:2,# A.C
                1:3,# B.D
                2:0,# C.A
                3:2}# D.B
    test2=( a5 == a2_a5_dict[a2] )
    
    # 3. 以下选项中哪一题的答案与其他三项不同: 
    a3_list=[a3,a6,a2,a4]
    a3_refer=a3_list[a3]
    a3_list.pop(a3)
    test3=not(a3_refer in a3_list) # 不在剩下的列表中, 所以是与剩下的不同
    
    # 4. 以下选项中哪两题的答案相同: 
    a4_dict={0:[1,5],
             1:[2,7],
             2:[1,9],
             3:[6,10]}
    test4=(allanswer[a4_dict[a4][0]]==            allanswer[a4_dict[a4][1]])
    
    # 5.以下选项中哪一题的答案与本题相同
    a5_dict={0:8,
             1:4,
             2:9,
             3:7}
    test5=(a5 == allanswer[a5_dict[a5]] )
    
    # 6.以下选项中哪两题的答案与第8题相同
    a6_dict={0:[2,4],
             1:[1,6],
             2:[3,10],
             3:[5,9]}
    test6=(a8 == allanswer[a6_dict[a6][0]]) and (
           a8 == allanswer[a6_dict[a6][1]])
    
    # 7.此十道题中, 被选中次数最少的选项字幕为: 
    a7_dict={0:2,
             1:1,
             2:0,
             3:3}
    ans_count=[allanswer.count(ans) for ans in range(4)]
    ans_count_min=min(ans_count)
    test7= allanswer.count(a7_dict[a7])==ans_count_min
    
    # 8.以下选项中, 哪一题的答案与第1题的答案在字母中不相邻: 
    a8_dict={0:7,1:5,2:2,3:10}
    test8=(np.abs(allanswer[a8_dict[a8]]-a8) !=1)
    
    # 9.已知"第1题与第6题的答案相同" 与 "第x题与第5题的答案相同" 的真假性相反, 那么X为: 
    a9_dict={0:6,1:10,2:2,3:9}
    bool_partA=(a1==a6)
    bool_partB=(allanswer[a9_dict[a9]]==a5)
    test9=(bool_partA != bool_partB)
    
    # 10.在此10道题中, ABCD四个字幕出现此处最多与最少者的差为: 
    a10_dict={0:3,1:2,2:4,3:1}
    ans_count_max=max(ans_count)
    test10=(a10_dict[a10]==(ans_count_max-ans_count_min))
    
    ans=(test2 and test3 and test4 and test5 and
         test6 and test7 and test8 and test9 and test10)
    test0=True
    test1=True
    testlist=[test0,test1,test2,test3,test4,test5,test6,test7, test8 , test9 , test10]

    return testlist,ans


# In[2]:


ans_dict={0:"A",1:"B",2:"C",3:"D"}
for a1 in range(4):
    for a2 in range(4):
        for a3 in range(4):
            for a4 in range(4):
                for a5 in range(4):
                    for a6 in range(4):
                        for a7 in range(4):
                            for a8 in range(4):
                                for a9 in range(4):
                                    for a10 in range(4):
                                        allans=[a1,a2,a3,a4,a5,a6,a7,a8,a9,a10]
                                        testlist,test=CSI_check(a1,a2,a3,a4,a5,a6,a7,a8,a9,a10)
                                        if test:
                                            for ind,ans in zip(range(1,11),allans):
                                                print(ind,ans_dict[ans])
                                
print("That's all")


# # 答案: 
# ![answer.jpg](https://i.loli.net/2018/03/01/5a9821ddb1dc7.jpg)
# 

# In[ ]:




