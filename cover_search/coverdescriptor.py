# -*- coding: utf-8 -*-
# @Author:   MR_Radish
# @Date:     2018-08-29 18:21:04
# @E-mail:   ty_2016@foxmail.com
# @FileName: coverdescriptor.py
# @TODO: extract keypoints and local invariant descriptors from the images

import numpy as np
import cv2

class CoverDescriptor:

	def __init__(self, useSIFT = False):
		self.useSIFT = useSIFT

	def describe(self, image):

		if self.useSIFT:
			descriptor = cv2.xfeatures2d.SIFT_create()
		else:
			descriptor = cv2.BRISK_create()
		# This method both detects keypoints (i.e., “interesting” regions of an image)
		# and then describes and quantifies the region surrounding each of the keypoints.
		# Thus, the keypoint detection is the “detect” phase, whereas the
		# actual description of the region is the “compute” phase.
		(kps, descs) = descriptor.detectAndCompute(image, None)
		# the (x, y) coordinates of the keypoint, contained in the pt attribute.
		kps = np.float32([kp.pt for kp in kps])

		return (kps, descs)

