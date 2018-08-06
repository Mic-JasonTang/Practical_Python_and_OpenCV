# -*- coding: utf-8 -*-
# @Author:   MR_Radish
# @Date:     2018-08-05 18:02:31
# @E-mail:   ty_2016@foxmail.com
# @FileName: otsu_and_riddler.py
# @TODO: Otsu’s method大金法进行二值化
# 使用mahotas包里面的otsu，更pythonic
# Otsu’s method assumes there are two peaks in the grayscale
# histogram of the image. It then tries to find an optimal
# value to separate these two peaks – thus our value of T

# While OpenCV provides support for Otsu’s method, I
# prefer the implementation by Luis Pedro Coelho in the mahotas
# package since it is more Pythonic.

import numpy as np
import argparse
import mahotas
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(image, (5, 5), 0)
cv2.imshow("Image:", image)

T = mahotas.thresholding.otsu(blurred)
print("Otsu's threshold: {}".format(T))

thresh = image.copy()
thresh[thresh > T] = 255
thresh[thresh < T] = 0
# 对图像取反操作。
thresh = cv2.bitwise_not(thresh)
# 上面四局代码相当于将>T的变成0（黑），<T变成255(白)
cv2.imshow("Otsu", thresh)

# 最大类间方差法
T = mahotas.thresholding.rc(blurred)
print("Riddler-Calvard: {}".format(T))
thresh = image.copy()
thresh[thresh > T] = 255
thresh[thresh < T] = 0
thresh = cv2.bitwise_not(thresh)
cv2.imshow("Riddler-Calvard", thresh)

cv2.waitKey(0)
