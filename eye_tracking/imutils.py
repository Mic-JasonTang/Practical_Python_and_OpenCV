# -*- coding: utf-8 -*-
# @Author:   MR_Radish
# @Date:     2018-07-24 11:18:50
# @E-mail:   ty_2016@foxmail.com
# @FileName: imutils.py
# @TODO: imutils, it’s a library that
# we are going to write ourselves and create “convenience”
# methods to do common tasks like translation, rotation, and
# resizing.It made by myself

import numpy as np
import cv2

def translate(image, tx, ty):
	M = np.float32([[1, 0, tx], [0, 1, ty]])
	shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
	return shifted

def rotate(image, angle, center=None, scale=1.0):
	(h, w) = image.shape[:2]

	if center is None:
		# 在图像数组image中是按w、h来存的，所以这里的顺序是这样。
		center = (w // 2, h // 2)

	M = cv2.getRotationMatrix2D(center, angle, scale)
	rotated = cv2.warpAffine(image, M, (w, h))
	return rotated

def resize(image, width = None, height = None, inter = cv2.INTER_AREA):
	dim = None
	(h, w) = image.shape[:2]

	if width is None and height is None:
		return image

	# 宽度是None，说明指定了高度
	if width is None:
		r = height / h
		dim = (int(w * r), height)

	# 高度是None，说明指定了宽度
	if height is None:
		r = width / w
		dim = (width, int(h * r))

	resized = cv2.resize(image, dim, interpolation=inter)
	return resized
