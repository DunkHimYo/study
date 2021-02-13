from sklearn.svm import LinearSVC
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import numpy as np

x,y=make_classification(n_samples=100,n_features=2,n_redundant=0,random_state=42)

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)

model=LinearSVC()
model.fit(x_train,y_train)

y_pred = model.predict(x_test)

plt.scatter(x[:, 0], x[:, 1], c=y, marker='.', cmap=plt.cm.bwr, alpha=0.7)

xi = np.linspace(-2, 2)

y = -model.coef_[0][0] / model.coef_[0][1] * xi - model.intercept_ / model.coef_[0][1]

plt.plot(xi, y)
plt.show()
