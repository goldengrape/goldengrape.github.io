
# coding: utf-8

# 以从抗体序列中定位CDR来练习正则表达式. 
# 
# 这个练习中, 我们将会使用这样一些正则表达式: 
# * [A-Z]: 任意字母
# * [A-Z]{3}: 任意字母重复3次
# * [A-Z]{3,5}: 任意字母重复至少3次, 至多5次
# * [A-Z]*?C: 任意字母重复0次或多次直到第一次遇到字母C
# * WYQ|WLQ|WFQ|WYL: 在WYQ, WLQ, WFQ, WYL之中选1个
# * ^A:  以字母A开头
# <!-- TEASER_END -->

# # 定位抗体序列中的CDR

# 在设计抗体时, 如何找出抗体序列中的CDR是一个问题, 
# 
# 按照[这个网页](http://www.bioinf.org.uk/abs/#cdrdef)上所描述的方法, 也可以使用对序列进行分析

# ## 轻链的CDR-L

# * CDR-L1
#     * Start	Approx residue 24
#     * Residue before 	always a Cys
#     * Residue after	always a Trp. Typically Trp-Tyr-Gln, but also, Trp-Leu-Gln, Trp-Phe-Gln, Trp-Tyr-Leu
#     * Length	10 to 17 residues
# * CDR-L2
#     * Start	always 16 residues after the end of L1
#     * Residues before 	generally Ile-Tyr, but also, Val-Tyr, Ile-Lys, Ile-Phe
#     * Length	always 7 residues (except NEW (7FAB) which has a deletion in this region)
# * CDR-L3
#     * Start	always 33 residues after end of L2 (except NEW (7FAB) which has the deletion at the end of CDR-L2)
#     * Residue before 	always Cys
#     * Residues after	always Phe-Gly-XXX-Gly
#     * Length	7 to 11 residues

# 以大名鼎鼎的[Lucentis(Ranibizumab)序列](https://www.drugbank.ca/drugs/DB01270)为例

# In[1]:


import re
VL="DIQLTQSPSSLSASVGDRVTITCSASQDISNYLNWYQQKPGKAPKVLIYFTSSLHSGVPSRFSGSGSGTDFTLTISSLQPEDFATYYCQQYSTVPWTFGQGTKVEIKRTVAAPSVFIFPPSDEQLKSGTASVVCLLNNFYPREAKVQWKVDNALQSGNSQESVTEQDSKDSTYSLSSTLTLSKADYEKHKVYACEVTHQGLSSPVTKSFNRGEC"
VH="EVQLVESGGGLVQPGGSLRLSCAASGYDFTHYGMNWVRQAPGKGLEWVGWINTYTGEPTYAADFKRRFTFSLDTSKSTAYLQMNSLRAEDTAVYYCAKYPYYYGTSHWYFDVWGQGTLVTVSSASTKGPSVFPLAPSSKSTSGGTAALGCLVKDYFPEPVTVSWNSGALTSGVHTFPAVLQSSGLYSLSSVVTVPSSSLGTQTYICNVNHKPSNTKVDKKVEPKSCDKTHL"
print(">Ranibizumab Light Chain\n",VL)
print(">Ranibizumab Heavy Chain\n",VH)


# ### CDR-L1
# 
# #### CDR-L1之前的部分
# * 开始于第24个字母: 
#     * 正则表达式: ```^[A-Z]{24}```
#     * ^表示从字符串开始
#     * [A-Z]表示一个字母
#     * {24}, 表示该字母重复了24次.
#     * 但其实CDR序列开始于第24个字母, 它前面应该是24-1=23个字母, 所以应当是^[A-Z]{23}
# * 序列之前总是Cys(单字母C): ```(^([A-Z]{22})C)```
#     * 也就是CDR之前的序列最后一个字母是C, 那么又用掉一个字母, 应当是23-1=22
#     
# python有个正则表达式的package叫re, 其中re.findall(表达式, 目标字符串), 可以从目标字符串中找到正则表达式所描述的子串, 用括号把正则表达式括起来的话, 就是说这是一个部分

# In[2]:


CDR_L1_before="(^[A-Z]{22}C)"
re.findall(CDR_L1_before,VL)


# #### CDR-L1序列的部分
# * 长度是10 to 17个字母: 
#     * 正则表达式: [A-Z]{10,17}

# In[3]:


CDR_L1_itself="([A-Z]{10,17})"
re.findall(CDR_L1_before+CDR_L1_itself,VL)
# 注意现在还没有定义结尾部分, 所以会直接找到{10, 17}中最大的17这个值


# #### CDR-L1序列之后的部分
# * 序列之后总是Trp(单字母W). 典型的是Trp-Tyr-Gln(WYQ), 但也可能Trp-Leu-Gln(WLQ), Trp-Phe-Gln(WFQ), Trp-Tyr-Leu(WYL): 
#     * 正则表达式: ```(WYQ|WLQ|WFQ|WYL)```
#     * 用|表示或的关系, 考虑到可读性, 我还是把所有的W都写出来了
#     * 如果不想记住语言的优先级, 加括号会更安全一些: ```((WYQ)|(WLQ)|(WFQ)|(WYL))```

# In[4]:


CDR_L1_after="(WYQ|WLQ|WFQ|WYL)"
CDR_L1_pattern="(^[A-Z]{22}C)"+"([A-Z]{10,17})"+"(WYQ|WLQ|WFQ|WYL)"
CDR_L2_pattern=""
CDR_L3_pattern=""
CDR_L_pattern=CDR_L1_pattern+CDR_L2_pattern+CDR_L3_pattern

CDR_Ls=re.findall(CDR_L_pattern,VL)
print(CDR_Ls)


# ### CDR-L2
# * L1结束后16个字母: 
#     * 正则表达式: [A-Z]{16}
#     * 但之前有WYQ已经用掉了3个字母, 又以1个字母开头, 所以应当是[A-Z]{12}
#     * 实际操作中我发现这条好像很难匹配上, 不限定字母数字好像更好些, 用[A-Z]*?
# * 序列长度7个字母: 
#     * 正则表达式: [A-Z]{7}
# * 序列之**前**通常是Ile-Tyr(IY), but also, Val-Tyr(VY), Ile-Lys(IK), Ile-Phe(IF)
#     * 正则表达式: (IY|VY|IK|IF)

# In[5]:


CDR_L1_pattern="(^[A-Z]{22}C)"+"([A-Z]{10,17})"+"(WYQ|WLQ|WFQ|WYL)"
CDR_L2_pattern="([A-Z]*?(IY|VY|IK|IF))"+"([A-Z]{7})"+"([A-Z]*?)" # 以前此处有bug
CDR_L3_pattern=""
CDR_L_pattern=CDR_L1_pattern+CDR_L2_pattern+CDR_L3_pattern

CDR_Ls=re.findall(CDR_L_pattern,VL)
print(CDR_Ls)


# ### CDR-L3
# * L2结束后第33个字母开始, 开始前总是Cys(C), 
#     * 正则表达式: [A-Z]{33}C
#     * 但前面的IY用掉了2个, 开头用掉1个, C用掉1个, 所以是[A-Z]{29}C
#     * 实际操作中我发现这条好像很难匹配上, 不限定字母数字好像更好些, 用[A-Z]*?C
# 
# * 序列长度7 to 11 字母: 
#     * 正则表达式: [A-Z]{7, 11}
# * 序列之后总是Phe-Gly-XXX-Gly(FG?G)
#     * 正则表达式: FG[A-Z]G
#     * XXX表示的是任意, 所以用[A-Z]表示

# In[6]:


CDR_L1_pattern="(^[A-Z]{22}C)"+"([A-Z]{10,17})"+"(WYQ|WLQ|WFQ|WYL)"
CDR_L2_pattern="([A-Z]*?(IY|VY|IK|IF))"+"([A-Z]{7})"+"([A-Z]*?)" # 以前此处有bug
CDR_L3_pattern="([A-Z]*?C)"+"([A-Z]{7,11})"+"(FG[A-Z]G)"
CDR_L_pattern=CDR_L1_pattern+CDR_L2_pattern+CDR_L3_pattern

CDR_Ls=re.findall(CDR_L_pattern,VL)
CDR_L1=CDR_Ls[0][1]
CDR_L2=CDR_Ls[0][5]
CDR_L3=CDR_Ls[0][8]
print(CDR_Ls)
print(CDR_L1,CDR_L2,CDR_L3)


# # 重链的CDR-H
# 
# * CDR-H1
#     * Start	Approx residue 26 (always 4 after a Cys) [Chothia / AbM defintion]; Kabat definition starts 5 residues later
#     * Residues before 	always Cys-XXX-XXX-XXX
#     * Residues after	always a Trp. Typically Trp-Val, but also, Trp-Ile, Trp-Ala
#     * Length	10 to 12 residues [AbM definition]; Chothia definition excludes the last 4 residues
# * CDR-H2
#     * Start	always 15 residues after the end of Kabat / AbM definition) of CDR-H1
#     * Residues before 	typically Leu-Glu-Trp-Ile-Gly, but a number of variations
#     * Residues after	Lys/Arg-Leu/Ile/Val/Phe/Thr/Ala-Thr/Ser/Ile/Ala
#     * Length	Kabat definition 16 to 19 residues; AbM (and recent Chothia) definition ends 7 residues earlier
# * CDR-H3
#     * Start	always 33 residues after end of CDR-H2 (always 2 after a Cys)
#     * Residues before 	always Cys-XXX-XXX (typically Cys-Ala-Arg)
#     * Residues after	always Trp-Gly-XXX-Gly
#     * Length	3 to 25(!) residues

# ### CDR-H1
# * 开始于26个字母后, 序列前总是 Cys-XXX-XXX-XXX: 
#     * 正则表达式: ^[A-Z]{21}C[A-Z]{3}
# * 长度10-12个字母: 
#     * 正则表达式: [A-Z]{10,12}
# * 序列后总是Trp(W). 典型Trp-Val(WV), 但也可能Trp-Ile(WI), Trp-Ala(WA)
#     * 正则表达式: (WV|WI|WA)

# In[7]:


CDR_H1_pattern="(^[A-Z]{21}C[A-Z]{3})"+"([A-Z]{10,12})"+"(WV|WI|WA)"
CDR_H2_pattern=""
CDR_H3_pattern=""
CDR_H_pattern=CDR_H1_pattern+CDR_H2_pattern+CDR_H3_pattern

CDR_Hs=re.findall(CDR_H_pattern,VH)
print(CDR_Hs)


# ### CDR-H2
# 
# * 开始总是在CDR-H1结束后15个字母, 序列开始前典型是Leu-Glu-Trp-Ile-Gly(LEWIG), 但也有一堆变化(WTF)
#     * 正则表达式: [A-Z]*?LEWIG
#     * 此处重重吐槽下, WTF表示what the fuck! 为什么生物学不找人待见, 别说生物学了, 连有机化学都是!说个什么规律, 结果反常情况比规律还多
# * 长度16到19(Kabat定义), 或者7(AbM, Chothia定义)
#     * 正则表达式: [A-Z]{7,19}
# * 序列之后Lys/Arg-Leu/Ile/Val/Phe/Thr/Ala-Thr/Ser/Ile/Ala, 看起来生物学家也使用某种正则表达式的雏形了, 这句话的意思是Lys或者Arg, 然后Leu/Ile/Val/Phe/Thr/Ala之中的1个, 然后Thr/Ser/Ile/Ala之中的一个
#     * 正则表达式: ```[K|R][L|I|V|F|T|A][T|S|I|A]```

# In[8]:


CDR_H1_pattern="(^[A-Z]{21}C[A-Z]{3})"+"([A-Z]{10,12})"+"(WV|WI|WA)"
CDR_H2_pattern="([A-Z]*?)"+"([A-Z]{7,19})"+"([K|R][L|I|V|F|T|A][T|S|I|A])"
CDR_H3_pattern=""
CDR_H_pattern=CDR_H1_pattern+CDR_H2_pattern+CDR_H3_pattern

CDR_Hs=re.findall(CDR_H_pattern,VH)
print(CDR_Hs)


# ### CDR-H3
# * 开时于CDR-H2后33个字母, 序列前总是Cys-XXX-XXX (典型是 Cys-Ala-Arg): 
#     * 正则表达式: ```[A-Z]*? C[A-Z]{2}```
# * 长度通常是3到25个字母: 
#     * 正则表达式: [A-Z]{3,25}
# * 序列之后总是Trp-Gly-XXX-Gly
#     * 正则表达式: WG[A-Z]G

# In[9]:


CDR_H1_pattern="(^[A-Z]{21}C[A-Z]{3})"+"([A-Z]{10,12})"+"(WV|WI|WA)"
CDR_H2_pattern="([A-Z]*?)"+"([A-Z]{7,19})"+"([K|R][L|I|V|F|T|A][T|S|I|A])"
CDR_H3_pattern="([A-Z]*?C[A-Z]{2})"+"([A-Z]{3,25})"+"(WG[A-Z]G)"
CDR_H_pattern=CDR_H1_pattern+CDR_H2_pattern+CDR_H3_pattern

CDR_Hs=re.findall(CDR_H_pattern,VH)
print(CDR_Hs)

CDR_H1=CDR_Hs[0][1]
CDR_H2=CDR_Hs[0][4]
CDR_H3=CDR_Hs[0][7]
print(CDR_H1,CDR_H2,CDR_H3)


# # 识别CDR的函数
# 
# 综上, 可以整合成一组函数, 专门用来识别CDR.
# 在实际使用中, HC CDR是有多种定义方式的, 所以采用了分类讨论的方式

# In[10]:


def search_CDR(CDR1_pattern,CDR2_pattern,CDR3_pattern,seq,loc1,loc2,loc3):
    # 根据pattern在seq中搜索CDR
    # loc1,loc2,loc3标明CDR在各个片段中的位置
    CDR_pattern=CDR1_pattern+CDR2_pattern+CDR3_pattern
    CDRs=re.findall(CDR_pattern,seq)
    try:# 有可能CDR_pattern不能匹配出结果, 因此用try
        #CDR1_pattern, CDR2_pattern, CDR3_pattern, 每个都会匹配出若干结果, 需要根据loc提取
        CDR1=CDRs[0][0+loc1]
        CDR2=CDRs[0][3+loc2]
        CDR3=CDRs[0][7+loc3]
    except: 
        # 当CDR_pattern无法匹配时, 尽量找出错误的区域
        # 于是分别匹配各自的pattern, 如果发现匹配错误, 则单独用? 表示
        try:
            CDR1="?\n"+re.findall(CDR1_pattern,seq)[0][loc1]
        except:
            CDR1="?\n"
        try:
            CDR2="?\n"+re.findall(CDR2_pattern,seq)[0][loc2]
        except:
            CDR2="?\n"
        try:
            CDR3="?\n"+re.findall(CDR3_pattern,seq)[0][loc3]
        except:
            CDR3="?"    
    return [CDR1,CDR2,CDR3]


# In[11]:


def LC_to_CDR(seq,defintion="Kabat"):
    '''
    根据http://www.bioinf.org.uk/abs/#cdrdef中记载的规则, 寻找LC CDR序列
    '''
    # 如果匹配成功, re.findall返回3段序列, CDR前, CDR自身, CDR后, CDR自身位于1号位置
    CDR1_pattern="(^[A-Z]{22}C)"+"([A-Z]{10,17})"+"(WYQ|WLQ|WFQ|WYL)"
    # 如果匹配成功, re.findall返回4!段序列, CDR前, (IY|VY|IK|IF之一), CDR自身, CDR后, CDR自身位于2号位置
    # CDR1与2之间使用松弛匹配, 没有严格限定字母数
    CDR2_pattern="([A-Z]*?(IY|VY|IK|IF))"+"([A-Z]{7})"+"([A-Z]*?)" 
    # 如果匹配成功, re.findall返回3段序列, CDR前, CDR自身, CDR后, CDR自身位于1号位置
    # CDR2与3之间使用松弛匹配, 没有严格限定字母数
    CDR3_pattern="([A-Z]*?C)"+"([A-Z]{7,11})"+"(FG[A-Z]G)"
    CDR_pattern=CDR1_pattern+CDR2_pattern+CDR3_pattern
    return search_CDR(CDR1_pattern,CDR2_pattern,CDR3_pattern,seq,1,2,1)


# In[12]:


def HC_to_CDR(seq,defintion="Kabat"):
    '''
    根据http://www.bioinf.org.uk/abs/#cdrdef中记载的规则, 寻找HC CDR序列
    '''
    # 使用Kabat定义
    # 如果匹配成功, re.findall返回3段序列, CDR前, CDR自身, CDR后, CDR自身位于1号位置
    if defintion=="Kabat":
        CDR1_pattern="(^[A-Z]{21}C[A-Z]{8})"+"([A-Z]{5,7})"+"(WV|WI|WA)"
        CDR2_pattern="([A-Z]{12})"+"([A-Z]{16,19})"+"([K|R][L|I|V|F|T|A][T|S|I|A])"
        CDR3_pattern="([A-Z]*?C[A-Z]{2})"+"([A-Z]{3,25})"+"(WG[A-Z]G)"
    elif defintion=="AbM":
        CDR1_pattern="(^[A-Z]{21}C[A-Z]{3})"+"([A-Z]{10,12})"+"(WV|WI|WA)"
        CDR2_pattern="([A-Z]{12})"+"([A-Z]{9,12})[A-Z]{7}"+"([K|R][L|I|V|F|T|A][T|S|I|A])"
        CDR3_pattern="([A-Z]*?C[A-Z]{2})"+"([A-Z]{3,25})"+"(WG[A-Z]G)"
    elif defintion=="Chothia":
        CDR1_pattern="(^[A-Z]{21}C[A-Z]{3})"+"([A-Z]{6,8})[A-Z]{4}"+"(WV|WI|WA)"
        CDR2_pattern="([A-Z]{12})"+"([A-Z]{9,12})[A-Z]{7}"+"([K|R][L|I|V|F|T|A][T|S|I|A])"
        CDR3_pattern="([A-Z]*?C[A-Z]{2})"+"([A-Z]{3,25})"+"(WG[A-Z]G)"
    CDR_pattern=CDR1_pattern+CDR2_pattern+CDR3_pattern
    CDRs=re.findall(CDR_pattern,seq)
    return search_CDR(CDR1_pattern,CDR2_pattern,CDR3_pattern,seq,1,1,0)


# 还是用Lucentis测试一下

# In[14]:


print(VL)
print(LC_to_CDR(VL))


# In[18]:


import pandas as pd
defintion_list=["Kabat","AbM","Chothia"]
HCCDR_df_list=[]
for d in defintion_list:
    HCCDRs=HC_to_CDR(VH,defintion=d)
    HCCDR_df_list.append(HCCDRs)
df=pd.DataFrame(HCCDR_df_list,index=defintion_list,columns=["CDR 1","CDR 2","CDR 3"])
df


# # 总结
# 
# 在这个练习中使用了一些正则表达式: 
# * [A-Z]: 任意字母
# * [A-Z]{3}: 任意字母重复3次
# * [A-Z]{3,5}: 任意字母重复至少3次, 至多5次
# * [A-Z]*?C: 任意字母重复0次或多次直到第一次遇到字母C
# * WYQ|WLQ|WFQ|WYL: 在WYQ, WLQ, WFQ, WYL之中选1个
# * ^A:  以字母A开头
# 
# 仅仅使用这些就已经可以从抗体序列中找到CDR了
# 

# # 更新
# (2018-3-26)
# 在之前的blog中, 对LC-CDR2的定义写错了. 把
# * "序列之前通常是Ile-Tyr(IY), but also, Val-Tyr(VY), Ile-Lys(IK), Ile-Phe(IF)"
# 错当成了
# * "序列之后通常是Ile-Tyr(IY), but also, Val-Tyr(VY), Ile-Lys(IK), Ile-Phe(IF)"
# 
# 已经修改了代码
