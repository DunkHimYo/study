import numpy as np
import cv2
import time
import matplotlib.pyplot as plt

img = cv2.imread(r'./bleak_2-wallpaper-5120x3200.jpg')

mat = cv2.getRotationMatrix2D(tuple(np.array(img.shape[:2]) / 2), 180,2.0)
print(img)
print(mat)
img=cv2.warpAffine(img,mat,img.shape[:2])

cv2.imshow('a',img)
cv2.waitKey()
