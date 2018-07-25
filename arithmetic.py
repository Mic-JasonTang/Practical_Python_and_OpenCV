# -*- coding: utf-8 -*-
# @Author:   MR_Radish
# @Date:     2018-07-24 22:57:55
# @E-mail:   ty_2016@foxmail.com
# @FileName: arithmetic.py
# @TODO: 对像素点进行算术操作

import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)

print("max of 255:{}".format(cv2.add(np.uint8([200]), np.uint8([100]))))
print("min of 0:{}".format(cv2.subtract(np.uint8([50]), np.uint8([100]))))

# 200 + 100 - 256 = 44
print("wrap around: {}".format(np.uint8([200]) + np.uint8([100])))
# 50 - 100 + 256 = 206
print("wrap around: {}".format(np.uint8([50]) - np.uint8([100])))

M = np.ones(image.shape, dtype=np.uint8) * 100
added = cv2.add(image, M)
# 变白了
cv2.imshow("Added", added)

M = np.ones(image.shape, dtype=np.uint8) * 50
subtracted = cv2.subtract(image, M)
# 变黑了
cv2.imshow("Subtracted", subtracted)
cv2.waitKey(0)
