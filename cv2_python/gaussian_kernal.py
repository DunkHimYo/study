import numpy as np
import cv2
import time
import matplotlib.pyplot as plt

img = cv2.imread(r'./bleak_2-wallpaper-5120x3200.jpg')

my_img=cv2.GaussianBlur(img,(3,3),0)
cv2.imshow('a',my_img)
cv2.waitKey()
