# -*- coding: utf-8 -*-
# @Author:   MR_Radish
# @Date:     2018-08-05 17:33:44
# @E-mail:   ty_2016@foxmail.com
# @FileName: adaptive_thresholding.py
# @TODO: 采用自适应滤波
# 计算每个领域一个阈值T

import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(image, (5, 5), 0)
cv2.imshow("Image", image)

# 255: 表示最大值
# cv2.ADAPTIVE_THRESH_MEAN_C: 计算邻域像素的方法，这里采用均值
# cv2.THRESH_BINARY_INV: 表示小于阈值T设置为255(白)，大于阈值T设置为0（黑）
# 11：11表示领域是11x11的区域。
# 4：这个参数也称为C，被均值减。that is subtracted from the mean,
# allowing us to fine-tune our thresholding.
thresh = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
							   cv2.THRESH_BINARY_INV, 11, 4)
cv2.imshow("Mean Thresh", thresh)
# cv2.ADAPTIVE_THRESH_GAUSSIAN_C: 加权平均。
thresh = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
							  cv2.THRESH_BINARY_INV, 15, 3)
cv2.imshow("Gaussian Thresh", thresh)
cv2.waitKey(0)
