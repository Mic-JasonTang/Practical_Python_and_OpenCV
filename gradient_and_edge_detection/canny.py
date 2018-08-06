# -*- coding: utf-8 -*-
# @Author:   MR_Radish
# @Date:     2018-08-06 15:35:36
# @E-mail:   ty_2016@foxmail.com
# @FileName: canny.py
# @TODO: 使用canny来计算边缘
# 上面的结果存在问题：the edges are very “noisy”.
# They are not clean and crisp. 在这里将用canny来解决这些问题.

# 步骤:
# 1.blur the image to remove noise
# 2.compute Sobel gradient image in the x and y direction
# 3.suppress edges
# 4.hysteresis thresholding stage that determine
# if a pixel is "edge-like" or not

import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Original", image)
# remove “noisy” edges
image = cv2.GaussianBlur(image, (5, 5), 0)
cv2.imshow("Blurred", image)

# 30: threshold1
# 150: threshold2
# 任何大于threshold2的像素会被认为是边缘
# 任何小于threshold1的像素不会被认为是边缘
# 在threshold1和threshold2之间的像素按照他们联系强度来判断是否为边缘
# Values in between threshold1
# and threshold2 are either classified as edges or non-edges
# based on how their intensities are “connected”.
canny = cv2.Canny(image, 30, 150)
cv2.imshow("Canny", canny)
cv2.waitKey(0)
