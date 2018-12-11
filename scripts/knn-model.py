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

from sklearn.neighbors import KNeighborsClassifier
from sklearn import pipeline, preprocessing, neighbors, model_selection

knn_pipe = pipeline.Pipeline([
    ("knn", KNeighborsClassifier())
])

kfold = model_selection.StratifiedKFold(n_splits=10, shuffle=True)

k_range = np.arange(1, 20)
k_scores = []
n_cv = 10

for k in k_range:
    knn_pipe.set_params(knn__n_neighbors=k)
    test_scores = []
    for i in range(n_cv):
        cv_results = model_selection.cross_validate(knn_pipe,xtest, ytest, cv=kfold)
        test_scores.append(np.mean(cv_results["test_score"]))

    k_scores.append(np.mean(test_scores))

from operator import itemgetter
scores = list(zip(k_range,test_scores))
scores.sort(key=itemgetter(1),reverse=True)


knn_pipe.to_pickle('knn.pkl')