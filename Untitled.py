
# coding: utf-8

# In[1]:


from sympy import *


# * symbols(字符串), 字符串里面是符号, 注意用空格隔开
# * expr.subs(字典), 替换, 相当于mathematica里面的expr/.{x->a}
# * Matrix(list), 把一个list转换成矩阵, 向量也用这个表示. 
# * solve(expr,x), 求解expr==0时, x的解
# * simplify(expr), 化简表达式

# In[3]:


a0,a1,a2,a3,an,an_m1,an_m2,x=symbols('a0 a1 a2 a3 an an_m1 an_m2 x')
Sn,Sn_m1,Sn_m2=symbols('Sn,Sn_m1,Sn_m2')


# In[ ]:


Gn=a0*x^0+a1*x1+Sn

