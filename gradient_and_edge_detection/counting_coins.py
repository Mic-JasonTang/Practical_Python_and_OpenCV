# -*- coding: utf-8 -*-
# @Author:   MR_Radish
# @Date:     2018-08-06 16:13:42
# @E-mail:   ty_2016@foxmail.com
# @FileName: counting_coins.py
# @TODO: 首先利用canny检测出边缘，然后找硬币的轮廓（outlines/contours）

import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Original", image)
# remove “noisy” edges
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
cv2.imshow("Blurred", blurred)

edged = cv2.Canny(blurred, 30, 150)
cv2.imshow("Edged", edged)

# Now that we have the outlines of the coins,
# we can find the contours of the outlines.

# Return Parameter:
# after_detection: our image after applying contour detection.
# cnts: the contours themselves. the type is list.
# hierarchy: hierarchy(层级) of contours.

# Argument:
# edged.copy(): edged image
# cv2.RETR_EXTERNAL: contour type,use cv2.RETR_EXTERNAL to retrieve only
#   the outermost contours.We can also pass in cv2.RETR_LIST to grab all contours.
#   Other methods include hierarchical contours using
#   cv2.RETR_COMP and cv2.RETR_TREE, but hierarchical contours are outside the scope of this book.
# cv2.CHAIN_APPROX_SIMPLE: this argument is how we want to approximate the
#   contour.We use cv2.CHAIN_APPROX_SIMPLE to compress
# horizontal, vertical, and diagonal segments into their endpoints only.
# This saves both computation and memory. If
# we wanted all the points along the contour, without compression,
# we can pass in cv2.CHAIN_APPROX_NONE; however,
# be very sparing when using this function. Retrieving all
# points along a contour is often unnecessary and is wasteful
# of resources.
(after_detection, cnts, hierarchy) = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL,
								 cv2.CHAIN_APPROX_SIMPLE)

print("hierarchy:{}".format(hierarchy))
cv2.imshow("After detection", after_detection)
print("I count {} coins in this image, the list is :{}".format(len(cnts), cnts))

# In order not to draw on our original image,
# we make a copy of the original image
coins = image.copy()
# draws the actual contours on our image.

# The first argument to the function is the image
# we want to draw on.

# The second is our list of contours.

# The Next, we have the contour index. By specifying a negative
# value of −1, we are indicating that we want to draw all of
# the contours. However, we would also supply an index i,
# which would be the i’th contour in cnts. This would allow
# us to draw only a single contour rather than all of them.

# The fourth argument to the cv2.drawContours function
# is the color of the line we are going to draw.

# The last argument is the thickness of the line we
# are drawing. We’ll draw the contour with a thickness of
# two pixels
cv2.drawContours(coins, cnts, -1, (0, 255, 0), 2)
cv2.imshow("Coins", coins)
cv2.waitKey(0)
