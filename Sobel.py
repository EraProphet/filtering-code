# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 14:08:36 2019

@author: Administrator
"""

import cv2  

#读取图像
img = cv2.imread('D:/picture/test.jpg',0)

#Sobel算子
x = cv2.Sobel(img, cv2.CV_64F, 1, 0,ksize = 3) #对x求一阶导
y = cv2.Sobel(img, cv2.CV_64F, 0, 1,ksize = 3) #对y求一阶导
absX = cv2.convertScaleAbs(x)    #转换图像深度  
absY = cv2.convertScaleAbs(y)    
Sobel = cv2.addWeighted(absX, 0.5, absY,0.5, 0)

cv2.imshow("output1", Sobel)

cv2.waitKey(0)
cv2.destroyAllWindows()