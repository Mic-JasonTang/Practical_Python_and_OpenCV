# -*- coding: utf-8 -*-
# @Author:   MR_Radish
# @Date:     2018-08-25 20:13:17
# @E-mail:   ty_2016@foxmail.com
# @FileName: track.py
# @TODO: 目标追踪(按照颜色)

import numpy as np
import argparse
import time
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video",
	help="path to the (optional) video file")
args = vars(ap.parse_args())

# Limit of the shades of blue in RGB color space.
# Define colors as "blue" if they are greater than R = 0,
# G = 67, B = 100 and less than R = 50, G = 128, B = 255.
# API: http://www.atool.org/colorpicker.php?
blueLower = np.array([100, 67, 0], dtype="uint8") # 颜色:#004364
blueUpper = np.array([255, 128, 50], dtype="uint8") # 颜色"#3280ff
camera = cv2.VideoCapture(args["video"])

while True:
	# A call to the read() method of camera grabs the next frame in the video.
	# The first, grabbed, is a boolean indicating whether or not
	# the frame was successfully read from the video file.
	# The second, frame, is the frame itself.
	(grabbed, frame) = camera.read()
	print(frame.shape)
	# reached the end of the video.
	if not grabbed:
		break

	# The first is the frame that she wants to check.
	# The second is the lower threshold on RGB pixels.
	# The third is the upper threshold.

	# The result of calling this function is a thresholded image, with pixels
	# falling [within the upper and lower range] set to white and
	# pixels that [do not fall into this range] set as black.
	blue = cv2.inRange(frame, blueLower, blueUpper)

	# To make finding contours more accurate.
	blue = cv2.GaussianBlur(blue, (3, 3), 0)

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

	# Return Parameter:
	# after_detection: our image after applying contour detection.
	# cnts: the contours themselves. the type is list.
	# hierarchy: hierarchy(层级) of contours.

	(_, cnts, _) = cv2.findContours(blue.copy(),
		                            cv2.RETR_EXTERNAL,
		                            cv2.CHAIN_APPROX_SIMPLE)

	if len(cnts) > 0:
		# Need to find the largest contour.
		# The contours are sorted in reverse order (largest first), using
		# the cv2.contourArea function to compute the area of the contour.
		# Grabed the contour with the largest area.
		cnt = sorted(cnts, key=cv2.contourArea, reverse=True)[0]

		# Now has the outline of the iPhone, but she needs to draw a bounding box around it.
		# Calling cv2.minAreaRect computes the minimum bounding box around the contour.
		# Then, cv2.boxPoints re-shapes the bounding box to be a list of points.
		rect = np.int32(cv2.boxPoints(cv2.minAreaRect(cnt)))
		# Draws the bounding box using the cv2.drawContours function.
		cv2.drawContours(frame, [rect], -1, (0, 255, 0), 2)

	cv2.imshow("Tracking", frame)
	cv2.imshow("Binary", blue)

	time.sleep(0.025)

	if cv2.waitKey(1) == ord("q"):
		break

camera.release()
cv2.destroyAllWindows()
