
# coding: utf-8

# # Alpha的后验分解
# 
# Alpha的后验分解：给定一个组合P，估算该组合相对于业绩基准组合B的各参数：$β_p$ 、$α_p$、 以及组合风险 $σ_p$ 和残差风险 $ω_p$
# 
# 总觉得自己哪里算错了, 华夏上证50(510050)的alpha算出来总是-0.00090, 
# 一时检查不出来, 暂时先摆出来供讨论
# <!-- TEASER_END -->

# In[1]:


import numpy as np
import pandas as pd
import tushare as ts


# # 设定目标

# In[2]:


target="510050.XSHG" # 华夏上证50
benchmark="000300.XSHG" # 沪深300指数
start="2015-1-1"
end="2018-9-1"


# # 获得历史价格

# In[3]:


# 如果有基金净值数据, 不能使用get_price取得, 因此分别提取数据
p_target   =get_price(target   , start_date=start, end_date=end, fields="close")
p_benchmark=get_price(benchmark, start_date=start, end_date=end, fields="close")


# In[4]:


# 为避免投资组合的净值(价格)采样时间与基准的采样时间不同, 取两者的交集
price= pd.concat([p_target, p_benchmark], axis=1, join='inner') 
price.columns=[target,benchmark]
# 通过ts获取基金净值的时间顺序, 与通过ts获取股票价格的时间顺序, 这两者可能不同, 因此统一到时间降序上
price.sort_index(ascending=False, inplace=True)
price.head()


# # 计算收益率
# 
# 每日收益率: 通过投资组合权益计算出的日收益率。
# 
# $$
# 每日收益率=\frac{当前交易日总权益-前一交易日总权益}{前一交易日总权益}
# $$

# In[5]:


r= price.shift(1)/price-1
r.drop(r.index[0], inplace=True) # row 0 is all zero, I think it should be droped
# 取得中债国债收益率曲线作为无风险收益率
r_riskfree=get_yield_curve(start_date=start, end_date=end, tenor='0S')
r = pd.merge(r, r_riskfree, left_index=True, right_index=True,how="inner")
r.columns=[target, benchmark, "riskfree"]
r.head()


# # 计算$\beta$

# 计算方法参考[RiceQuant API文档](https://www.ricequant.com/api/python/chn#backtest-results-factors)
# 
# > 贝塔(beta, $\beta$ ): [CAPM](https://en.wikipedia.org/wiki/Capital_asset_pricing_model)模型中市场基准组合项的系数，表示资产收益对市场整体收益波动的敏感程度。
#  $$
#  \beta=\frac{Cov(r_{p,e}, r_{b,e})}{Var(r_{b,e})}
#  $$
# 
# > 其中$r_{p,e}$为策略超额收益率（策略收益率 - 无风险组合收益率）；$r_{b,e}$为市场基准组合超额收益率（市场基准组合收益率 - 无风险组合收益率）；Cov 表示协方差；Var 表示方差
# 
# 
# 
# 
# 注意: numpy中, np.cov(a,b)的计算结果是$2\times2$矩阵
# $$
# np.cov(a,b)=\left[ \begin{array}{cc} cov\left( a,\; a \right) & cov\left( a,\; b \right) \\ cov\left( a,\; b \right) & cov\left( b,\; b \right) \end{array} \right]
# $$

# In[6]:


r_pe=r[target]-r["riskfree"]
r_be=r[benchmark]-r["riskfree"]
beta=np.cov(r_pe, r_be)[0,1]/np.var(r_be)
beta


# # 求解$\alpha$
# 
# ## 方法1
# 计算方法参考[RiceQuant API文档](https://www.ricequant.com/api/python/chn#backtest-results-factors)
# 
# > 阿尔法(alpha, $\alpha$): [CAPM](https://en.wikipedia.org/wiki/Capital_asset_pricing_model)模型表达式中的残余项。表示策略所持有投资组合的收益中和市场整体收益无关的部分，是策略选股能力的度量。当策略所选股票的总体表现优于市场基准组合成分股时，阿尔法取正值；反之取负值。
# $$
# \alpha=E[r_p-[r_f+\beta \times (r_b-r_f)]]
# $$
# 
# > 其中$r_p$为策略所持有投资组合收益；$r_f$为无风险组合收益；$\beta$为CAPM模型中的贝塔系数；E表示随机变量的期望。

# In[7]:


alpha=(r[target]-(r["riskfree"]+beta*(r[benchmark]-r["riskfree"]))).mean()
alpha


# ## 方法2
# 
# $$
# \theta_p(t)= \alpha_p+ \epsilon(t)
# \\
# E[r_p(t)] = \beta_p E[r_B(t)] + E[\theta_p(t)]
# \\
# \alpha_p=E[\theta_p(t)]
# \\
# \alpha_p=E[r_p(t)]-\beta_p E[r_B(t)]
# $$
# 
# 

# In[8]:


(r_pe.mean()-beta*r_be.mean())


# # 求解投资组合风险 $\sigma_p$
# 
# 

# In[9]:


sigma_p=r[target].std()
sigma_p


# # 求解残差风险 $\omega_p$
# 
# $$
# \omega _{p}=\; \sqrt{\sigma _{p}^{2}-\beta _{p}^{2}\cdot \sigma _{B}^{2}\; }
# $$
# 

# In[10]:


omega_p=np.sqrt(sigma_p**2-beta**2*(r[benchmark].std()**2))
omega_p


# # 年化
# 这里假设一年有244个交易日。

# In[11]:


day_count=len(get_trading_dates(start_date=start,end_date=end))
annual_correct=np.sqrt(244/(day_count-1))
annual_sigma_p=annual_correct*sigma_p
annual_omega_p=annual_correct*omega_p
annual_sigma_p, omega_p


# # RiceQuant上其他一些指标

# ## 年化波动率(volatility, $\sigma_t$): 
# >策略收益率的标准差，最常用的风险度量。波动率越大，策略承担的风险越高。这里假设一年有244个交易日。
# 
# $$
# \sigma =\sqrt{\frac{244}{n-1}\sum_{i=1}^{n}{\left[ r_{p}\left( i \right)\; -\; \bar{r_{p}} \right]^{2}}}
# $$
# 
# >其中，n为回测期内交易日数目；$r_p(i)$ 表示第 i 个交易日策略所持有投资组合的日收益率；$ \bar{r_p} $ 为回测期内策略日收益率的均值。

# In[12]:


volatility=np.sqrt(244/(day_count-1)*(r[target].std()**2)) # 定义与年化投资组合风险sigma_p一致
volatility


# ## 年化跟踪误差(tracking error,$\sigma_t$ ): 
# 
# >纯多头主动交易策略（阿尔法策略和基准择时策略）收益和市场基准组合收益之间差异的度量。跟踪误差越大，意味着策略所持有投资组合偏离基准组合的程度越大。需要注意，跟踪误差不适用于多-空结合的对冲策略的风险评估
# 
# 
# $$
# \sigma =\sqrt{\frac{244}{n-1}\sum_{i=1}^{n}{\left[ r_{pa}\left( i \right)\; -\; \bar{r_{pa}} \right]^{2}}}
# \\
# r_{pa}(i)=r_p(i)-r_b(i)
# $$
# 其中，n为回测期内交易日数量；$r_{pa}(i), r_p(i), r_b(i)$分别表示第i个交易日策略所持有投资组合的日主动收益、日收益率和基准组合的日收益率。

# In[13]:


tracking_error=np.sqrt(244/(day_count-1 * (r_pe.std()**2)))
tracking_error


# ## 年化下行波动率(downside risk, $\sigma_d$):
# 
# > 相比波动率，下行波动率对收益向下波动和向上波动两种情况做出了区分，并认为只有收益向下波动才意味着风险。在实际计算中，我们统一使用基准组合收益为目标收益，作为向上波动和向下波动的判断标准。
# 
# $$
# \sigma =\sqrt{\frac{244}{n-1}\sum_{i=1}^{n}{\left[ r_{p}\left( i \right)\; -\; r_{b}(i) \right]^{2} I(i)}}
# $$
# $$
# I(i)=\begin{cases}1 & r_p(i)<r_b(i) \\ 0 & r_p(i) \geq r_b(i)\end{cases}
# $$
# 
# 
# 
# >其中，n为回测期内交易日数量；$r_p,r_b$ 分别表示第i个交易日策略所持有投资组合的日收益率、基准组合的日收益率；I(i)为指示函数(indicator function)，如果第i个交易日策略所持有投资组合收益低于基准组合收益，则标记为1（向下波动），否则标记为0（向上波动）。

# In[14]:


downside_r=r.where(r[target]<r[benchmark]).dropna()
downside_risk=np.sqrt(244/(day_count-1)*((downside_r[target]-downside_r[benchmark])**2).sum())
downside_risk


# ## 最大回撤(max drawdown): 
# 
# > 在回测期内，在任一交易日往后推，策略总权益走到最低点时收益率回撤幅度的最大值。最大回撤是评估策略极端风险管理能力的重要指标。其计算方式如下：
# $$
# Drawdown_t=\begin{cases}0 & NET_t = min_{j \geq t} NET_j\\\frac{NET_t-min_{j \geq t}NET_j}{NET_t} & ELSE\end{cases}
# \\
# NET=某期净值
# \\
# MaxDrawdown=Max(Drawdown_t)
# $$
# 

# In[15]:


NET=p_target
NET.sort_index(ascending=False, inplace=True)
NET_min=NET.copy()
for date in NET.index:
    NET_min.loc[date]=(NET.loc[:date].min())
Drawdown_t=(NET-NET_min)/NET
max_Drawdown=Drawdown_t.max()
max_Drawdown_date=Drawdown_t.idxmax()
(max_Drawdown_date, max_Drawdown)

