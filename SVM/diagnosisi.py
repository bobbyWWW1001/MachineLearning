import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

import sklearn.svm as svm
import sklearn.model_selection as model_sel
import sklearn.preprocessing as preprocess
import sklearn.metrics as metrics


# 显示所有列
pd.set_option('display.max_columns', None)


train_data = pd.read_csv('./data/data.csv')

# 数据探索
print(train_data.info())
print('-'*30)

print(train_data.describe())
print('-'*30)

print(train_data.describe(include=['O']))
print(train_data['diagnosis'].value_counts())
print('-'*30)

print(train_data.head())
print('-'*30)


# 数据清洗

# mean, se, worst 放入不同集合
features_mean = list(train_data.columns[2:12])
features_se = list(train_data.columns[12:22])
features_worst = list(train_data.columns[22:32])
print(features_mean)
print('-'*30)

# 删除无用的 id 列
# 在横向上遍历每行，去掉列名对应位置的数据
train_data.drop('id', axis=1, inplace=True)
print(train_data.head())
print('-'*30)

# diagnosis 字符类型替换为数字
# B:0, M:1
# 使用字典进行映射
train_data['diagnosis'] = train_data['diagnosis'].map({'B':0, 'M':1})
print(train_data['diagnosis'].value_counts())
print('-'*30)


# 选择特征

# 可视化 diagnosis 计数直方图
sns.countplot(x='diagnosis', data=train_data, label='count')
#plt.show()
# 热力图显示 features_mean 之间关系
corr = train_data[features_mean].corr()
plt.figure(figsize=(16, 16))
sns.heatmap(corr, annot=True)
# plt.show()

# radius_mean 和 perimeter_mean, area_mean 关联大，三选一
# compactness_mean 和 daconcavity_mean concave points_mean  关联大，三选一
features_mean = ['radius_mean', 'texture_mean',
                 'smoothness_mean', 'compactness_mean', 'concavity_mean',
                 'concave points_mean', 'symmetry_mean', 'fractal_dimension_mean']

# 切分训练集和测试集
# random_state 随机种子，重新运行代码可得到相同的结果
train, test = model_sel.train_test_split(train_data, test_size=0.25, random_state=1)
train_x = train[features_mean]
train_y = train['diagnosis']
test_x = test[features_mean]
test_y = test['diagnosis']

# z-score 规范化，均值为 0 ，方差为 1 的正态分布
ss = preprocess.StandardScaler()
train_ss_x = ss.fit_transform(train_x)
# 根据之前进行fit的整体指标，对剩余数据使用同样的均值、方差、最大最小值等进行转换，保证 train、test 处理方式相同
test_ss_x = ss.transform(test_x)

# 训练 SVM（SVC）
# rbf：高斯核函数
# C:default=1.0 分类错误项的惩罚系数，C越大，一旦分类错误，惩罚越严重，准确性越高，泛化能力变差，容易过拟合。
# gamma:1 / n_features
svc = svm.SVC(kernel='rbf', C=1.0, gamma='auto')
svc.fit(train_ss_x, train_y)

# 测试训练结果
predict_y = svc.predict(test_ss_x)

# 计算模型精度
print(np.round(metrics.accuracy_score(test_y, predict_y), 5))


