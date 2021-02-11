import numpy as np
import cv2
import time
import matplotlib.pyplot as plt
img=cv2.imread(r'./retrosupply-jLwVAUtLOAQ-unsplash.jpg')
print(img.shape)
cv2.imshow('retrosupply',img)
a=cv2.waitKey()

print(a)
