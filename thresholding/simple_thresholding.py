# -*- coding: utf-8 -*-
# @Author:   MR_Radish
# @Date:     2018-08-04 23:28:22
# @E-mail:   ty_2016@foxmail.com
# @FileName: simple_thresholding.py
# @TODO: 使用阈值来进行二值化图像

import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# 使用高斯滤波去掉一些高频的边缘信息
blurred = cv2.GaussianBlur(image, (5, 5), 0)
cv2.imshow("Image", image)

# 155: 阈值
# 255：表示超过阈值就设置为此值
# 返回2个值，一个是阈值，另一个是结果图片
(T, thresh) = cv2.threshold(blurred, 155, 255, cv2.THRESH_BINARY)
print("T:", T)
cv2.imshow("Binary", thresh)
# cv2.THRESH_BINARY_INV表示低于阈值就设置为255
(T, threshInv) = cv2.threshold(blurred, 155, 255, cv2.THRESH_BINARY_INV)
print("T:", T)
cv2.imshow("Binary Inverse", threshInv)

#
cv2.imshow("Coins", cv2.bitwise_and(image, image, mask=threshInv))
cv2.waitKey(0)
