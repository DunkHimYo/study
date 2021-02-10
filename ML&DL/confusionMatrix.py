import numpy as np
from sklearn.metrics import confusion_matrix

y_true = [0, 0, 0, 1, 1, 1]
y_pred = [1, 0, 0, 1, 1, 1]

confMatrix = confusion_matrix(y_true, y_pred)
print(confMatrix)
print(np.trace(confMatrix)/sum(confMatrix.flat))
