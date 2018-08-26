# -*- coding: utf-8 -*-
# @Author:   MR_Radish
# @Date:     2018-08-26 16:33:25
# @E-mail:   ty_2016@foxmail.com
# @FileName: eyetracking.py
# @TODO: 眼睛追踪

from eyetracker import EyeTracker
import imutils
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-f", "--face", required=True,
	help="path to where the face cascade resides")
ap.add_argument("-e", "--eye", required=True,
	help="path to where the eye cascade resides")
ap.add_argument("-v", "--video",
	help="path to the (optional) video file")
args = vars(ap.parse_args())

et = EyeTracker(args["face"], args["eye"])

if not args.get("video", False):
	camera = cv2.VideoCapture(0)

	if not camera.isOpened():
		raise ValueError("camera not found！")
else:
	camera = cv2.VideoCapture(args["video"])

while True:
	(grabbed, frame) = camera.read()

	# if video is available then break if not grabbed frame.
	if args.get("video") and not grabbed:
		break
	# In order to make face and eye detection faster, Laura first
	# resizes the image to have a width of 300 pixels
	frame = imutils.resize(frame, width=300)
	# Converting to grayscale tends to increase the
	# accuracy of the cascade classifiers.
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	rects = et.track(gray)

	for rect in rects:
		cv2.rectangle(frame, (rect[0], rect[1]),
			(rect[2], rect[3]), (0, 255, 0), 2)

	cv2.imshow("Tracking", frame)

	if cv2.waitKey(20) == ord("q"):
		break

camera.release()
cv2.destroyAllWindows()
