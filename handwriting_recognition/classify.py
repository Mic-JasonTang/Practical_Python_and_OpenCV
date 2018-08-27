# -*- coding: utf-8 -*-
# @Author:   MR_Radish
# @Date:     2018-08-27 20:36:09
# @E-mail:   ty_2016@foxmail.com
# @FileName: classify.py
# @TODO: 使用训练好的模型

from sklearn.externals import joblib
from hog import HOG
import dataset
import argparse
import mahotas
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-m", "--model", required=True,
	help="path to where the model will be stored")
ap.add_argument("-i", "--image", required=True,
	help="path to the image file")
args = vars(ap.parse_args())

model = joblib.load(args["model"])

hog = HOG(orientations = 18, pixelsPerCell=(10, 10),
	cellsPerBlock=(1, 1), transform=True)

image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

blurred = cv2.GaussianBlur(gray, (5, 5), 0)
edged = cv2.Canny(blurred, 30, 150)
(_, cnts, _) = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL,
	cv2.CHAIN_APPROX_SIMPLE)

# Finds contours in the edged image and sorts
# them from left to right. Each of these contours represents a
# digit in an image that needs to be classified.
# cv2.boundingRect():返回矩形的x,y,w,h
# 这里根据x来进行排序,即从左到右
cnts = sorted([(c, cv2.boundingRect(c)[0]) for c in cnts], key = lambda x: x[1])

for (c, _) in cnts:
	# using the cv2.boundingRect function, which returns the
	# starting (x, y) coordinates of the bounding box, followed by
	# the width and height of the box.
	(x, y, w, h) = cv2.boundingRect(c)

	# Checks the width and height of the bounding
	# box to ensure it is at least seven pixels wide and
	# twenty pixels tall. If the bounding box region does not meet
	# these dimensions, then it is considered to be too small to be
	# a digit.
	if w >= 7 and h >= 20:
		# The Region of Interest (ROI) is extracted from the
		# grayscale image using NumPy array slices
		roi = gray[y:y + h, x: x + w]
		thresh = roi.copy()
		# The first is to apply Otsu’s thresholding method to segment
		# the foreground (the digit) from the background
		# (the paper the digit was written on).
		T = mahotas.thresholding.otsu(roi)
		thresh[thresh > T] = 255
		thresh = cv2.bitwise_not(thresh)
		# The digit is then deskewed and translated to the center of the image.
		thresh = dataset.deskew(thresh, 20)
		thresh = dataset.center_extent(thresh, (20, 20))

		cv2.imshow("thresh", thresh)
		# Computes the HOG feature vector of the thresholded ROI by calling
		# the describe method of the HOG descriptor.
		hist = hog.describe(thresh)
		# The HOG feature vector is fed into the LinearSVC’s predict
		# method which classifies which digit the ROI is, based on
		# the HOG feature vector.
		digit = model.predict([hist])[0]
		print("I think that number is: {}".format(digit))

		# The first calls the cv2.rectangle function to draw a green
		# rectangle around the current digit ROI
		cv2.rectangle(image, (x, y), (x + w, y + h),
			(0, 255, 0), 1)
		# Using the cv2.putText method to draw the
		# digit itself on the original image.
		# The first argument to the cv2.putText function is the image that
		# wants to draw on.
		# The second argument is the string containing what he wants to draw.
		# The third (x, y) coordinates of where the text will be drawn.
		# (x-10, y-10)相当于是向左上移动了
		# The fourth argument is a built-in OpenCV constant used
		# to define what font will be used to draw the text.
		# The fifth argument is the relative size of the text, the sixth the color
		# of the text (green), and the final argument is the thickness
		# of the text (two pixels).
		cv2.putText(image, str(digit), (x - 10, y - 10),
			cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 0), 2)
		cv2.imshow("image", image)
		cv2.waitKey(0)

