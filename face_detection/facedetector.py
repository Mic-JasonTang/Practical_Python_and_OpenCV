# -*- coding: utf-8 -*-
# @Author:   MR_Radish
# @Date:     2018-08-24 16:30:05
# @E-mail:   ty_2016@foxmail.com
# @FileName: facedetector.py
# @TODO: 人脸检测工具

import cv2

class FaceDetector:
	# 官方文档:https://docs.opencv.org/3.0-beta/modules/objdetect/doc/cascade_classification.html
	def __init__(self, faceCascadePath):
		# the path to where his cascade classifier lives
		# This classifier is serialized as an XML file.
		# Making a call to cv2.CascadeClassifier will deserialize
		# the classifier, load it into memory, and allow him to detect
		# faces in images.
		self.faceCascade = cv2.CascadeClassifier(faceCascadePath)

	# scaleFactor: How much the image size is reduced at
	# each image scale. This value is used to create the scale
	# pyramid in order to detect faces at multiple scales
	# in the image (some faces may be closer to the foreground,
	# and thus be larger; other faces may be smaller
	# and in the background, thus the usage of varying
	# scales). A value of 1.05 indicates that Jeremy is reducing the
	# size of the image by 5% at each level in the pyramid. (参数必须>1)
	# minNeighbors: How many neighbors each window
	# should have for the area in the window to be considered a face.
	# The cascade classifier will detect multiple
	# windows around a face. This parameter controls how
	# many rectangles (neighbors) need to be detected for
	# the window to be labeled a face.
	# minSize: A tuple of width and height (in pixels) indicating the minimum size
	# of the window. Boundingboxes smaller than this size are ignored. It is a good
	# idea to start with (30, 30) and fine-tune from there.
	def detect(self, image, scaleFactor = 1.2, minNeighbors = 5,
				minSize = (30, 30)):
		# Detecting the actual faces in the image
		rects = self.faceCascade.detectMultiScale(image, scaleFactor = scaleFactor,
			    minNeighbors = minNeighbors, minSize = minSize,
			    flags=cv2.CASCADE_SCALE_IMAGE)
		# returns rects, a list of tuples containing
		# the bounding boxes of the faces in the image.
		return rects
