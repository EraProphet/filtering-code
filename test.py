# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 15:10:03 2019

@author: Administrator
"""

import cv2  
import numpy as np  

 
#读取图片
img = cv2.imread('D:/picture/test.jpg')

 
#高斯滤波
dst = cv2.GaussianBlur(img, (5,5), 0)
print(dst[200,200,])

def blur_demo(img):
    kernel = np.ones([5,5],np.uint8)/ 25
    dst = cv2.filter2D(img,-1,kernel = kernel)
    print(dst[200,200,])
  
blur_demo(img)

