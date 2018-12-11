import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import dateutil.parser
import os
import pickle
from sklearn.model_selection import GridSearchCV
from sklearn import linear_model
from sklearn.cross_validation import train_test_split

with open(r"logreg-alldata-final.pkl", "rb") as input_file:
    logreg = pickle.load(input_file)

with open(r'test-train-split.pkl', "rb") as input_file:
    data = pickle.load(input_file)

xtrain_s = data[0]
ytrain   = data[1]
xtest_s  = data[2]
ytest    = data[3]


# Create regularization penalty space
penalty = ['l1', 'l2']

# Create regularization hyperparameter space
C = np.logspace(-2, 4, 1)

# Create hyperparameter options
hyperparameters = dict(C=C, penalty=penalty)

logistic = linear_model.LogisticRegression()


# Create grid search using 5-fold cross validation
clf = GridSearchCV(logistic, hyperparameters, cv=5, verbose=0,n_jobs=-1)
# Fit grid search
best_model = clf.fit(xtrain_s, ytrain)

# View best hyperparameters
print('Best Penalty:', best_model.best_estimator_.get_params()['penalty'])
print('Best C:', best_model.best_estimator_.get_params()['C'])

# Predict target vector
best_model.predict(xtest_s)

pickle.dump(best_model, open('best-model.pkl', 'wb'))

