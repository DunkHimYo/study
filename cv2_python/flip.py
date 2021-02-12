import numpy as np
import cv2
import time
import matplotlib.pyplot as plt

img = cv2.imread(r'./bleak_2-wallpaper-5120x3200.jpg')

img=cv2.flip(img,10)
cv2.imshow('a',img)
cv2.waitKey()
