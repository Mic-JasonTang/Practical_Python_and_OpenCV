# -*- coding: utf-8 -*-
# @Author:   MR_Radish
# @Date:     2018-08-30 15:50:47
# @E-mail:   ty_2016@foxmail.com
# @FileName: search.py
# @TODO:
# CoverDescriptor will extract keypoints and
# local invariant descriptors from the images
from coverdescriptor import CoverDescriptor
# CoverMatcher will determine how well two book covers “match.”
from covermatcher import CoverMatcher
import argparse
import glob
import csv
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-d", "--db", required=True,
	help="path to the book database")
ap.add_argument("-c", "--covers", required=True,
	help="path to the director that contains our book covers")
ap.add_argument("-q", "--query", required=True,
	help="path to the query book cover")
ap.add_argument("-s", "--sift", type=int, default=0,
	help="whether or not SIFT should be used")
args = vars(ap.parse_args())

db = {}

for l in csv.reader(open(args['db'])):
	# The db dictionary is updated with the unique filename of the book
	# as the key and the title of the book and author as the value.
	db[l[0]] = l[1:]

useSIFT = args["sift"] > 0
# Determine whether or not the Hamming distance should be used.
# If we are using the SIFT algorithm, then we’ll be extracting real-valued
# feature vectors – thus the Euclidean distance should be used. However,
# if we are using the BRISK algorithm, then we’ll be computing binary feature
# vectors, and the Hamming distance should be used instead.
useHamming = args["sift"] == 0
ratio = 0.7
minMatches = 40
# In the case that we are using the SIFT algorithm we, we’ll add the extra
# constraint that more matches should be found to ensure a more accurate book
# cover identification.
if useSIFT:
	minMatches = 50

cd = CoverDescriptor(useSIFT = useSIFT)
cm = CoverMatcher(cd, glob.glob(args["covers"] + "/*.png"),
	ratio = ratio, minMatches = minMatches, useHamming = useHamming)

queryImage = cv2.imread(args["query"])
gray = cv2.cvtColor(queryImage, cv2.COLOR_BGR2GRAY)
(queryKps, queryDescs) = cd.describe(gray)
print("queryKps:{}".format(queryKps))
print("len(queryKps):{}".format(len(queryKps)))
print("queryDescs:{}".format(queryDescs))
print("len(queryDescs):{}".format(len(queryDescs)))
results = cm.search(queryKps, queryDescs)

cv2.imshow("Query", queryImage)

if len(results) == 0:
	print("I could not find a match for that cover!")
	cv2.wait(0)
else:
	for (i, (score, coverPath)) in enumerate(results):
		print("coverPath:{}".format(coverPath))
		(author, title) = db[coverPath[coverPath.rfind("\\") + 1:]]
		print("{}. {:.2f}% : {} - {}".format(i + 1, score * 100, author, title))

		result = cv2.imread(coverPath)
		cv2.imshow("Result", result)
		cv2.waitKey(0)

