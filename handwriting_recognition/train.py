# -*- coding: utf-8 -*-
# @Author:   MR_Radish
# @Date:     2018-08-27 10:43:46
# @E-mail:   ty_2016@foxmail.com
# @FileName: train.py
# @TODO: create a model to recognize digits.

# joblib will be used to dump the trained model to file.
from sklearn.externals import joblib
# SVC: 支持向量分类
from sklearn.svm import LinearSVC
from hog import HOG
import argparse
import dataset

ap = argparse.ArgumentParser()
ap.add_argument("-d", "--dataset", required=True,
	help="path to the dataset file")
ap.add_argument("-m", "--model", required=True,
	help="path to where the model will be stored")
args = vars(ap.parse_args())

(digits, target) = dataset.load_digits(args["dataset"])
data = []

# Using 18 orientations for the gradient magnitude histogram,
# 10 pixels for each cell, and 1 cell per block.
# By setting transform = True, indicates that the square-root
# of the pixel intensities will be computed prior to creating
# the histograms.
hog = HOG(orientations=18, pixelsPerCell=(10, 10),
	cellsPerBlock=(1, 1), transform=True)

for image in digits:
	image = dataset.deskew(image, 20)
	image = dataset.center_extent(image, (20, 20))

	hist = hog.describe(image)
	data.append(hist)

model = LinearSVC(random_state = 42)
model.fit(data, target)

joblib.dump(model, args["model"])

print("train has done!")
