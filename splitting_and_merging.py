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

cv2.imshow("Red", R)
cv2.imshow("Green", G)
cv2.imshow("Blue", B)
cv2.waitKey(0)

merged = cv2.merge([B, G, R])
cv2.imshow("Merged", merged)
cv2.waitKey(0)
cv2.destroyAllWindows()
