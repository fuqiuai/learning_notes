from sklearn import datasets
from xgboost.sklearn  import XGBClassifier

from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

iris = datasets.load_iris()
mnist = datasets.load_digits()

X_train, X_test, y_train, y_test = train_test_split(
     mnist.data, mnist.target, test_size=0.33, random_state=42)


# 设置参数
clf = XGBClassifier(max_depth=2,learning_rate=1)

# train and predict
clf.fit(X_train, y_train)
preds = clf.predict(X_test)

# return score
score = accuracy_score(y_test, preds)
print(score)
