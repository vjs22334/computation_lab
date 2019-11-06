import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder


traindata = pd.read_csv("train.csv")
# traindata.head()
testdata = pd.read_csv("test.csv")
print(traindata)
del traindata['Survived']
del traindata['Name']
del traindata['Ticket']
del traindata['Fare']
del traindata['SibSp']
del traindata['Parch']
del traindata['Embarked']
del traindata['Cabin']
del traindata['PassengerId']

enc = LabelEncoder()
enc.fit(traindata['Sex'])
traindata['Sex'] = enc.transform(traindata['Sex'])

print(traindata)


# print(testdata)
# del testdata['Survived']
# print(testddel traindata['Embarked']ata)
