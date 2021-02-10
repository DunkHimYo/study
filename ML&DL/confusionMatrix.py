import numpy as np
from sklearn.metrics import confusion_matrix
from sklearn.metrics import recall_score, f1_score, accuracy_score

y_true = [0, 0, 0, 1, 1, 1]
y_pred = [1, 0, 0, 1, 1, 1]

confMatrix = confusion_matrix(y_true, y_pred)
print(confMatrix)

#정확도 : 모든 경우에 맞는 결과의 비율
print(accuracy_score(y_true, y_pred))

# 재현율 : 실제 양성인 데이터중 얼마나 판정했는지 비율
print(recall_score(y_true, y_pred))

# 적합률 : 양성이라고 예측한 데이터 중 몇 퍼센트가 옳은 지 비율
print(precision_score(y_true, y_pred))

#적랍률  재현률 비율
print(f1_score(y_true, y_pred))
