# -*- coding: utf-8 -*-
# @Author:   MR_Radish
# @Date:     2018-07-24 19:13:06
# @E-mail:   ty_2016@foxmail.com
# @FileName: flipping.py
# @TODO: 翻转图像

import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)

# param1: src, input image
# param2: flipCode:
# >0, Horizontally
# =0, Vertically
# <0, Horizontally & Vertically
flipped = cv2.flip(image, 1)
cv2.flip
cv2.imshow("Flipped Horizontally", flipped)

flipped = cv2.flip(image, 0)
cv2.imshow("Flipped Vertically", flipped)

flipped = cv2.flip(image, -1)
cv2.imshow("Flipped Horizontally & Vertically", flipped)

cv2.waitKey(0)
