import numpy as np
import sklearn.neighbors as sk_neighbors
import sklearn.datasets as sk_datasets
import sklearn.model_selection as model_sel
import sklearn.preprocessing as preprocess
import sklearn.metrics as metrics
import matplotlib.pyplot as plt

# 装载数据
digits_data = sk_datasets.load_digits()

print(digits_data.images[0])
print(digits_data.target[0])
# plt.imshow(digits_data.images[0])
# plt.show()

print(digits_data.data.shape)

# 切分训练集和测试集
# random_state 随机种子，重新运行代码可得到相同的结果
train_x, test_x, train_y, test_y = model_sel.train_test_split(digits_data.data, digits_data.target,
                                                              test_size=0.25, random_state=1)

# z-score 规范化，均值为 0 ，方差为 1 的正态分布
ss = preprocess.StandardScaler()
train_ss_x = ss.fit_transform(train_x)
# 根据之前进行fit的整体指标，对剩余数据使用同样的均值、方差、最大最小值等进行转换，保证 train、test 处理方式相同
test_ss_x = ss.transform(test_x)

# 训练 KNN 模型
# n_neighbors:默认值 5 代表邻居数量，太小会过拟合，太大会无法分类
# weights:uniform 所有邻居权重都相同
# algorithm:auto 自动选择计算邻居的算法 其他选项有 kd_tree(维度少)，ball_tree(维度大)
# leaf_size:默认 30，影响树的构造及搜素速度
knn = sk_neighbors.KNeighborsClassifier(n_neighbors=5, weights='uniform', algorithm='auto', leaf_size=30)
knn.fit(train_ss_x, train_y)

# 测试训练结果
predict_y = knn.predict(test_ss_x)

# 计算模型精度
print(np.round(metrics.accuracy_score(test_y, predict_y), 5))


