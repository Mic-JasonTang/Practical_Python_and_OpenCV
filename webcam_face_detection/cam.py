# -*- coding: utf-8 -*-
# @Author:   MR_Radish
# @Date:     2018-08-25 10:31:20
# @E-mail:   ty_2016@foxmail.com
# @FileName: cam.py
# @TODO:

from facedetector import FaceDetector
import imutils
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-f", "--face", required=True,
	help="path to the face cascade resides")
ap.add_argument("-v", "--video",
	help="path to the (optional) video file")
args = vars(ap.parse_args())

fd = FaceDetector(args["face"])

# API: https://docs.opencv.org/3.0-beta/modules/videoio/doc/reading_and_writing_video.html?highlight=videocapture
if not args.get("video", False):
	# Param1: filename – name of the opened video file (eg. video.avi) or
	# image sequence (eg. img_%02d.jpg, which will read samples like img_00.jpg,
	#  img_01.jpg, img_02.jpg, ...)
	# Param2: device – id of the opened video capturing device (i.e. a camera index).
	# If there is a single camera connected, just pass 0.
	camera = cv2.VideoCapture(0)
	if not camera.isOpened():
		raise ValueError("camera not found!")
else:
	camera = cv2.VideoCapture(args["video"])

while True:
	# return false if no frame has been grabbed.
	(grabbed, frame) = camera.read()
	# if the frame was not grabbed, then the video is over.
	if args.get("video") and not grabbed:
		break

	frame = imutils.resize(frame, width = 300)
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	faceRects = fd.detect(gray, scaleFactor=1.1)
	frameClone = frame.copy()

	for (fX, fY, fW, fH) in faceRects:
		cv2.rectangle(frameClone, (fX, fY), (fX + fW, fY + fH),
			(0, 255, 0), 2)
	cv2.imshow("Face", frameClone)

	# 按q键退出,ord()返回字符的ascii码
	if cv2.waitKey(30) == ord("q"):
		break

camera.release()
cv2.destroyAllWindows()
