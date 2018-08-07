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
# horizontal, vertical, and diagonal segments into their endpoints only.仅保存轮廓的拐点信息
# This saves both computation and memory. If
# we wanted all the points along the contour, without compression,
# we can pass in cv2.CHAIN_APPROX_NONE; however,
# be very sparing when using this function. Retrieving all
# points along a contour is often unnecessary and is wasteful
# of resources.
(after_detection, cnts, hierarchy) = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL,
								 cv2.CHAIN_APPROX_SIMPLE)

print("hierarchy:\n{}".format(hierarchy))
# output:
# 分别表示第i个轮廓的后一个轮廓、前一个轮廓、父轮廓、内嵌轮廓的索引编号，没有则为-1。
# [[[ 1 -1 -1 -1]
#   [ 2  0 -1 -1]
#   [ 3  1 -1 -1]
#   [ 4  2 -1 -1]
#   [ 5  3 -1 -1]
#   [ 6  4 -1 -1]
#   [ 7  5 -1 -1]
#   [ 8  6 -1 -1]
#   [-1  7 -1 -1]]]

# cv2.imshow("After detection", after_detection)
# 每个元素是三维矩阵
print("I count {} coins in this image, the cnts'shape is :{}".format(len(cnts), np.shape(cnts[0])))
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
for i in range(9):
	cv2.drawContours(coins, cnts, i, (0, 255, 0), 2)
	cv2.imshow("Coins", coins)
	cv2.waitKey(0)
# -1显示所有边缘
# cv2.drawContours(coins, cnts, -1, (0, 255, 0), 2)

# crop each individual coin from the image
for (i, c) in enumerate(cnts):
	# This method finds the “enclosing box” that
	# our contour will fit into, allowing us to crop it from the
	# image. The function takes a single parameter, a contour,
	# and then returns a tuple of the x and y position that the
	# rectangle starts at, followed by the width and height of the
	# rectangle.
	print("c.shape:{}".format(np.shape(c)))
	print(c)
	(x, y, w, h) = cv2.boundingRect(c)
	print("x:{}, y:{}, w:{}, h:{}".format(x, y, w, h))

	print("Coin #{}".format(i+1))
	coin = image[y:y + h, x:x + w]
	cv2.imshow("Coin", coin)

	mask = np.zeros(image.shape[:2], dtype="uint8")
	# We pass in a circle variable, the current
	# contour, and are given the x and y coordinates of the circle,
	# along with its radius.
	((centerX, centerY), radius) = cv2.minEnclosingCircle(c)
	# Using the (x, y) coordinates and the radius, we can draw
	# a circle on our mask, representing the coin.
	cv2.circle(mask, (int(centerX), int(centerY)), int(radius), 255, -1)
	cv2.imshow("Mask", mask)
	mask = mask[y:y + h, x:x + w]
	# In order to show only the foreground of the coin and ignore
	# the background, we make a call to our trusty bitwise
	# AND function using the coin image and the mask for the
	# coin. The coin, with the background removed,
	cv2.imshow("Masked Coin", cv2.bitwise_and(coin, coin, mask=mask))
	cv2.waitKey(0)
