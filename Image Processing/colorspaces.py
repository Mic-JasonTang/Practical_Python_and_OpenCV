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

lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
cv2.imshow("L*a*b", lab)

cv2.waitKey(0)
