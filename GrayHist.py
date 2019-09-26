# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 10:32:36 2019

@author: Guo xiaobin
"""
import cv2 as cv
import numpy as np
import time

#遍历像素实现像素值取反
def access_pixels(img):
    print(img.shape)
    height = img.shape[0]
    width = img.shape[1]
    channels = img.shape[2]
    for row in range(height):
        for col in range(width):
            for c in range(channels):
                every_pixels = img[row,col,c]
                img[row,col,c] = 255 - every_pixels
                
    cv.imshow("test",img)
   
#调用cv中的bitwise_not
def inverse(img):
    img = cv.bitwise_not(img)
    cv.imshow("test1",img)
    cv.imwrite("D:/picture/huangbo2.jpg",img)
    
img = cv.imread("D:/picture/huangbo.jpg")
img1 = cv.imread("D:/picture/huangbo.jpg")
cv.imshow("Original image",img)
a1 = time.perf_counter()
access_pixels(img)
a2 = time.perf_counter()
print("用时{}秒".format(a2-a1))
a3 = time.perf_counter()
inverse(img1)
a4 = time.perf_counter()
print("用时{}秒".format(a4-a3))


cv.waitKey()
cv.destroyAllWindows()