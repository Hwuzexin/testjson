import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
import xgboost as xgb
from xgboost import plot_importance
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score  # 准确率


from sklearn.preprocessing import MinMaxScaler


df = pd.DataFrame(np.random.rand(3, 4), columns=list('abcd'), index=list('ABC'))

print(df)

print('======values======')

print(df.values)
my_matrix = df.values

#独热编码
onehotmatrix = pd.get_dummies(my_matrix[:, 0])
twohotmatrix = pd.get_dummies(my_matrix[:, 1])
#合并矩阵
contact = np.hstack((onehotmatrix, twohotmatrix))  #
print(contact)
trainoutcome = my_matrix[:, 2]
#contact = contact.tolist()
#trainoutcome = trainoutcome.tolist()

# 记载样本数据集
X, Y = contact, trainoutcome
# 数据集分割
X_train,X_test,y_train,y_test = train_test_split(X,Y,test_size=0.2,random_state=123457)


# 算法参数
params = {
    'booster': 'gbtree',
    'objective': 'multi:softmax',
    'num_class': 3,
    'gamma': 0.1,
    'max_depth': 6,
    'lambda': 2,
    'subsample': 0.7,
    'colsample_bytree': 0.7,
    'min_child_weight': 3,
    'slient': 1,
    'eta': 0.1,
    'seed': 1000,
    'nthread': 4,
}

plst = list(params.items())

# 生成数据集格式
dtrain = xgb.DMatrix(X_train, y_train)
num_rounds = 3
# xgboost模型训练
model = xgb.train(plst, dtrain, num_rounds)

# 对测试集进行预测
dtest = xgb.DMatrix(X_test)
y_pred = model.predict(dtest)
print(y_pred)
# 计算准确率
accuracy = accuracy_score(y_test, y_pred)
print('accuarcy:%.2f%%' % (accuracy * 100))

# 显示重要特征
plot_importance(model)
plt.show()