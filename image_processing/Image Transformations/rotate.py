# -*- coding: utf-8 -*-
# @Author:   MR_Radish
# @Date:     2018-07-24 16:02:54
# @E-mail:   ty_2016@foxmail.com
# @FileName: rotate.py
# @TODO: 对图像进行旋转

import numpy as np
import argparse
import imutils
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Origin", image)

# 获取图像的h和w
# h:shape[0]
# w:shape[1]
(h, w) = image.shape[:2]
# 计算图像中心点坐标
center = (w // 2, h // 2)

# param1：center
# param2：angle
# param3：scale
M = cv2.getRotationMatrix2D(center, 45, 1.0)
print(M)
# Origin Image.shape:(1797, 2673, 3)
# print("Origin Image.shape:{}".format(image.shape))
rotated = cv2.warpAffine(image, M, dsize=(w, h))
# Rotated Image.shape:(1797, 2673, 3)
# print("Rotated Image.shape:{}".format(rotated.shape))
cv2.imshow("Rotated by 45 Degrees", rotated)

M = cv2.getRotationMatrix2D(center, -90, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
cv2.imshow("Rotated by -90 Degrees", rotated)

rotated = imutils.rotate(image, 180)
cv2.imshow("Rotated by 180 Degrees", rotated)
cv2.waitKey(0)
