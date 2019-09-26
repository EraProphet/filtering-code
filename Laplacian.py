# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 16:45:40 2019

@author: Administrator
"""

import cv2  

#读取图像
img = cv2.imread('D:/picture/peiqi.jpg')

#灰度化处理图像


#拉普拉斯算法
dst = cv2.Laplacian(img, cv2.CV_16S, ksize =3)
Laplacian = cv2.convertScaleAbs(dst) 
a = img -Laplacian 

cv2.imshow("output", Laplacian)

cv2.imshow("output1", a)

cv2.waitKey(0)
cv2.destroyAllWindows()