import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

n = 1000
val1 = np.random.randn(n)
val2 = np.random.randn(n)

# 散点图可显示两个变量之间的关系
# matplot
plt.scatter(val1, val2, marker='x')
plt.show()

# seaborn
df = pd.DataFrame({'x': val1, 'y': val2})
sns.jointplot(x='x', y='y', data=df, kind='scatter')


my_data = pd.read_csv('../data/tips.csv')

print(my_data.head())

sns.jointplot(x='total_bill', y='tip', data=my_data, kind='scatter')
sns.jointplot(x='total_bill', y='tip', data=my_data, kind='kde')
sns.jointplot(x='total_bill', y='tip', data=my_data, kind='hex')

plt.show()
