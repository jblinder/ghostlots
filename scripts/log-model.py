import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import dateutil.parser
import seaborn as sns
from IPython.display import Image
from sklearn import linear_model
from sklearn.cross_validation import train_test_split

pd.set_option('display.max_columns', 100)
pd.set_option('display.max_rows', 20)
pd.set_option('display.precision', 3)

df_pluto = pd.read_pickle('df_pluto_features-pickling.pkl')
# Drop categorical columns
df_pluto = df_pluto[df_pluto.columns.difference(['BldgClass','FireComp','IrrLotCode','Sanborn','SplitZone','ZoneDist1'])]
# Drop rows with NANs
df_pluto = df_pluto.dropna()


# Create independent/ dependent variables
y = df_pluto['LotUnitRatio'].astype(int)
X = df_pluto[df_pluto.columns.difference(['LotUnitRatio'])]
xtrain, xtest, ytrain,ytest= train_test_split(X,y)

log = linear_model.LogisticRegression(class_weight='balanced',n_jobs=-1)
log.fit(xtrain,ytrain)

# Score Test and Train
test_score = log.score(xtest,ytest)
train_score = log.score(xtrain,ytrain)
print(f'test{test_score} train{train_score}')

log.to_pickle('logistic.pkl')