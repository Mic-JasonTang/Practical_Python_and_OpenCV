# -*- coding: utf-8 -*-
# @Author:   MR_Radish
# @Date:     2018-07-25 15:54:44
# @E-mail:   ty_2016@foxmail.com
# @FileName: masking.py
# @TODO:     按照指定图形覆盖图片

import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "---image", required=True, help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)

mask = np.zeros(image.shape[:2], dtype="uint8")
(cX, cY) = (image.shape[1] // 2, image.shape[0] //2)
cv2.rectangle(mask, (cX - 75, cY - 75), (cX + 75, cY + 75), 255, -1)
cv2.imshow("Mask Rectangle", mask)

# param mask:optional operation mask, 8-bit single channel array,
# that specifies elements of the output array to be changed.
masked = cv2.bitwise_and(image, image, mask=mask)
cv2.imshow("Mask Applied to Image", masked)

mask = np.zeros(image.shape[:2], dtype="uint8")
cv2.circle(mask, (cX, cY), 100, 255, -1)
masked = cv2.bitwise_and(image, image, mask=mask)
cv2.imshow("Mask Circle", mask)
cv2.imshow("Maks Applied to Image", masked)
cv2.waitKey(0)
