import matplotlib.pyplot as plt

# matplot 显示中文
# 步骤一（替换sans-serif字体）
plt.rcParams['font.sans-serif'] = ['SimHei']

my_labels = ['高中', '本科', '硕士', '博士', '其他']
nums = [7, 39, 22, 6, 3]

# matplot 显示
# 饼图可以用于显示整体和局部的关系
plt.pie(x=nums, labels=my_labels)
plt.show()

