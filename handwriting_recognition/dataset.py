# -*- coding: utf-8 -*-
# @Author:   MR_Radish
# @Date:     2018-08-26 23:50:25
# @E-mail:   ty_2016@foxmail.com
# @FileName: dataset.py
# @TODO: define some methods to help manipulate and
# prepare the dataset for feature extraction and training model.

import imutils
import numpy as np
import mahotas
import cv2

def load_digits(datasetPath):
	data = np.genfromtxt(datasetPath, delimiter=",",
		dtype="uint8")
	traget = data[:, 0]
	data = data[:, 1:].reshape(data.shape[0], 28, 28)

	return (data, traget)

