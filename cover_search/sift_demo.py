# -*- coding: utf-8 -*-
# @Author:   MR_Radish
# @Date:     2018-08-31 10:00:09
# @E-mail:   ty_2016@foxmail.com
# @FileName: sift_demo.py
# @TODO: sift_demo
# https://blog.csdn.net/zhangziju/article/details/79754652
import numpy as np
import argparse
import glob
import csv
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-a", "--imageA", required=True,
	help="path to the imageA")
ap.add_argument("-b", "--imageB", required=True,
	help="path to the imageB")
ap.add_argument("-s", "--sift", type=int, default=0,
	help="whether or not SIFT should be used")
args = vars(ap.parse_args())

useSIFT = args["sift"] > 0

useHamming = args["sift"] == 0
ratio = 0.75
minMatches = 40

if useSIFT:
	minMatches = 50

distanceMethod = "BruteForce"

if useHamming:
	distanceMethod += "-Hamming"

if useSIFT:
	descriptor = cv2.xfeatures2d.SIFT_create()
else:
	descriptor = cv2.BRISK_create()

imageA = cv2.imread(args["imageA"])
imageA = cv2.resize(imageA, (640, 480))
gray1 = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
(kpsA, descsA) = descriptor.detectAndCompute(gray1, None)

gray1 = cv2.drawKeypoints(imageA, kpsA, imageA)
cv2.imshow(str(gray1.shape), gray1) #拼接显示为gray
cv2.waitKey(0)

imageB = cv2.imread(args["imageB"])
imageB = cv2.resize(imageB, (640, 480))
gray2 = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)
(kpsB, descsB) = descriptor.detectAndCompute(gray2, None)

gray2 = cv2.drawKeypoints(imageB, kpsB, imageB)
cv2.imshow(str(gray2.shape), gray2)
cv2.waitKey(0)


matcher = cv2.DescriptorMatcher_create(distanceMethod)
rawMatches = matcher.knnMatch(descsB, descsA, 2)

matches = []

for m in rawMatches:
	if not (len(m) == 2 and m[0].distance < m[1].distance * ratio):
		# matches.append((m[0].trainIdx, m[0].queryIdx))
		matches.append([m[0]])
		# rawMatches.remove(m)

# kpsA2 = kpsA.copy()
# kpsB2 = kpsB.copy()
# kpsA2 = np.float32([kp.pt for kp in kpsA2])
# kpsB2 = np.float32([kp.pt for kp in kpsB2])

# if len(matches) > minMatches:
# 	ptsA = np.float32([kpsA2[i] for (i, _) in matches])
# 	ptsB = np.float32([kpsB2[j] for (_, j) in matches])
# 	(matrix, status) = cv2.findHomography(ptsA, ptsB, cv2.RANSAC, 4.0)

# score = float(status.sum()) / status.size
# print("matrix:{}".format(matrix))
# if score < 0:
	# print("match failed!")
# else:
result = cv2.drawMatchesKnn(imageA, kpsA, imageB, kpsB, matches, None, flags=2)

cv2.imshow("Result", result)

cv2.waitKey(0)
cv2.destroyAllWindows()
