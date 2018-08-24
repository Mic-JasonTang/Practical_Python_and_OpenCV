# -*- coding: utf-8 -*-
# @Author:   MR_Radish
# @Date:     2018-08-19 22:22:51
# @E-mail:   ty_2016@foxmail.com
# @FileName: detect_faces.py
# @TODO: 人脸检测


import cv2
import argparse
from facedetector import FaceDetector

ap = argparse.ArgumentParser()
ap.add_argument("-f", "--face", required=True,
	help="path to where the face cascade resides")
ap.add_argument("-i", "--image", required=True,
	help="path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

fd = FaceDetector(args["face"])
faceRects = fd.detect(gray, scaleFactor = 1.2, minNeighbors = 5,
					 minSize = (30, 30))
print("I found {} face(s)".format(len(faceRects)))

for (x, y, w, h) in faceRects:
	cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

cv2.imshow("Faces", image)
cv2.waitKey(0)
