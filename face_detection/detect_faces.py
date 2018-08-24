# -*- coding: utf-8 -*-
# @Author:   MR_Radish
# @Date:     2018-08-19 22:22:51
# @E-mail:   ty_2016@foxmail.com
# @FileName: detect_faces.py
# @TODO: 人脸检测


import cv2
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-f", "--face", required=True,
	help="path to where the face cascade resides")
ap.add_argument("-i", "--image", required=True,
	help="path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
