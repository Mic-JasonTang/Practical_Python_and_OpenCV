# -*- coding: utf-8 -*-
# @Author:   MR_Radish
# @Date:     2018-08-25 20:13:17
# @E-mail:   ty_2016@foxmail.com
# @FileName: track.py
# @TODO: 目标追踪

import numpy as np
import argparse
import time
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video",
	help="path to the (optional) video file")
args = vars(ap.parse_args())

blueLower = np.array([100, 67, 0], dtype="uint8")
blueUpper = np.array([255, 128, 50], dtype="uint8")

camera = cv2.VideoCapture(args["video"])

