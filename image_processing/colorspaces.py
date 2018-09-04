# -*- coding: utf-8 -*-
# @Author:   MR_Radish
# @Date:     2018-07-25 23:32:02
# @E-mail:   ty_2016@foxmail.com
# @FileName: colorspaces.py
# @TODO: 颜色空间

import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray", gray)

# Hue-Saturation-Value: 亮度-饱和度
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
cv2.imshow("HSV", hsv)

cv2.waitKey(0)

# Merge时使用
zeros = np.zeros(image.shape[:2], dtype="uint8")
# 拆分HSV
(h, s, v) = cv2.split(hsv)

mergedH = cv2.merge([h, zeros, zeros])
cv2.imshow("Merged Hue", mergedH)

mergedS = cv2.merge([zeros, s, zeros])
cv2.imshow("Merged Saturation", mergedS)

mergedV = cv2.merge([zeros, zeros, v])
cv2.imshow("Merged Value", mergedV)

cv2.waitKey(0)
# L* for the lightness and a* and b* for the green–red and blue–yellow color components
lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
cv2.imshow("L*a*b", lab)

# (L, a, b) = cv2.split(lab)

# mergedL = cv2.merge([L, zeros, zeros])
# cv2.imshow("Merged L", mergedL)

# mergeda = cv2.merge([zeros, a, zeros])
# cv2.imshow("Merged a", mergeda)

# mergedb = cv2.merge([zeros, zeros, b])
# cv2.imshow("Merged b", mergedb)
cv2.waitKey(0)
