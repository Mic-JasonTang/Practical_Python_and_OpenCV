# -*- coding: utf-8 -*-
# @Author:   MR_Radish
# @Date:     2018-08-01 22:49:45
# @E-mail:   ty_2016@foxmail.com
# @FileName: blurring.py
# @TODO: 图像模式操作

import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)

# average blurring
# 使用hstack,来水平堆叠三个图像
blurred = np.hstack([
	cv2.blur(image, (3, 3)),
	cv2.blur(image, (5, 5)),
	cv2.blur(image, (7, 7))])

# print(image.shape)
# print(blurred.shape)
cv2.imshow("Averaged", blurred)
cv2.waitKey(0)

# gaussian blurring
blurred = np.hstack([
	cv2.GaussianBlur(image, (3, 3), 0),
	cv2.GaussianBlur(image, (5, 5), 0),
	cv2.GaussianBlur(image, (7, 7), 0)])
cv2.imshow("Gaussian", blurred)
cv2.waitKey(0)

# median blurring
# 适合去除salt-and-pepper noise椒盐噪声
blurred = np.hstack([
	cv2.medianBlur(image, 3),
	cv2.medianBlur(image, 5),
	cv2.medianBlur(image, 7)])
cv2.imshow("Median", blurred)
cv2.waitKey(0)

# bilateral Filter
# 在保留边缘的情况下去除噪声，通过2个高斯分布来完成
# 第一个高斯函数仅考虑邻域的像素点，第二个高斯函数用来保持邻域
# 内的像素密度接近。
# The first Gaussian function only considers spatial neighbors, that is, pixels that appear close together in the (x, y)
# coordinate space of the image. The second Gaussian then
# models the pixel intensity of the neighborhood, ensuring
# that only pixels with similar intensity are included in the
# actual computation of the blur.

# cv2.bilateralFileter(image, diameter, color sigma, space sigma)
# diameter: the diameter of our pixel neighborhood
# color sigma: A larger value for color sigma means that more
#              colors in the neighborhood will be considered when computing the blur.
# space sigma: A larger value of space sigma means that pixels farther out from
#              the central pixel will influence the blurring calculation, provided
#              that their colors are similar enough.
blurred = np.hstack([
	cv2.bilateralFilter(image, 5, 21, 21),
	cv2.bilateralFilter(image, 7, 31, 31),
	cv2.bilateralFilter(image, 9, 41, 41)])
cv2.imshow("Bilateral", blurred)
cv2.waitKey(0)
