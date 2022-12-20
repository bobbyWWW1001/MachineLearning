import matplotlib.pyplot as plt
import seaborn as sns

x = ['c1', 'c2', 'c3', 'c4', 'c5']
y = [3, 8, 18, 8, 4]


# matplot
# 显示固定分类的相应数量，一般用于离散型变量
plt.bar(x, y)
plt.show()

# seaborn
sns.barplot(x=x, y=y)
plt.show()
