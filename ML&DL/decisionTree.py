from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
import numpy as np
from sklearn import tree
x,y=make_classification(n_samples=100,n_features=2,n_redundant=0,random_state=42)

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)

model=DecisionTreeClassifier()

model.fit(x_train,y_train)

print(model.score(x_test,y_test))
tree.plot_tree(model)
plt.show()
