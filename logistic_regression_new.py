#LOGISTIC REGRESSION
import numpy as np
import pandas as pd
import math
import scikitplot as skplt
import matplotlib.pyplot as plt
train = pd.read_csv("train.csv")
print("Ratios:",train.shape)
nc = train.columns[train.isnull().any()]
for i in nc:
    print("Null Columns:",i)
train['Embarked'] = train['Embarked'].fillna('S')
train = train.drop(["PassengerId", "Name", "Ticket", "Cabin"], axis=1)
from sklearn.impute import SimpleImputer
imp = SimpleImputer(missing_values='NaN', strategy='median')
train['Age'] = train['Age'].fillna(np.mean(train['Age']))
print("New Column ratios:",train.shape)
train = pd.get_dummies(train, columns=["Sex", "Embarked"])
Y = train["Survived"]
X = train.drop("Survived", axis=1)
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state = 0)
from sklearn.linear_model import LogisticRegression
log = LogisticRegression()
log.fit(X_train, y_train)
y_pred = log.predict(X_test)
from sklearn.metrics import roc_auc_score
print("Area Under the Receiver Operating Characteristic Curve",roc_auc_score(y_test, y_pred) *
100)

y_probas = log.predict_proba(X_test)
skplt.metrics.plot_roc(y_test, y_probas)
from sklearn.metrics import confusion_matrix
print("Confusion matrix",confusion_matrix(y_test, y_pred))
from sklearn.metrics import precision_score, recall_score, f1_score
print("Precision score:",precision_score(y_test, y_pred)*100)
print("Recall score:",recall_score(y_test, y_pred)*100)
print("Average of precision and recall score",f1_score(y_test, y_pred)*100)
plt.show()