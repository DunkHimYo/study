import numpy as np
import cv2
import time
import matplotlib.pyplot as plt
img=cv2.imread(r'./retrosupply-jLwVAUtLOAQ-unsplash.jpg')
print(img.shape)
img=cv2.resize(img,(img.shape[1]//3,img.shape[0]//3))

print(img.shape)
cv2.imshow('retrosupply',img)
a=cv2.waitKey()
print(a)
