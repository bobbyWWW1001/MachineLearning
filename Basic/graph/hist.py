import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

n = 10
val = np.random.randn(n)
print(val)

# matplot
# 显示变量的数值分布，一般用于连续型变量
# bins 默认 10，表示 x 轴数据划分为多少个不同的组
# val 表示 x 轴数据
# y 轴表示 val 中数据出现的频数
plt.hist(val, bins=10)
plt.show()

# seaborn
sns.displot(val, kde=False)
plt.show()
sns.displot(val, kde=True)
plt.show()

