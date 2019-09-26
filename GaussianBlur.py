# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 14:56:06 2019

@author: Administrator
"""

import cv2  
import numpy as np  
 
#读取图片
img = cv2.imread('D:/picture/test.jpg')

#高斯滤波
dst = cv2.GaussianBlur(img, (5,5), 0)
print(dst[80,200,]) #输出80行200列像素值 BGR图像，返回值为B、G、R的值

#显示图形
cv2.imwrite("D:/picture/post filter.jpg",dst)
cv2.imshow("GaussianBlur", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()