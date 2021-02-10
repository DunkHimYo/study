from sklearn import svm, datasets
from sklearn.model_selection import cross_val_score

iris = datasets.load_iris()
x = iris.data
y = iris.target

svc = svm.SVC(C=1, kernel='rbf', gamma=0.001)
scores = cross_val_score(svc, x, y, cv=5)
print(scores)
print(f"평균 점수 : {scores.mean()}")
