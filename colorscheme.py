#Source: https://opencv24-python-tutorials.readthedocs.io/en/latest/

import cv2
import numpy as np
from matplotlib import pyplot as plt 


img = cv2.imread('Butter_Album_Cover.jpeg')
img2 = cv2.imread('BTS-UN.jpeg') 
cv2.imshow('Original', img)

# Convert BGR to HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow('HSV', hsv)

# Convert BGR to Grey 
grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Grey', grey)

# Thresholding 
ret,thresh1 = cv2.threshold(grey,127,255,cv2.THRESH_BINARY)
ret,thresh2 = cv2.threshold(grey,127,255,cv2.THRESH_BINARY_INV)
ret,thresh3 = cv2.threshold(grey,127,255,cv2.THRESH_TRUNC)
ret,thresh4 = cv2.threshold(grey,127,255,cv2.THRESH_TOZERO)
ret,thresh5 = cv2.threshold(grey,127,255,cv2.THRESH_TOZERO_INV)

titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
images = [grey, thresh1, thresh2, thresh3, thresh4, thresh5]

for i in range(6):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()

#Adaptive Thresholding 
ret,th1 = cv2.threshold(grey,127,255,cv2.THRESH_BINARY)
th2 = cv2.adaptiveThreshold(grey,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
            cv2.THRESH_BINARY,11,2)
th3 = cv2.adaptiveThreshold(grey,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv2.THRESH_BINARY,11,2)

titles = ['Original Image', 'Global Thresholding (v = 127)',
            'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']
images = [grey, th1, th2, th3]

for i in range(4):
    plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()

# Edge Detection 
edges = cv2.Canny(img2,100,200)

plt.subplot(121),plt.imshow(img2,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

plt.show()

cv2.waitKey(0)
