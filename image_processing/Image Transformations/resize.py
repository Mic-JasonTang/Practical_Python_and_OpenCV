# -*- coding: utf-8 -*-
# @Author:   MR_Radish
# @Date:     2018-07-24 16:40:16
# @E-mail:   ty_2016@foxmail.com
# @FileName: resize.py
# @TODO: 改变图像的大小

import numpy as np
import argparse
import imutils
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Origin", image)

print("Orgin image.shape:{}".format(image.shape))

# 按照指定宽度来缩放图片，设置图像新的宽度为150
# 为了按照同等比例缩放，这里计算新宽度/原宽度的比例
new_width = 150
old_width = image.shape[1]
old_height = image.shape[0]
# 计算新的高度
r = new_width / image.shape[1]  # 宽度的缩放因子
new_height = int(old_height * r)

dim = (new_width, new_height)  # 高度乘以宽度的缩放因子
print("r:{}, dim:{}".format(r, dim))

# interpolation：插值
#cv2.INTER_LINEAR, cv2.INTER_CUBIC, cv2.INTER_NEAREST
resized = cv2.resize(image, dim, interpolation= cv2.INTER_AREA)
print("Resized image.shape:{}".format(resized.shape))
cv2.imshow("Resized (Width)", resized)


# 按照指定高度来缩放图片
new_height = 50
old_height = image.shape[0]
new_width = int(image.shape[1] * r)
dim = (new_width, new_height)

resized = cv2.resize(image, dim, interpolation= cv2.INTER_AREA)
cv2.imshow("Resized (Height)", resized)

resize = imutils.resize(image, width=100)
cv2.imshow("Resized via function", resized)
cv2.waitKey(0)
