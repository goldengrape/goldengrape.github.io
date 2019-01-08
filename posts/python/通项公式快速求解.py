
# coding: utf-8

# 现在每天早上早起, 先做一道[无忧公主的数学时间](https://mp.weixin.qq.com/s/kyWUQoWPPokr4ITg4G3fwA)里面的数学题, 提神醒脑. 
# 
# 今天的题目是这样的:
# 
# >f(1)=f(2)=1
# 
# >f(n)=f(n-1)-f(n-2)+n
# 
# >求f(2018)
# 
# 解法大概是找规律什么的吧, 中间会出现f(n-1)=f(n-2)的情况, 然后有一定的循环.
# 
# 但是, 怎么能这么轻易使用自己手算呢? 一定要暴力编程解决才好.
# 

# 随手写个递归:

# In[1]:


def f(n):
    if n<=2:
        return 1
    else:
        return f(n-1)-f(n-2)+n
N=10
for i in range(1,N+1):
    print(i, f(i))


# 但没有使用尾递归的话, 计算f(2018)肯定是要死机的. 然后, 我**忘记怎么写尾递归了**
# <!-- TEASER_END -->

# 第二招, 母函数
# 
# 要用上母函数, 里面不能有个n这样的变量. 应该消掉. 所以把f(n-1)=f(n-2)-f(n-3)+n-1代入,
# ```
# f(n)=f(n-2)-f(n-3)+n-1 -f(n-2)+n
# f(n)=-f(n-3)+2n-1
# ```
# 再消掉n, 得到:
# $$
# f(n)=2 f(n-1)-2 f(n-2)+f(n-3)+1
# $$

# 然后, 我忘记母函数如何展开了, 要用泰勒展开之类的.

# 还有第三招, 矩阵乘法
# 
# 把f(n)写成一个矩阵M去乘与f(n-1)向量的形式, 然后最终就成了计算M的n次方. 当然, 我又不记得矩阵乘方的运算了, 似乎是进行特征分解. 不过呢, 反正numpy在算矩阵乘法的时候是经过优化的, 速度很快.
# 
# 目的是写出一个简单的矩阵M, 满足下面的式子

# $$
# \begin{bmatrix}
#   f(n) 
#   \\f(n-1)
#   \\f(n-2)
#   \\n+1
#   \\1
# \end{bmatrix}=
# M
# \begin{bmatrix}
#   f(n-1) 
#   \\f(n-2)
#   \\f(n-3)
#   \\n
#   \\1
# \end{bmatrix}
# $$

# 根据条件, 很好写:
# $$
# \begin{bmatrix}
#   f(n) 
#   \\f(n-1)
#   \\f(n-2)
#   \\n+1
#   \\1
# \end{bmatrix}=
# \begin{bmatrix}
#     1,-1,0, 1,0 
#   \\1,0, 0,0,0
#   \\0,1, 0,0,0
#   \\0,0,0,1,1
#   \\0,0,0,0,1
# \end{bmatrix}
# \begin{bmatrix}
#   f(n-1) 
#   \\f(n-2)
#   \\f(n-3)
#   \\n
#   \\1
# \end{bmatrix}
# $$
# 

# 所以程序就很容易写出来了:

# In[2]:


import numpy as np
from numpy.linalg import matrix_power
def f_matrix(n):
    M=np.asarray([
        [1,-1,0,1,0],
        [1,0,0,0,0],
        [0,1,0,0,0],
        [0,0,0,1,1],
        [0,0,0,0,1]
    ])
    f3=np.asarray([f(3),f(2),f(1),4,1])
    if n>3:
        fn=np.matmul(matrix_power(M, n-3), f3)
        return fn[0]
    else:
        return f(n)


# In[5]:


get_ipython().run_cell_magic('timeit', '', 'f_matrix(2018)')


# In[6]:


print(f_matrix(2018))


# 以上方法适用于类似我这样知识点只记得住开头的水平, 即使没有能够记住完整的部分, 也可以利用矩阵乘法在程序内置计算够快的feature来求解. 万一以后做什么面试题, 也许会用上吧
