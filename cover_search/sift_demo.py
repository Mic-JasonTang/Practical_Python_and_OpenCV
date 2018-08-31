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

def imresize(src, height):
    ratio = src.shape[0] * 1.0/height
    width = int(src.shape[1] * 1.0/ratio)
    return cv2.resize(src, (width, height))

ap = argparse.ArgumentParser()
ap.add_argument("-a", "--imageA", required=True,
	help="path to the imageA")
ap.add_argument("-b", "--imageB", required=True,
	help="path to the imageB")
ap.add_argument("-m", "--method", default="sift",
	help="which method should be used")
# ap.add_argument("-r", "--resize", default=0,
# 	help="resize the image to keep the size of two images are same")
args = vars(ap.parse_args())

ratio = 0.6

distanceMethod = "BruteForce"

method = args["method"]
# resize = args["resize"]

print("use {} method".format(method))

if method == "sift":
	descriptor = cv2.xfeatures2d.SIFT_create()
elif method == "brisk":
	descriptor = cv2.BRISK_create()
elif method == "surf":
	descriptor = cv2.xfeatures2d.SURF_create()
elif method == "orb":
	descriptor = cv2.ORB_create()
else:
	raise ValueError("The {} method is not supported.".format(method))

imageA = cv2.imread(args["imageA"])
print("image.shape:{}".format(imageA.shape))
imageA = imresize(imageA, 480)
gray1 = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
(kpsA, descsA) = descriptor.detectAndCompute(gray1, None)

gray1 = cv2.drawKeypoints(imageA, kpsA, imageA)
cv2.imshow(str(gray1.shape) + "A", gray1) #拼接显示为gray
cv2.waitKey(0)

imageB = cv2.imread(args["imageB"])
print("image.shape:{}".format(imageB.shape))
imageB = imresize(imageB, 480)
gray2 = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)
(kpsB, descsB) = descriptor.detectAndCompute(gray2, None)

gray2 = cv2.drawKeypoints(imageB, kpsB, imageB)
cv2.imshow(str(gray2.shape) + "B", gray2)
cv2.waitKey(0)

if method == "brisk" or method == "orb":
	matcher = cv2.DescriptorMatcher_create(distanceMethod)
	rawMatches = matcher.knnMatch(descsB, descsA, 2)
else:
	# FLANN 参数设计
	FLANN_INDEX_KDTREE = 0
	index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
	search_params = dict(checks=50)
	flann = cv2.FlannBasedMatcher(index_params, search_params)
	rawMatches = flann.knnMatch(descsB, descsA, 2)

matches = []

for m, n in rawMatches:
	if m.distance < n.distance * ratio:
		matches.append([m])

print("I got {} matches.".format(len(matches)))
result = cv2.drawMatchesKnn(imageA, kpsA, imageB, kpsB, matches, None)

cv2.imshow(str(method), result)

cv2.waitKey(0)
cv2.destroyAllWindows()
