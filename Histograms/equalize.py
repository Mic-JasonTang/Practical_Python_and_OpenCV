# -*- coding: utf-8 -*-
# @Author:   MR_Radish
# @Date:     2018-07-30 10:08:11
# @E-mail:   ty_2016@foxmail.com
# @FileName: equalize.py
# @TODO: 直方图均衡化

import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

eq = cv2.equalizeHist(image)

print("eq.shape:{}".format(np.shape(eq)))
result = np.hstack([image, eq])
print("result.shape:{}".format(result.shape))
cv2.imshow("Histogram Equalization", result)
cv2.waitKey(0)
