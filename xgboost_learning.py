import xgboost as xgb

from sklearn import datasets
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

iris = datasets.load_iris()
mnist = datasets.load_digits()

X_train, X_test, y_train, y_test = train_test_split(
     mnist.data, mnist.target, test_size=0.33, random_state=42)

X_train = xgb.DMatrix(X_train, y_train)
X_test = xgb.DMatrix(X_test)
# 设置参数
param = {'max_depth':2, 
         'eta':1, 
         'silent':0, 
         'objective': 'multi:softmax', 
         'num_class':10 }

num_round = 50 # 迭代次数

# train and predict
bst = xgb.train(param, X_train, num_round)
preds = bst.predict(X_test)

# return score
score = accuracy_score(y_test, preds)
print(score)
