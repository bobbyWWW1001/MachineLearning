import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

labels = ['A', 'B', 'C', 'D', 'E']
my_data = np.random.normal(size=(10, 5))

# matplot
# 显示原始数据中（此处每组原始数据包含 10 个数）最大，最小，中位，Q1,Q3 两个四分位数
plt.boxplot(my_data, labels=labels)
plt.show()

# seaborn
df = pd.DataFrame(my_data, columns=labels)
sns.boxplot(data=df)
plt.show()



