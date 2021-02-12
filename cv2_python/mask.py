import numpy as np
import cv2
import time
import matplotlib.pyplot as plt

img = cv2.imread(r'./bleak_2-wallpaper-5120x3200.jpg')

mask=cv2.imread(r'./abc.jpg',0)
mask=cv2.resize(mask,(img.shape[1],img.shape[0]))
my_img=cv2.bitwise_or(img,img,mask=mask)
cv2.imshow('a',my_img)
cv2.waitKey()
