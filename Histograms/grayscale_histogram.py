# -*- coding: utf-8 -*-
# @Author:   MR_Radish
# @Date:     2018-07-26 15:31:24
# @E-mail:   ty_2016@foxmail.com
# @FileName: grayscale_histogram.py
# @TODO: 灰度图计算直方图

from matplotlib import pyplot as plt
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])

image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Original", image)

# param1:images: This is the image that we want to compute a
			# histogram for. Wrap it as a list: [myImage].
# param2:channels: This is a list of indexes, where we specify
			# the index of the channel we want to compute a histogram for. To compute
			# a histogram of a grayscale
			# image, the list would be [0]. To compute a histogram
			# for all three red, green, and blue channels, the channels list would be [0,1,2]
# param3:mask:If a mask is
			# provided, a histogram will be computed for masked
			# pixels only.
# param4:histSize: This is the number of bins we want to use
			# when computing a histogram. Again, this is a list, one
			# for each channel we are computing a histogram for.
			# The bin sizes do not all have to be the same. Here is
			# an example of 32 bins for each channel: [32,32,32].
# param5:ranges: Here we specify The range of possible pixel
			# values. Normally, this is [0, 256] for each channel, but
			# if you are using a color space other than RGB (such as
			# HSV), the ranges might be different.
hist = cv2.calcHist([image], [0], None, [256], [0, 256])

plt.figure()
plt.title("Grayscale Histogram")
plt.xlabel("Bins")
plt.ylabel("# of Pixels")
plt.plot(hist)
plt.show()
cv2.waitKey(0)
