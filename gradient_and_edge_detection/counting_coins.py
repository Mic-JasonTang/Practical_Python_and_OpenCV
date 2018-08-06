# -*- coding: utf-8 -*-
# @Author:   MR_Radish
# @Date:     2018-08-06 16:13:42
# @E-mail:   ty_2016@foxmail.com
# @FileName: counting_coins.py
# @TODO: 首先利用canny检测出边缘，然后找硬币的轮廓（outlines/contours）

import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Original", image)
# remove “noisy” edges
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
cv2.imshow("Blurred", blurred)

edged = cv2.Canny(blurred, 30, 150)
cv2.imshow("Edged", edged)
