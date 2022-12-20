import pandas as pd
import statsmodels.formula.api as api
import statsmodels.stats.anova as anova
import scipy.stats as stats
import warnings

# warnings.filterwarnings("ignore")

df = pd.read_csv('data/ratio.txt')
data1 = df[df['algo'] == 'a']['ratio']
data2 = df[df['algo'] == 'b']['ratio']

# 检查算法1,2 对应的转化率是否满足正态分布
# shapiro 适用于小样本场合 3≤n≤50
# normaltest 适合 20<n<50
# lillifors 适合 50<n<300
# kstest 适合 n>300
# 检测结果中的 p 值远远大于 0.05，所以原假设(H0)成立，数据服从正态分布。
print(stats.shapiro(data1))
print(stats.shapiro(data2))

# 检查两组数据的方差齐性
# p 值仍然明显大于 0.05，说明方差相等或相近
args = [data1, data2]
print(stats.levene(*args))

# 单因素组间(或组内)方差分析(one-way anova)
# p 值明显大于 0.05，接受 H0 原假设，即来自相同正态分布，无显著性差异
print(stats.f_oneway(*args))

# 多因素方差分析
# ~ 分隔符，左边为因变量，右边为自变量，公式中可呈现多自变量
model = api.ols(formula='ratio ~ algo', data=df).fit()
anova_ret = anova.anova_lm(model)
print(anova_ret)
