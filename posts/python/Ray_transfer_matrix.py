
# coding: utf-8

# # 光线传输矩阵
# 
# 这是一次sympy的小练习. 
# 
# 光线传输矩阵又称做[ABCD矩阵](https://en.wikipedia.org/wiki/Ray_transfer_matrix_analysis) 用来描述近轴光线的传播过程. 
# 
# ![](https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/RayTransferMatrixDefinitions.svg/600px-RayTransferMatrixDefinitions.svg.png)
# 
# 光线穿过一个光学系统的过程可以用一个2x2的矩阵来表示, 如果: 
# * 入射光线距离光轴是x1, 角度是 θ1,  
# * 出射光线距离光轴是x2, 角度是 θ2,
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
# sympy是python库, 用于符号计算, 轻量级, 不依赖于其他库. 符号计算就是做类似于
# $$
# (x+y)^2 = x^2 +2xy+ y^2
# $$
# 
# 试了一下sympy, 看起来还比较容易, 几个要点: 
# * 要把运算中涉及到的符号先定义好, 例如 ``` x,y = symbols('a b') ```
# * 要注意一下大小写, symbols是小写, Matrix是大写, solve是小写
# * 其他没什么了
# 
# 我平时常用的几个函数也不多, 其实在mathematica里面也就常用这些. 
# * symbols(字符串), 字符串里面是符号, 注意用空格隔开
# * expr.subs(字典), 替换, 相当于mathematica里面的expr/.{x->a}
# * Matrix(list), 把一个list转换成矩阵, 向量也用这个表示. 
# * solve(expr,x), 求解expr==0时, x的解
# * simplify(expr), 化简表达式

# In[1]:


from sympy import *


# # ABCD Matrix
# 
# 内置上常用的参数字典, 其实最常用的也就是在自由空间内传播, 和在球面上折射, 而这两者可以合并成在球面上折射然后再传播一段距离. 
# 
# * 在自由空间传播距离为d的矩阵是: 
# $$
# free\space space\space matrix=\begin{bmatrix} 1 & d \\ 0 & 1 \end{bmatrix}
# $$
# * 在球面上折射的矩阵, 如果从n1折射率介质经过半径为R的球面, 折射到n2折射率介质: 
# $$
# curved\space interface\space matrix=\begin{bmatrix} 1 & 0 \\ \frac{(n_1-n_2)}{R n_2} & \frac{n_1}{n_2} \end{bmatrix}
# $$
# * 两者合并是相乘的关系, 注意乘法的顺序, 从右至左应当先经过曲面, 再自由传播: 
# 
# $$
# pass\space curved\space interface\space  matrix=
# \begin{bmatrix} 1 & d \\ 0 & 1 \end{bmatrix}
# \begin{bmatrix} 1 & 0 \\ \frac{(n_1-n_2)}{R n_2} & \frac{n_1}{n_2} \end{bmatrix}
# $$
# 
# 

# In[2]:


def ABCD(dictname):
    d,n1,n2,R,f,p=symbols('d n1 n2 R f p')
    abcd_dict={
        'free space':         [1, d, 0, 1],
        'flat interface':     [1, 0, 0, n1/n2],
        'curved interface':   [1, 0, (n1-n2)/(R*n2), n1/n2],
        'curved mirror':      [1, 0, -2/R, 1],
        'Thin lens':          [1, 0, -1/f, 1],
        'Thin lens in power': [1, 0, -p/1000, 1],
    }
    a,b,c,d=abcd_dict[dictname]
    return Matrix([[a,b],[c,d]])

def free_space(d_inspace):
    d = symbols('d')
    return ABCD('free space').subs(d,d_inspace)
def curved_interface(na,nb,Rx):
    n1,n2,R=symbols('n1 n2 R')
    return ABCD('curved interface').subs([(n1,na),(n2,nb),(R,Rx)])
def pass_curved_interface(surface_parameters):
    n_from,n_to,R,p_from, p_to=surface_parameters
    transfer_matrix =free_space(p_to-p_from) * curved_interface(n_from,n_to,R)
    return transfer_matrix
def Thin_lens_in_power(power):
    p = symbols('p')
    return ABCD("Thin lens in power").subs(p,power)


# # 基础人眼模型
# 
# ## The Gullstrand Schematic Eye
# 数据来自: AAO 2014版 Basic and Clinical Science Course (BCSC) Section 3: Clinical Optics 
# 第75页
# 
# * 折射率:
# ``` python
# n_air: [1, 1]
# n_cornea: [1.376, 1.376]
# n_humor: [1.336,1.336]
# n_vitreous: [1.336,1.336]
# n_lens:[1.386,1.386]
# n_core_lens:[1.406,1.406]
# ```
# * 顶点位置: 
# ``` python
# p_cornea_Anterior: [0,0]
# p_cornea_Posterior: [0.5,0.5]
# p_lens_Anterior: [3.6, 3.2]
# p_core_lens_Anterior: [4.146, 3.8725]
# p_core_lens_Posterior: [6.565, 6.5275]
# p_lens_Posterior: [7.2,7.2]
# p_retina: [24.4, 24.4]
# ```
# 
# * 曲率半径: 
# ``` python
# R_cornea_Anterior: [7.7, 7.7]
# R_cornea_Posterior: [6.8, 6.8]
# R_lens_Anterior: [10, 5.33]
# R_core_lens_Anterior: [7.911, 2.655]
# R_core_lens_Posterior: [-5.76, -2.655]
# R_lens_Posterior: [-6.0, -5.33]
# ```
# 
# 
# 
# 

# In[3]:


def Gullstrand_Schematic_Eye(eye_parameters):
    
    # 需要定义成符号
    n_air, n_cornea,n_humor, n_vitreous, n_lens, n_core_lens = symbols(
    'n_air n_cornea n_humor n_vitreous n_lens n_core_lens')
    p_cornea_Anterior,p_cornea_Posterior,p_lens_Anterior,p_core_lens_Anterior,p_core_lens_Posterior,p_lens_Posterior,p_retina=symbols(
    'p_cornea_Anterior p_cornea_Posterior p_lens_Anterior p_core_lens_Anterior p_core_lens_Posterior p_lens_Posterior p_retina')
    R_cornea_Anterior,R_cornea_Posterior,R_lens_Anterior,R_core_lens_Anterior,R_core_lens_Posterior,R_lens_Posterior=symbols(
    'R_cornea_Anterior R_cornea_Posterior R_lens_Anterior R_core_lens_Anterior R_core_lens_Posterior R_lens_Posterior')
    
    # 对各个曲面的参数定义: 入射介质折射率, 出射介质折射率, 曲率半径, 本曲面顶点位置, 下一个曲面顶点位置
    surface={
    "cornea_Anterior": [n_air,n_cornea,R_cornea_Anterior,p_cornea_Anterior, p_cornea_Posterior],
    "cornea_Posterior":[n_cornea,n_humor,R_cornea_Posterior,p_cornea_Posterior,p_lens_Anterior],
    "lens_Anterior":[n_humor,n_lens,R_lens_Anterior,p_lens_Anterior,p_core_lens_Anterior],
    "core_lens_Anterior":[n_lens,n_core_lens,R_core_lens_Anterior,p_core_lens_Anterior, p_core_lens_Posterior],
    "core_lens_Posterior":[n_core_lens,n_lens,R_core_lens_Posterior,p_core_lens_Posterior,p_lens_Posterior],
    "lens_Posterior":[n_lens,n_vitreous,R_lens_Posterior,p_lens_Posterior,p_retina],
    "retina":[n_vitreous,n_vitreous,1,p_retina,p_retina]
    }
    
    # 曲面的顺序
    surface_seq=["cornea_Anterior","cornea_Posterior","lens_Anterior","core_lens_Anterior",
                "core_lens_Posterior","lens_Posterior","retina"]
    
    # 连乘
    eye_transfer_matrix= eye(2) # identity matrix
    for s in surface_seq:
        m = pass_curved_interface(surface[s])
        eye_transfer_matrix= m * eye_transfer_matrix
    
    return eye_transfer_matrix.subs(eye_parameters)


# ## Gullstrand_Schematic_Eye具体参数
# 
# 每个项目有两个参数, 前者是调节放松状态, 后者是最大调节状态

# In[4]:


Gullstrand_Schematic_Eye_parameters={
    "n_air": [1, 1],
    "n_cornea": [1.376, 1.376],
    "n_humor": [1.336,1.336],
    "n_vitreous": [1.336,1.336],
    "n_lens":[1.386,1.386],
    "n_core_lens":[1.406,1.406],
    "p_cornea_Anterior": [0,0],
    "p_cornea_Posterior": [0.5,0.5],
    "p_lens_Anterior": [3.6, 3.2],
    "p_core_lens_Anterior": [4.146, 3.8725],
    "p_core_lens_Posterior": [6.565, 6.5275],
    "p_lens_Posterior": [7.2,7.2],
    "p_retina": [24.4, 24.4],
    "R_cornea_Anterior": [7.7, 7.7],
    "R_cornea_Posterior": [6.8, 6.8],
    "R_lens_Anterior": [10, 5.33],
    "R_core_lens_Anterior": [7.911, 2.655],
    "R_core_lens_Posterior": [-5.76, -2.655],
    "R_lens_Posterior": [-6.0, -5.33],
}


# ## 调节状态
# 假定调节状态是各个参数的线性变化

# In[5]:


def Accommodation_state(persentage):
    state={k:v[0]+persentage*(v[1]-v[0])
        for (k,v) in 
        zip(Gullstrand_Schematic_Eye_parameters.keys(),
            Gullstrand_Schematic_Eye_parameters.values())}
    return state


# ## 测试
# 
# 假定调节状态从0到1, 以0.2变化, 其中调节状态=0是调节放松, 调节状态=1是最大调节状态. 
# 
# 入射光从光轴旁0.1mm,平行于光轴入射. 

# In[6]:


import numpy as np
input_light=Matrix([0.1,0])
for Accommodation in np.linspace(0,1,5):
    eye_parameters=Accommodation_state(Accommodation)
    eye_matrix=Gullstrand_Schematic_Eye(eye_parameters)
    output_light=eye_matrix*input_light
    print("视网膜上光点距离光轴的距离是: {0}\n入射到视网膜上的角度是: {1}\n".format(output_light[0],output_light[1]))


# ## 测试求解某个参数
# 
# 将各个参数都先赋值, 然后取出要求解的x, 将其设定为symbol, 指定入射光线和出射光线参数后, 就可以求解了. 
# 由于是使用的符号运算, 所以可以使用solve命令进行求解. 

# In[7]:


def solve_x_in_focus(optic_matrix,parameters,x):
    parameters[x]=symbols(x)
    # 因为使用近轴光线假设, 所以并不存在球差, 
    # 所以输入光线平行于光轴都可以汇聚, 于输入光线位置无关
    x_input=symbols('x_input')
    input_light=Matrix([x_input,0])
    output_light=optic_matrix(parameters)*input_light
    result = solve(output_light[0],symbols(x))[0]
    return result


# In[8]:


eye_parameters=Accommodation_state(0)
x="p_retina"
p_retina = solve_x_in_focus(Gullstrand_Schematic_Eye,eye_parameters,x)

print("视网膜位置在: {0}".format( p_retina))


# # 戴上眼镜
# 
# 眼镜认为是薄透镜, 角膜距离眼镜12mm

# In[9]:


# f, d = symbols('f d')
glasses_matrix=free_space(12) * ABCD('Thin lens in power')
def Gullstrand_Schematic_Eye_wear_glasses(eye_parameters):
    return Gullstrand_Schematic_Eye(eye_parameters)*glasses_matrix


# In[10]:


eye_wear_glasses_parameters=Accommodation_state(0)
eye_wear_glasses_parameters["p_retina"]=25.6
power=solve_x_in_focus(Gullstrand_Schematic_Eye_wear_glasses,eye_wear_glasses_parameters,'p')
print("眼镜屈光度={}".format(power))


# # 计算人工晶体

# ## 人工晶体眼
# 
# 人工晶体假定为薄透镜, 所在位置为ELP.
# 
# 待调整, 可能需要把角膜两层合成一个K. 
# 
# 目前结果看起来有点怪异, 一般认为正视眼放入的IOL大约是19-20D, 现在得出的结果有点差得远, 大概什么地方有错误

# In[11]:


def IOL_Eye(IOL_eye_parameters):
    
    # 需要定义成符号
    n_air, n_cornea,n_humor, n_vitreous, n_lens, n_core_lens = symbols(
    'n_air n_cornea n_humor n_vitreous n_lens n_core_lens')
    p_cornea_Anterior,p_cornea_Posterior,p_lens_Anterior,p_core_lens_Anterior,p_core_lens_Posterior,p_lens_Posterior,p_retina=symbols(
    'p_cornea_Anterior p_cornea_Posterior p_lens_Anterior p_core_lens_Anterior p_core_lens_Posterior p_lens_Posterior p_retina')
    R_cornea_Anterior,R_cornea_Posterior,R_lens_Anterior,R_core_lens_Anterior,R_core_lens_Posterior,R_lens_Posterior=symbols(
    'R_cornea_Anterior R_cornea_Posterior R_lens_Anterior R_core_lens_Anterior R_core_lens_Posterior R_lens_Posterior')
    ELP=symbols('ELP')
    IOL_Power=symbols('IOL_Power')
    # 对各个曲面的参数定义: 入射介质折射率, 出射介质折射率, 曲率半径, 本曲面顶点位置, 下一个曲面顶点位置
    surface={
    "cornea_Anterior": [n_air,n_cornea,R_cornea_Anterior,p_cornea_Anterior, p_cornea_Posterior],
    "cornea_Posterior":[n_cornea,n_humor,R_cornea_Posterior,p_cornea_Posterior,ELP],
    }
    
    # 曲面的顺序
    surface_seq=["cornea_Anterior","cornea_Posterior"]
    
    # 连乘
    eye_transfer_matrix= eye(2) # identity matrix
    for s in surface_seq:
        m = pass_curved_interface(surface[s])
        eye_transfer_matrix= m * eye_transfer_matrix
        
    # 经过人工晶体
    # 此处可能有错误, 是否应当代入折射率
    eye_transfer_matrix = Thin_lens_in_power(IOL_Power/n_humor)*eye_transfer_matrix
    
    # 到达视网膜
    eye_transfer_matrix = free_space(p_retina-ELP)*eye_transfer_matrix
    
    return eye_transfer_matrix.subs(IOL_eye_parameters)


# In[12]:


IOL_eye_parameters = {
    "n_air": 1,
    "n_cornea": 1.376,
    "n_humor": 1.336,
    "n_vitreous": 1.336,
    "p_cornea_Anterior": 0,
    "p_cornea_Posterior": 0.5,
    "p_retina": 24.4, 
    "R_cornea_Anterior": 7.7,
    "R_cornea_Posterior": 6.8,
    "ELP": 4,
    "IOL_Power":19,
}


# In[13]:


# IOL_eye_parameters['ELP']=symbols('ELP')
x="IOL_Power"
IOL_Power = simplify(solve_x_in_focus(IOL_Eye,IOL_eye_parameters,x))

print("人工晶体度数=: {0}".format( IOL_Power))


# In[ ]:




