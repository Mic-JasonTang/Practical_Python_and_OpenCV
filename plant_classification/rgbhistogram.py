# -*- coding: utf-8 -*-
# @Author:   MR_Radish
# @Date:     2018-08-28 16:45:08
# @E-mail:   ty_2016@foxmail.com
# @FileName: rgbhistogram.py
# @TODO: image descriptor

import cv2

class RGBHistogram:

	def __init__(self, bins):
		self.bins = bins

	# an image that the color histogram will be built from, and an optional
	# mask. If Charles supplies a mask, then only pixels associated
	# with the masked region will be used in constructing the histogram.
	# This allows him to describe only the petals of the
	# image, ignoring the rest of the image
	def describe(self, image, mask = None):
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
		hist = cv2.calcHist([image], [0, 1, 2],
			mask, self.bins, [0, 256, 0, 256, 0, 256])
		# Normalize the histogram within the function and updates
		# the second parameter (i.e., the “output”) passed in.
		cv2.normalize(hist, hist)

		return hist.flatten()
