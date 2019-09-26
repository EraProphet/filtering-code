# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 14:42:31 2019

@author: Administrator
"""

import cv2 as cv
import numpy as np
import time


def blur_demo(img):
    kernel = np.ones([5,5],np.uint8)/25
    dst = cv.filter2D(img,-1,kernel = kernel)
    cv.imshow('output',dst)
    cv.imwrite('D:/picture/blur.jpg',dst)
    
img = cv.imread("D:/picture/test.jpg")    
a1 = time.perf_counter()
blur_demo(img)
a2 = time.perf_counter()
print("用时{}秒".format(a2-a1))

cv.waitKey()
cv.destroyAllWindows()