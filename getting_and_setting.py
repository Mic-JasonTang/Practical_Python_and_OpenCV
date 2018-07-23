# -*- coding: utf-8 -*-
# @Author:   MR_Radish
# @Date:     2018-07-23 18:00:01
# @E-mail:   ty_2016@foxmail.com
# @FileName: getting_and_setting.py
# @TODO: 操作图像中的像素点

import argparse
import cv2

parser = argparse.ArgumentParser(prog="PROG")
parser.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(parser.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)
# cv2.waitKey(0)

(b, g, r) = image[0, 0]
print(image[0, 0])
print("Pixel at (0, 0) - Red: {}, Green: {}, Bule: {}".format(r, g, b))
# Update the pixel at (0, 0)
image[0, 0] = (0, 0, 255)
(b, g, r) = image[0, 0]
print("Pixel at (0, 0) - Red: {}, Green: {}, Bule: {}".format(r, g, b))

corner = image[0:200, 0:100]
cv2.imshow("Corner", corner)

# start-y: end-y, start-x: end-x
#第一维是y坐标
image[0:200, 0:100] = (0, 255, 0)

cv2.imshow("Updated", image)
cv2.waitKey(0)
