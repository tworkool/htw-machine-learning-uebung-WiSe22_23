# https://stackabuse.com/decision-trees-in-python-with-scikit-learn/

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, confusion_matrix

# load the dataset
dataset = pd.read_csv("data/bill_authentication.csv")
""" print(dataset.head())
print(dataset.shape) """

# X contains all data except Class column
# y contains only the Class column
X = dataset.drop('Class', axis=1)
y = dataset['Class']

# we use to split up 20% of the data in to the test set and 80% for training
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)

# train the model with the training data
classifier = DecisionTreeClassifier()
classifier.fit(X_train, y_train)

# make predictions on the trained model
y_pred = classifier.predict(X_test)

print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))