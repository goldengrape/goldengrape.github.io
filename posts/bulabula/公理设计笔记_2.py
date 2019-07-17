#!/usr/bin/env python
# coding: utf-8

# 如同商学院说事一定要画四格表，工学院说事一定要写向量和矩阵的。这种表述就是工科癖好，虽然在后续的语境中确实好用，但复习笔记中还是以平实的语言描述比较好。
# 
# <!-- TEASER_END -->

# 有四个域（Domain）：

# * CNs：Customer Needs，
#     * 客户需求。
#     * 客户域
#     * 就是客户描述的一大堆自然语言也说不清楚的事情，什么高端大气上档次之类的东西。
#     * What adds value
# * FRs：Functional Requirements，
#     * 功能需求。
#     * 功能域
#     * 从CNs域到FRs域的变换，就是把客户漫无边际的需求翻译成一些可定量的参数，比如战舰控制系统的FR有二：1）控制航行方向。2）控制开炮方向。
#     * What it does
# * DPs：Design Parameters，
#     * 设计参数。
#     * 物理域
#     * 实现FRs的物理参数，比如航向控制器和炮塔控制器。
#     * What it looks like
# * PVs：Process Variables，
#     * 过程变量。
#     * 过程域
#     * 没细说，大概是如何实现DPs
#     * How you make it

# 这四个域里，最重要的是FRs（功能需求）到DPs（设计参数）的映射。 （考虑到我一向憎恶缩写，我会在每一个FRs后面都写上功能需求四个字）
# 

# FRs（功能需求）会有很多啦，可以写成
# 
# $$
# FRs=
# \begin{bmatrix}FR_1 
# \\ FR_2
# \\ ...
# \\ FR_n
# \end{bmatrix}
# $$
# 
# 类似的，能够达成FRs（功能需求）的DPs（设计参数）也有很多，可以写成
# 
# $$
# DPs=
# \begin{bmatrix}DP_1 
# \\ DP_2
# \\ ...
# \\ DP_m
# \end{bmatrix}
# $$

# 于是，DPs（设计参数）实现FRs（功能需求）这件事情，就可以写成矩阵乘法的形式
# $$
# FRs=A \times DPs
# $$
# 或者说：
# $$
# \begin{bmatrix}FR_1 
# \\ FR_2
# \\ ...
# \\ FR_n
# \end{bmatrix}=
# \begin{bmatrix}A_{11} & A_{12} & ... & A_{1m}
# \\ A_{21} &  A_{22} & ... & A_{2m}
# \\ ...
# \\ A_{n1} &  A_{n2} & ... & A_{nm}
# \end{bmatrix}
# \begin{bmatrix}DP_1 
# \\ DP_2
# \\ ...
# \\ DP_m
# \end{bmatrix}
# $$
# 
# 当然，不一定是线性的，那工科标准做法就是就求导，反正在小量范围内可以近似成线性的。其实还是类似上面的矩阵，只不过带上了偏导符号而已，还不如原来看得清楚，所以后面就按线性近似来说了。
# 

# 然后，华丽丽的矩阵写好以后，其实我们不关心$A_{ij}$的系数具体是怎样的，只关心是否为0，如果不是0，就画个x。
# 比如USS Monitor号上的情况。
# * $FR_1$（功能需求1）：调整航向
# * $FR_2$（功能需求2）：调整开炮方向
# * $DP_1$（设计参数1）：船舵
# * $DP_2$（设计参数1）：旋转炮塔
# 
# $$
# \begin{bmatrix}FR_1 
# \\ FR_2
# \end{bmatrix}=
# \begin{bmatrix}A_{11} &  A_{12}
# \\ A_{21} &  A_{22}
# \end{bmatrix}
# \begin{bmatrix}DP_1 
# \\ DP_2
# \end{bmatrix}
# $$
# 
# $$
# \begin{bmatrix}FR_1 
# \\ FR_2
# \end{bmatrix}=
# \begin{bmatrix}X &  0
# \\ X &  X
# \end{bmatrix}
# \begin{bmatrix}DP_1 
# \\ DP_2
# \end{bmatrix}
# $$
# 
# 其中转动船舵的时候，船会转向，所以$A_{11}$这里是X，同时船身上的炮塔也跟着船一起转向，所以也影响开炮方向$FR_2$，因此$A_{21}$也是X。
# 而在旋转炮塔的时候，不影响船的航行方向，所以$A_{12}$这里是0。
# 
# 
# 

# # 好的设计
# 
# 一个好的设计是什么呢？
# 
# * 首先FRs（功能需求）的数量N，应当等于DPs(设计参数）的数量M。
# * 每一个FR（功能需求）有且只有一个DP（设计参数）来调整。
# 
# 就是A矩阵应当是一个对角矩阵，也就是说：
# 
# $$
# A=\begin{bmatrix}
# X & 0 & ... & 0
# \\ 0 &  X & ... & 0
# \\ ...
# \\ 0 &  0 & ... & X
# \end{bmatrix}
# $$

# # 可行的设计
# 
# A矩阵是一个三角形矩阵，如果按照调整顺序来规划DPs(设计参数），那么更确切的说，应当是上三角矩阵
# 
# $$
# \mathbf{A}=\left[\begin{array}{ccccc}{X} & {} & {\cdots} & {} & {0} \\ {X} & {X} & {} & {(0)} & {} \\ {X} & {X} & {\ddots} & {} & {\vdots} \\ {\vdots} & {\vdots} & {\ddots} & {\ddots} & {} \\ {X} & {X} & {\dots} & {X} & {X}\end{array}\right]
# $$
# 
# 在这种情况下，DPs(设计参数）仍然是可以一定程度decouple的，比如先调整船的航向，然后再调整炮塔的方向，但炮塔方向要先补偿船的转向，再加上需要旋转的角度。

# # 糟糕的设计
# 
# A里面到处都是X，并且无法通过交换FRs（功能需求）和DPs（设计参数）的顺序来形成三角形矩阵。比如：
# *  FRs（功能需求）的数量N，小于 DPs(设计参数）的数量M。
# 
# CSS Virginia号的情况就是这样，有2个FRs(功能需求）
# * $FR_1$（功能需求1）：调整航向
# * $FR_2$（功能需求2）：调整开炮方向
# 
# 但只有一个DP(设计参数）
# * $DP_1$（设计参数1）：船舵
# 
# $$
# \begin{bmatrix}FR_1 
# \\ FR_2
# \end{bmatrix}=
# \begin{bmatrix}X 
# \\ X 
# \end{bmatrix}
# \begin{bmatrix}DP_1 
# \end{bmatrix}
# $$
# 
# 写不成三角矩阵
# 
# 于是只好靠装甲厚实扛打
