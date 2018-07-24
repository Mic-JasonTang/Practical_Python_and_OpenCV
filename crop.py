# -*- coding: utf-8 -*-
# @Author:   MR_Radish
# @Date:     2018-07-24 20:12:18
# @E-mail:   ty_2016@foxmail.com
# @FileName: crop.py
# @TODO: 图像裁剪

import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)

# startY=500, endY:620
# startX=540, endY:735
cropped = image[500:620, 540:735]
cv2.imshow("Face", cropped)
cv2.waitKey(0)
