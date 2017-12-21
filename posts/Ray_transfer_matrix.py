
# coding: utf-8

# # 光线传输矩阵
# 
# 又称做[ABCD矩阵](https://en.wikipedia.org/wiki/Ray_transfer_matrix_analysis) 用来描述近轴光线的传播过程. 
# 
# ![](https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/RayTransferMatrixDefinitions.svg/600px-RayTransferMatrixDefinitions.svg.png)
# 
# 光线穿过一个光学系统的过程可以用一个2x2的矩阵来表示, 如果: 
# * 入射光线距离光轴是x1, 角度是$\theta_1$, 
# * 出射光线距离光轴是x2, 角度是$\theta_2$,
# 
# 那么: 
# $$
# \begin{bmatrix}x_2\\ \theta_2 \end{bmatrix} = \begin{bmatrix}A & B \\C & D \end{bmatrix} \begin{bmatrix}x_1\\ \theta_1 \end{bmatrix}
# $$
# 
# 对于不同的光学元件, ABCD的取值不同. 
# 
# 下面准备使用python的符号运算库sympy, 进行光路的ABCD矩阵分析. 试图建立一个简化的眼球光路追迹模型. 
# <!-- TEASER_END -->

# # Sympy基本
# 
# sympy是python库, 用于符号计算, 轻量级, 不依赖于其他库. 

# In[1]:


from sympy import *
a,b,c,d=symbols("a b c d")
x1,x2,theta1,theta2=symbols('x1 x2 theta1 theta2')


# # ABCD Matrix
# 
# 内置上常用的参数字典

# In[2]:


def ABCD(dictname):
    d,n1,n2,R,f,p=symbols('d n1 n2 R f p')
    abcd_dict={
        'free space':         [1, d, 0, 1],
        'flat interface':     [1, 0, 0, n1/n2],
        'curved interface':   [1, 0, (n1-n2)/R, n1/n2],
        'curved mirror':      [1, 0, -2/R, 1],
        'Thin lens':          [1, 0, -1/f, 1],
        'Thin lens in power': [1, 0, p, 1],
    }
    a,b,c,d=abcd_dict[dictname]
    return Matrix([[a,b],[c,d]])
def free_space(d_inspace):
    return ABCD('free space').subs(d,d_inspace)
def curved_interface(na,nb,Rx):
    n1,n2,R=symbols('n1 n2 R')
    return ABCD('curved interface').subs([(n1,na),(n2,nb),(R,Rx)])


# # 基础人眼模型
# 
# * CCT: 角膜中央厚度
# * AD: 前房深度
# * AL: 眼轴长
# * LT: 晶体厚度
# * VT: 玻璃体厚度
# 
# 注意此模型有两个假设: 
# 
# * 假设角膜, 晶状体和玻璃体是均一介质, 折射率不变. 注意实际情况中这个假设在晶状体是不成立的.
# * 假设角膜前后表面, 晶状体前后表面都是球面, 这个假设也是不成立的

# In[3]:


def human_eye_basic(x_input,theta_input):
    d,n1,n2,R,f,p=symbols('d n1 n2 R f p')
    CCT,AD,K1,K2,LT,VT=symbols('CCT AD K1 K2 LT VT')
    n_cornea, n_humor, n_lens, n_vitreous=symbols('n_cornea n_humor n_lens n_vitreous')
    R_cornea_front,R_cornea_back=symbols('R_cornea_front R_cornea_back ')
    R_lens_front,R_lens_back=symbols('R_lens_front R_lens_back')
    
    input_light=Matrix([x_input,theta_input])
    pass_cornea_front=curved_interface(1,n_cornea,R_cornea_front) 
    
    to_cornea_back=free_space(CCT) 
    pass_cornea_back=curved_interface(n_cornea,n_humor,R_cornea_back)
    
    to_lens_front=free_space(AD)
    pass_lens_front=curved_interface(n_humor,n_lens,R_lens_front)
    
    to_lens_back=free_space(LT)
    pass_lens_back=curved_interface(n_lens,n_vitreous,R_lens_back)
    
    to_retina=free_space(VT)
    
    last =  to_retina *             pass_lens_back *             to_lens_back *             pass_lens_front *             to_lens_front *             pass_cornea_back *             to_cornea_back *             pass_cornea_front *             input_light
    return last


# In[4]:


x_output,theta_output=human_eye_basic(1,0)
print(x_output)


# 看着超长的公式好有趣

# In[ ]:




