# -*- coding: utf-8 -*-
# @Author:   MR_Radish
# @Date:     2018-07-25 19:02:48
# @E-mail:   ty_2016@foxmail.com
# @FileName: splitting_and_merging.py
# @TODO: 图像通道分割与合并

import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
(B, G, R) = cv2.split(image)

print("image.shape:{}".format(image.shape))
print("B.shape:{}, G.shape:{}, R.shape:{}".format(B.shape, G.shape, R.shape))
cv2.imshow("Red", R)
cv2.imshow("Green", G)
cv2.imshow("Blue", B)
cv2.waitKey(0)

merged = cv2.merge([B, G, R])
cv2.imshow("Merged", merged)

# B G R 三个通道都是二维数组
zeros = np.zeros(image.shape[:2], dtype="uint8")
mergedR = cv2.merge([zeros, zeros, R])
cv2.imshow("Merged Red", mergedR)
mergedG = cv2.merge([zeros, G, zeros])
cv2.imshow("Merged Green", mergedG)
mergedB = cv2.merge([B, zeros, zeros])
cv2.imshow("Merged Blue", mergedB)
cv2.waitKey(0)
cv2.destroyAllWindows()
