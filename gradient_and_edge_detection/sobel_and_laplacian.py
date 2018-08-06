# -*- coding: utf-8 -*-
# @Author:   MR_Radish
# @Date:     2018-08-06 15:00:08
# @E-mail:   ty_2016@foxmail.com
# @FileName: sobel_and_laplacian.py
# @TODO: 使用sobel和laplacian算子进行边缘检测

import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Original", image)

# cv2.CV_64F: 表示输出图片的数据类型
# Why are we using a 64-bit float now?
# The reason involves the transition of black-to-white and
# white-to-black in the image.

# Transitioning from black-to-white is considered a positive slope,
# whereas a transition from white-to-black is a
# negative slope. If you remember our discussion of image
# arithmetic in Chapter 6, you’ll know that an 8-bit unsigned
# integer does not represent negative values. Either it will be
# clipped to zero if you are using OpenCV or a modulus op-eration
# will be performed using NumPy.

# The short answer here is that if you don’t use a floating
# point data type when computing the gradient magnitude
# image, you will miss edges, specifically the white-to-black
# transitions.
lap = cv2.Laplacian(image, cv2.CV_64F)
# print("Before:", lap[0, 0], type(lap[0, 0]))  # <class 'numpy.float64'>
lap = np.uint8(np.absolute(lap))
# print("After:", lap[0, 0], type(lap[0, 0]))   # <class 'numpy.uint8'>
cv2.imshow("Laplacian", lap)
cv2.waitKey(0)

# Specify a value of 1 and 0 to find vertical edge-like
# regions and 0 and 1 to find horizontal edge-like regions.

sobelX = cv2.Sobel(image, cv2.CV_64F, 1, 0)
sobelY = cv2.Sobel(image, cv2.CV_64F, 0, 1)

sobelX = np.uint8(np.absolute(sobelX))
sobelY = np.uint8(np.absolute(sobelY))

# an OR operation is true when either pixel is greater than zero.
# Therefore, a given pixel will be True if either a horizontal
# or vertical edge is present. either: 两者中一个
sobelCombined = cv2.bitwise_or(sobelX, sobelY)

cv2.imshow("Sobel X", sobelX)
cv2.imshow("Sobel Y", sobelY)
cv2.imshow("Sobel Combined", sobelCombined)
cv2.waitKey(0)

# 上面的结果存在问题：the edges are very “noisy”.
# They are not clean and crisp.

