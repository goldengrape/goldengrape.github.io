
# coding: utf-8

# 以从抗体序列中定位CDR来练习正则表达式. 
# 
# 正则表达式的基础和简介放在以后写
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

# In[10]:


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

# In[2]:


CDR1_before="(^[A-Z]{22}C)"
re.findall(CDR1_before,VL)


# #### CDR-L1序列的部分
# * 长度是10 to 17个字母: 
#     * 正则表达式: [A-Z]{10,17}

# In[3]:


CDR1_itself="([A-Z]{10,17})"
re.findall(CDR1_before+CDR1_itself,VL)
# 注意现在还没有定义结尾部分, 所以会直接找到{10, 17}中最大的17这个值


# #### CDR-L1序列之后的部分
# * 序列之后总是Trp(单字母W). 典型的是Trp-Tyr-Gln(WYQ), 但也可能Trp-Leu-Gln(WLQ), Trp-Phe-Gln(WFQ), Trp-Tyr-Leu(WYL): 
#     * 正则表达式: ```(WYQ|WLQ|WFQ|WYL)```
#     * 用|表示或的关系, 考虑到可读性, 我还是把所有的W都写出来了
#     * 如果不想记住语言的优先级, 加括号会更安全一些: ```((WYQ)|(WLQ)|(WFQ)|(WYL))```

# In[4]:


CDR1_after="(WYQ|WLQ|WFQ|WYL)"
CDR1_pattern="(^[A-Z]{22}C)"+"([A-Z]{10,17})"+"(WYQ|WLQ|WFQ|WYL)"
re.findall(CDR1_pattern,VL)


# ### CDR-L2
# * L1结束后16个字母: 
#     * 正则表达式: [A-Z]{16}
#     * 但之前有WYQ已经用掉了3个字母, 又以1个字母开头, 所以应当是[A-Z]{12}
#     * 实际操作中我发现这条好像很难匹配上, 不限定字母数字好像更好些, 用[A-Z]*?
# * 序列长度7个字母: 
#     * 正则表达式: [A-Z]{7}
# * 序列之后通常是Ile-Tyr(IY), but also, Val-Tyr(VY), Ile-Lys(IK), Ile-Phe(IF)
#     * 正则表达式: (IY|VY|IK|IF)

# In[5]:


CDR1_pattern="(^[A-Z]{22}C)"+"([A-Z]{10,17})"+"(WYQ|WLQ|WFQ|WYL)"
CDR2_pattern="([A-Z]*?)"+"([A-Z]{7})"+"(IY|VY|IK|IF)"
CDR_pattern=CDR1_pattern+CDR2_pattern
re.findall(CDR_pattern,VL)


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


CDR1_pattern="(^[A-Z]{22}C)"+"([A-Z]{10,17})"+"(WYQ|WLQ|WFQ|WYL)"
CDR2_pattern="([A-Z]*?)"+"([A-Z]{7})"+"(IY|VY|IK|IF)"
CDR3_pattern="([A-Z]*?C)"+"([A-Z]{7,11})"+"(FG[A-Z]G)"
CDR_pattern=CDR1_pattern+CDR2_pattern+CDR3_pattern

CDRs=re.findall(CDR_pattern,VL)
CDR1=CDRs[0][1]
CDR2=CDRs[0][4]
CDR3=CDRs[0][7]
print(CDRs)
print(CDR1,CDR2,CDR3)


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

# In[11]:


CDR1_pattern="(^[A-Z]{21}C[A-Z]{3})"+"([A-Z]{10,12})"+"(WV|WI|WA)"
CDR_pattern=CDR1_pattern
re.findall(CDR_pattern,VH)


# ### CDR-H2
# 
# * 开始总是在CDR-H1结束后15个字母, 序列开始前典型是Leu-Glu-Trp-Ile-Gly(LEWIG), 但也有一堆变化(WTF)
#     * 正则表达式: [A-Z]*?LEWIG
#     * 此处重重吐槽下, WTF表示what the fuck! 为什么生物学不找人待见, 别说生物学了, 连有机化学都是!说个什么规律, 结果反常情况比规律还多
# * 长度16到19(Kabat定义), 或者7(AbM, Chothia定义)
#     * 正则表达式: [A-Z]{7,19}
# * 序列之后Lys/Arg-Leu/Ile/Val/Phe/Thr/Ala-Thr/Ser/Ile/Ala, 看起来生物学家也使用某种正则表达式的雏形了, 这句话的意思是Lys或者Arg, 然后Leu/Ile/Val/Phe/Thr/Ala之中的1个, 然后Thr/Ser/Ile/Ala之中的一个
#     * 正则表达式: ```[K|R][L|I|V|F|T|A][T|S|I|A]```

# In[15]:


CDR1_pattern="(^[A-Z]{21}C[A-Z]{3})"+"([A-Z]{10,12})"+"(WV|WI|WA)"
CDR2_pattern="([A-Z]*?)"+"([A-Z]{7,19})"+"([K|R][L|I|V|F|T|A][T|S|I|A])"
CDR_pattern=CDR1_pattern+CDR2_pattern
re.findall(CDR_pattern,VH)


# ### CDR-H3
# * 开时于CDR-H2后33个字母, 序列前总是Cys-XXX-XXX (典型是 Cys-Ala-Arg): 
#     * 正则表达式: ```[A-Z]*? C[A-Z]{2}```
# * 长度通常是3到25个字母: 
#     * 正则表达式: [A-Z]{3,25}
# * 序列之后总是Trp-Gly-XXX-Gly
#     * 正则表达式: WG[A-Z]G

# In[19]:


CDR1_pattern="(^[A-Z]{21}C[A-Z]{3})"+"([A-Z]{10,12})"+"(WV|WI|WA)"
CDR2_pattern="([A-Z]*?)"+"([A-Z]{7,19})"+"([K|R][L|I|V|F|T|A][T|S|I|A])"
CDR3_pattern="([A-Z]*?C[A-Z]{2})"+"([A-Z]{3,25})"+"(WG[A-Z]G)"
CDRs=re.findall(CDR_pattern,VH)
CDR1=CDRs[0][1]
CDR2=CDRs[0][4]
CDR3=CDRs[0][7]
print(CDRs)
print(CDR1,CDR2,CDR3)


# In[ ]:




