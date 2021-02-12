import numpy as np
import cv2
import time
import matplotlib.pyplot as plt

img = cv2.imread(r'./bleak_2-wallpaper-5120x3200.jpg')

retval, my_img=cv2.threshold(img,10,255,cv2.THRESH_TOZERO)
cv2.imshow('a',my_img)
cv2.waitKey()
