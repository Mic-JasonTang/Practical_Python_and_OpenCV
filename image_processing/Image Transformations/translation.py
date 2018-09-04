# -*- coding: utf-8 -*-
# @Author:   MR_Radish
# @Date:     2018-07-24 10:29:38
# @E-mail:   ty_2016@foxmail.com
# @FileName: translation.py
# @TODO: 图像平移变换


import numpy as np
import argparse
# imutils, it’s a library that
# we are going to write ourselves and create “convenience”
# methods to do common tasks like translation, rotation, and
# resizing.It made by myself.
import imutils
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)

# 平移矩阵
# tx=25, ty=50
M = np.float32([[1, 0, 25], [0, 1, 50]])
print(M)
# Affine: 放射变化
# shape[1]: 宽度
# shape[0]: 高度
# API:https://docs.opencv.org/2.4/modules/imgproc/doc/geometric_transformations.html#warpaffine
shifted = cv2.warpAffine(image, M, dsize=(image.shape[1], image.shape[0]))

print("image.shape:{}".format(image.shape))
print("shifted.shape:{}".format(shifted.shape))
cv2.imshow("Shifted Down and Right", shifted)

# 平移矩阵
# tx=-50, ty = -90
M = np.float32([[1, 0, -50], [0, 1, -90]])
print(M)
shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
cv2.imshow("Shifted Up and Left", shifted)

# shifted = imutils.translate(image, 0, 100)
# cv2.imshow("Shifted Down", shifted)

cv2.waitKey(0)
