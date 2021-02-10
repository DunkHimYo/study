import numpy as np
from sklearn.metrics import confusion_matrix
from sklearn.metrics import recall_score, f1_score, accuracy_score

y_true = [0, 0, 0, 1, 1, 1]
y_pred = [1, 0, 0, 1, 1, 1]

confMatrix = confusion_matrix(y_true, y_pred)
print(confMatrix)
print(accuracy_score(y_true, y_pred))
print(recall_score(y_true, y_pred))
print(f1_score(y_true, y_pred))
