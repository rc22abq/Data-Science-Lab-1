# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 16:46:53 2023

@author: User
"""

# Lab 9 notes: Classification

# 9.1 Vertebrate Dataset
import warnings
warnings.simplefilter(action="ignore", category=FutureWarning)

import pandas as pd

data = pd.read_csv("vertebrate.csv", header="infer")
print(data)

data["Class"] = data["Class"].replace(["fishes", "birds", "amphibians",
                                       "reptiles"], "non-mammals")
print(data)

crosstab = pd.crosstab([data["Warm-blooded"], data["Gives Birth"]], 
                       data["Class"])
print(crosstab)


# 9.2 Decision Tree Classifier
from sklearn import tree

Y = data["Class"]
X = data.drop(["Name", "Class"], axis=1)

clf = tree.DecisionTreeClassifier(criterion="entropy", max_depth=3)
clf = clf.fit(X, Y)

import pydotplus
from IPython.display import Image

dot_data = tree.export_graphviz(clf, feature_names=X.columns, 
                                class_names=["mammals", "non-mammals"],
                                filled=True, out_file=None)
graph = pydotplus.graph_from_dot_data(dot_data)
Image(graph.create_png())















