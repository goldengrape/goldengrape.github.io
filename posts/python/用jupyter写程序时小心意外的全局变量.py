
# coding: utf-8

# 这周写作业, 用jupyter时遇坑一枚, 导致我改了作业10次以后才全对通过. 
# ![10次交作业](https://i.loli.net/2018/02/07/5a7abfe105014.png)
# 而且这个坑与我当前的编程习惯有关. 有必要记录下来, 以免未来再犯. 
# <!-- TEASER_END -->

# # 过程重现
# 

# In[19]:


import numpy as np

def lstm_forward(x, a0, parameters):
    caches = []
    
    ### START CODE HERE ###
    # Retrieve dimensions from shapes of x and Wy (≈2 lines)
    n_x, m, T_x = x.shape
    n_y, n_a = Wy.shape
    
    # initialize "a", "c" and "y"
    a = np.random.rand(n_a, m, T_x)
    c = np.random.rand(n_a, m, T_x)
    y = np.random.rand(n_y, m, T_x)
    
    # other code
    pass

    return a, y, c, caches


# In[18]:


np.random.seed(1)
x = np.random.randn(3,10,7)
a0 = np.random.randn(5,10)
Wy = np.random.randn(2,5)
by = np.random.randn(2,1)

parameters = {"Wy": Wy, "by": by}

a, y, c, caches = lstm_forward(x, a0, parameters)
print("a[4][3][6] = ", a[4][3][6])
print("a.shape = ", a.shape)
print("y[1][4][3] =", y[1][4][3])
print("y.shape = ", y.shape)


# coursera这门RNN的课程作业, 一般都会给出每一次测试的期望结果, 比如会写明, 输出结果应当是: 
# ```python
# a[4][3][6] =  0.177161164438
# a.shape =  (5, 10, 7)
# y[1][4][3] = 0.15098073328
# y.shape =  (2, 10, 7)
# ```
# 当然实际计算比这个复杂, 我不应该展示作业中的代码, 并不会完整展示整个函数内部. 
# 
# 由于指定了随机数种子np.random.seed(1), 这个结果是可以重现的, 又因为输入是随机数, 如果计算过程错了, 几乎很难出现相同的结果. 
# 
# 所以当我看到计算的结果和期望的输出结果一致, 就理所当然认为自己已经做对了, 于是安心提交, 于是每次都是这个函数无法通过. 但函数内部没有太复杂的计算过程, 怎么也找不到哪里错了, 差点就向coursera报bug了. 直到我搜讨论区里的帖子, 看到[这一条](https://www.coursera.org/learn/nlp-sequence-models/discussions/weeks/1/threads/dEtBDwcQEei__wr1QTcVxA/replies/jpn0MAcSEei-vwoKMc4stg/comments/nXGxtQcdEei9nwpnlVcPbA), 才搞清楚了问题在哪里. 

# # bug解释
# 
# 注意这里: 
# ```python
# def lstm_forward(x, a0, parameters):
#     # Retrieve dimensions from shapes of x and Wy
#     n_y, n_a = Wy.shape
#     return 
# ```
# 我只看到提示说要从Wy里提取出维度信息, 于是就直接取了Wy.shape, 但参数表```def lstm_forward(x, a0, parameters):```之中并没有Wy!
# 
# Wy因为没有出现在参数表里, 没有和参数表中的(x,a0,paramaters) bound在一起, 所以其实是一个[free variable](https://en.wikipedia.org/wiki/Free_variables_and_bound_variables), 一个free variable的取值要从函数外面找, 如果函数外面没有, 自然就会报错. 

# 倒霉的是自己在一个jupyter文件内运行, 和把作业提交给coursera进行检测是两种不同的情况. 
# 
# 自己运行测试的时候是
# ```python
# np.random.seed(1)
# Wy = np.random.randn(2,5)
# parameters = {"Wy": Wy, "by": by}
# a, y, c, caches = lstm_forward(x, a0, parameters)
# ```
# 这里Wy被Wy = np.random.randn(2,5)定义了, 所以在lstm_forward函数内部, 用Wy.shape时会直接找到这里. 
# 
# 而在作业检测时, 恐怕不是这样, 没有外部定义的Wy, 所有给lstm_forward的参数都是从(x, a0, parameters)传入的, 在parameters字典里, 有一个叫做Wy的参数. 

# # 正确的写法

# In[22]:


def lstm_forward(x, a0, parameters):
    # Retrieve dimensions from shapes of x and Wy
    n_y, n_a = parameters["Wy"].shape # 而不是 Wy.shape
    return


# 这样获得的Wy才是从参数表中传入的. 而不是在本地测试时自己去外面找来的. 
# 
# 在
# ```python
# np.random.seed(1)
# Wy = np.random.randn(2,5)
# parameters = {"Wy": Wy, "by": by}
# a, y, c, caches = lstm_forward(x, a0, parameters)
# ```
# 里面, 
# 
# Wy = np.random.randn(2,5) 这句话实际上是隐式定义了一个叫Wy的全局变量, 在这个jupyter文件中各个函数都可以访问. 

# # 为什么危险
# 
# 因为这是和我当前使用jupyter写程序的习惯有关的. 
# 
# 作为一名野生程序员, 我根本不可能记忆大量的python函数, 写上面演示时, 我甚至还要测试一下到底是```np.random.rand(n_a, m, T_x)```还是写成```np.random.rand((n_a, m, T_x))```, 谁能记得np.random.rand和np.random.zeros用的是不一样的括号个数! 
# 
# 我想即使是专业程序员在写代码时也是需要摆上参考书或者参考网站的. 于是我的做法是一边查一边写, 一边写一边改, 直到改通了再写, 那么一边写一边改的时候, 比较方便的是在jupyter开一个cell, 写, 运行, 再写, 再运行, 这一段cell写好以后, 再把它装进一个def的函数里. 
# 
# 那么在这个过程里, 就很容易出现上面的bug, 一个是写的时候不一定考虑好了封装和传入参数表的问题, 二是当前工作内存中是存有之前放入的测试数据的. 

# # 应该怎么改
# 
# 我想: 
# * 首先还是养成好习惯. 如果要用到全局变量, 就要显式声明出来, 
# * 即时封装, 除非是需要在同一个jupyter里展示, 否则最好每个部分都用def给封装起来, 在程序最后用```if __name__=="__main__"```来设定输出的部分. 
# * 完整的测试还是要在另一个文件中调用才好, 如果记得的话, 最好还使用不同的变量名进行参数设定. 
