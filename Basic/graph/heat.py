import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

flights_data = pd.read_csv('../data/flights.csv')

print(flights_data.shape)
print(flights_data.head())

# 数据透视操作，改变表数据形状
my_data = flights_data.pivot(index='year', columns='month', values='passengers')

print(my_data.head())

# seaborn 绘制热力图
sns.heatmap(my_data)
plt.show()



