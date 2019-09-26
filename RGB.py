# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 10:16:01 2019

@author: Guo xiaobin
"""
import cv2 as cv
import numpy as np
img = cv.imread("D:/picture/huangbo.jpg")
img_rgb = cv.cvtColor(img,cv.COLOR_BGR2RGB)# 读入
 
# 使用numpy进行分割
# b = np.zeros((img.shape[0], img.shape[1]), dtype=img.dtype)
# g = np.zeros((img.shape[0], img.shape[1]), dtype=img.dtype)
# r = np.zeros((img.shape[0], img.shape[1]), dtype=img.dtype)
 
# b[:, :] = img[:, :, 0]  # B蓝色通道
# g[:, :] = img[:, :, 1]  # G绿色通道
# r[:, :] = img[:, :, 2]  # R红色通道
# 使用OpenCV进行分割
b, g, r = cv.split(img)
zeros = np.zeros(img.shape[:2], np.uint8)
b = cv.merge([b, zeros, zeros])
g = cv.merge([zeros, g, zeros])
r = cv.merge([zeros, zeros, r]) 

cv.imshow("Original image",img)
cv.imshow("Blue", b)
cv.imwrite("D:/picture/huangboB.JPG", b)
cv.imshow("Red", r)
cv.imwrite("D:/picture/huangboR.JPG", r)
cv.imshow("Green", g)
cv.imwrite("D:/picture/huangboG.JPG", g)

cv.waitKey(0)
cv.destroyAllWindows()