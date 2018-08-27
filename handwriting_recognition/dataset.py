# -*- coding: utf-8 -*-
# @Author:   MR_Radish
# @Date:     2018-08-26 23:50:25
# @E-mail:   ty_2016@foxmail.com
# @FileName: dataset.py
# @TODO: define some methods to help manipulate and
# prepare the dataset for feature extraction and training model.

import imutils
import numpy as np
# mahotas: another computer vision library to aid cv2
import mahotas
import cv2

# datasetPath: The path to where the MNIST sample dataset resides on disk.
def load_digits(datasetPath):
	data = np.genfromtxt(datasetPath, delimiter=",",
		dtype="uint8")
	# 第一列是label
	traget = data[:, 0]
	# 其余的是数字图片
	data = data[:, 1:].reshape(data.shape[0], 28, 28)

	return (data, traget)

# Perform some preprocessing on the digit images.
# deskew: 偏移校正
def deskew(image, width):
	# Grabs the height and width of the image.
	(h, w) = image.shape[:2]
	# 计算图片的矩,矩包含一些统计信息,白色像素在图片中的位置分布.
	moments = cv2.moments(image)

	# 利用moment计算skew
	skew = moments["mu11"] / moments["mu02"]
	# This matrix M will be used to deskew the image.
	M = np.float32([
		[1, skew, -0.5 * w * skew],
		[0, 1, 0]])
	# The first argument is the image that is going to be skewed.
	# The second is the matrix M that defines the “direction” in which
	# the image is going to be deskewed.
	# The third parameter is the resulting width and height of the deskewed image.
	# The flags parameter controls how the image is going to be deskewed.
	image = cv2.warpAffine(image, M, (w, h),
		flags = cv2.WARP_INVERSE_MAP | cv2.INTER_LINEAR)

	image = imutils.resize(image, width = width)

	return image

# With the digit placed at the center of the image, then needs
# to define the extent of an image.
# The first is the deskewed image and
# the second is the output size of the image
def center_extent(image, size):
	(eW, eH) = size

	# checks to see if the width is greater than the
	# height of the image. If this is the case, the image is resized
	# based on its width.
	if image.shape[1] > image.shape[0]:
		image = imutils.resize(image, width = eW)

	else:
		image = imutils.resize(image, height = eH)

	extent = np.zeros((eH, eW), dtype = "uint8")
	# These offsets indicate the starting (x, y) coordinates
	# (in y, x order) of where the image will be placed in the extent.
	offsetX = (eW - image.shape[1]) // 2
	offsetY = (eH - image.shape[0]) // 2
	extent[offsetY: offsetY + image.shape[0], offsetX:
		 offsetX + image.shape[1]] = image

	# Computes the weighted mean of the white pixels in
	# the image using the center_of_mass function of the mahotas
	# package. This function returns the weighted (x, y) coordinates
	# of the center of the image. Then converts these
	# (x, y) coordinates to integers rather than floats.
	CM = mahotas.center_of_mass(extent)
	(cY, cX) = np.round(CM).astype("int32")
	# then translates the digit so that it is placed at
	# the center of the image.
	(dX, dY) = ((size[0] // 2) - cX, (size[1] // 2) - cY)
	# 平移矩阵
	M = np.float32([[1, 0, dX], [0, 1, dY]])
	# 通过平移让数字在图像的中间
	extent = cv2.warpAffine(extent, M, size)

	return extent
