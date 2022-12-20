import numpy as np
import pandas as pd
from sklearn.feature_extraction import DictVectorizer
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import cross_val_score
from sklearn.tree import export_graphviz

# 显示所有列
pd.set_option('display.max_columns', None)
# 显示所有行
pd.set_option('display.max_rows', None)


# 数据装载
train_data = pd.read_csv('./data/train.csv')
test_data = pd.read_csv('./data/test.csv')

# 数据探索
print(train_data.info())
print(test_data.info())
print('-'*10)

print(train_data.describe())
print('-'*10)

print(train_data[train_data.Fare == 0])
print('-'*10)

print(train_data.describe(include=['O']))
print('-'*10)

print(train_data.head())
print('-'*10)

print(train_data.tail())
print('-'*10)

print(train_data['Embarked'].value_counts())
print('-'*10)

# 数据清洗

# 平均值补齐
train_data['Age'].fillna(train_data['Age'].mean(), inplace=True)
test_data['Age'].fillna(test_data['Age'].mean(), inplace=True)

train_data[train_data.Fare == 0] = train_data['Fare'].mean()
test_data.fillna(0, inplace=True)
test_data[test_data.Fare == 0] = test_data['Fare'].mean()

# 高频值补齐
train_data['Embarked'].fillna('S', inplace=True)
test_data['Embarked'].fillna('S', inplace=True)


# 放弃补齐 Cabin 字段

print(train_data.info())
print(train_data[train_data.Fare == 0])
print('-'*10)

# 选择特征向量
features = ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked']
train_features = train_data[features]
test_features = test_data[features]

# 浮点型，训练模型时需转换为 int
train_labels = train_data['Survived']

# sparse=False 不产生稀疏矩阵
dvec = DictVectorizer(sparse=False)
train_features = dvec.fit_transform(train_features.to_dict(orient='records'))
test_features = dvec.fit_transform(test_features.to_dict(orient='records'))
print(dvec.get_feature_names())


# 模型训练
clf = DecisionTreeClassifier(criterion='entropy')
clf.fit(train_features, train_labels.astype('int'))


# 评估准确率
acc = clf.score(train_features, train_labels.astype('int'))
# 测试数据集没有结果标签，采用交叉验证方式
acc_cross = np.mean(cross_val_score(clf, train_features, train_labels.astype('int'), cv=10))
print(acc)
print(acc_cross)


# 使用测试集数据预测
pre_labels = clf.predict(test_features)
print(pre_labels)


# 导出可视化决策树
# dot -Tpng clf_ship.dot -o clf_ship.png
export_graphviz(clf, out_file="./clf_ship.dot")




