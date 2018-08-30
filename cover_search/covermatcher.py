# -*- coding: utf-8 -*-
# @Author:   MR_Radish
# @Date:     2018-08-30 10:46:09
# @E-mail:   ty_2016@foxmail.com
# @FileName: covermatcher.py
# @TODO: Extracted keypoints and descriptors from the covers of books.
# Determine how well two book covers “match.”

import numpy as np
import cv2

class CoverMatcher:

	# The three optional arguments are detailed below:
	# • ratio: The ratio of nearest neighbor distances suggested by Lowe to
	# prune down the number of keypoints a homography needs to be computed for.
	# • minMatches: The minimum number of matches required for a homography
	# to be calculated.
	# • useHamming: A boolean indicating whether the Hamming or Euclidean
	# distance should be used to compare feature vectors.
	def __init__(self, descriptor, coverPaths, ratio = 0.7,
		minMatches = 40, useHamming = True):
		self.descriptor = descriptor
		self.coverPaths = coverPaths
		self.ratio = ratio
		self.minMatches = minMatches
		self.distanceMethod = "BruteForce"

		# When comparing realvalued descriptors, like SIFT or SURF, we would
		# want to use the Euclidean distance. However, if we are using BRISK
		# features which produce binary feature vectors, the Hamming
		# distance should be used instead.
		if useHamming:
			# BRISK features which produce binary feature vectors, he’ll
			# indicate that the Hamming method should be used
			self.distanceMethod += "-Hamming"

	# the set of keypoints and descriptors extracted from the query image.
	def search(self, queryKps, queryDescs):
		results = {}

		for coverPath in self.coverPaths:
			cover = cv2.imread(coverPath)
			gray = cv2.cvtColor(cover, cv2.COLOR_BGR2GRAY)
			(kps, descs) = self.descriptor.describe(gray)

			# The number of matched keypoints is then determined
			# using the match method and updated the results dictionary.
			score = self.match(queryKps, queryDescs, kps, descs)
			results[coverPath] = score

		# Do a quick check to make sure that at least some results exist.
		if len(results) > 0:
			# The results are sorted in descending order, with book covers with
			# more keypoint matches placed at the top of the list.
			results = sorted([(v, k) for (k, v) in results.items() if v > 0],
				reverse = True)

		return results

	# How to matche keypoints and descriptors.
	# • kpsA: The list of keypoints associated with the first
	# image to be matched.
	# • featuresA: The list of feature vectors associated with
	# the first image to be matched.
	# • kpsB: The list of keypoints associated with the second
	# image to be matched.
	# • featuresB: The list of feature vectors associated with
	# the second image to be matched.
	def match(self, kpsA, featuresA, kpsB, featuresB):
		# Using the cv2.DescriptorMatcher_create function either be BruteForce
		# or BruteForce-Hamming, indicating that he is going to compare
		# every descriptor in featuresA to every descriptor in featuresB
		# using either the Euclidean or Hamming distance.
		matcher = cv2.DescriptorMatcher_create(self.distanceMethod)
		# The actual matching is performed using the knnMatch function of matcher.
		# The “kNN” portion of the function stands for “k-Nearest-Neighbor,”
		# where the “nearest neighbors” are defined by the smallest Euclidean
		# distance between feature vectors.
		# The two feature vectors with the smallest Euclidean distance are
		# considered to be “neighbors”. Both featuresA and featuresB are passed
		# into the knnMatch function, with a third parameter of 2, indicating
		# that wants to find the two nearest neighbors for each feature vector.
		# The output of the knnMatch method is stored in rawMatches.
		# However, these are not the actual mapped keypoints!
		# API:https://docs.opencv.org/master/db/d39/classcv_1_1DescriptorMatcher.html#a378f35c9b1a5dfa4022839a45cdf0e89
		rawMatches = matcher.knnMatch(featuresB, featuresA, 2)
		# print("rawMatches:{}".format(rawMatches))
		# Initialize the list of actual matches.
		matches = []

		for m in rawMatches:
			# The first is that there are indeed two matches. The second
			# is to apply David Lowe’s ratio test, by ensuring the distance
			# between the first match is less than the distance of the second
			# match, times the supplied ratio.
			# This test helps remove false matches and prunes down the number of
			# keypoints the homography needs to be computed for, thus speeding up
			# the entire process.
			if len(m) == 2 and m[0].distance < m[1].distance * self.ratio:
				# the matches list is updated with a tuple of the index of the
				# first keypoint and the index of the second keypoint.
				matches.append((m[0].trainIdx, m[0].queryIdx))
				# print("m[0].trainIdx:{}, m[0].queryIdx:{}".format(m[0].trainIdx, m[0].queryIdx))

		# Ensures that the number of matches is at least the number of minimum matches.
		# If there are not enough matches, it is not worth computing the
		# homography since the two images (likely) do not contain the same book cover.
		if len(matches) > self.minMatches:
			# Defines two lists, ptsA and ptsB to store the (x, y) coordinates
			# for each set of matched keypoints.
			ptsA = np.float32([kpsA[i] for (i, _) in matches])
			ptsB = np.float32([kpsB[j] for (_, j) in matches])
			# Compute the homography, which is a mapping between the two keypoint
			# planes with the same center of projection.
			# Uses the cv2.findHomography function and the RANSAC algorithm,
			# which stands for Random Sample Consensus.

			# The first two are ptsA and ptsB, the (x, y) coordinates of the potential matches.
			# The third argument is the homography method. In this case,
			# passes in cv2.RANSAC to indicate that he wants to use the RANSAC algorithm.
			# The final parameter is the RANSAC re-projection threshold,
			# which allows for some “wiggle room” between keypoints.
			# Assuming that the (x, y) coordinates for ptsA and ptsB are measured
			# in pixels, Gregory passes in a value 4.0 to indicate that an error
			# of 4.0 pixels will be tolerated for any pair of keypoints to be considered an inlier.
			# The cv2.findHomograpy function returns a tuple of two
			# values. The first is the transformation matrix,the second
			# returned value, the status variable is a list of booleans, with a
			# value of 1 if the corresponding keypoints in ptsA and ptsB
			# were matched, and a value of 0 if they were not.
			(_, status) = cv2.findHomography(ptsA, ptsB, cv2.RANSAC, 4.0)
			# Computes the ratio of the number of inliers to the total number
			# of potential matches and returns it to the caller.
			# A high score indicates a better “match” between two images.
			return float(status.sum()) / status.size
		# if the minimum number of matches test on Line 106 failed, then returns
		# a value of -1.0, indicating that the number of inliers could not be computed.
		return -1.0
