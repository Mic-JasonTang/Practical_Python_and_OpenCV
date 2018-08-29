# -*- coding: utf-8 -*-
# @Author:   MR_Radish
# @Date:     2018-08-28 21:51:40
# @E-mail:   ty_2016@foxmail.com
# @FileName: classify.py
# @TODO: classify what species a given flower is

from rgbhistogram import RGBHistogram
# LabelEncoder: In order to build a machine learning
# classifier to distinguish between flower species
from sklearn.preprocessing import LabelEncoder
# A random forest is an ensemble learning method used for
# classification,consisting of multiple decision trees.
from sklearn.ensemble import RandomForestClassifier
# needs two sets of data: a training set and a testing (or
# validation) set.
from sklearn.cross_validation import train_test_split
from sklearn.metrics import classification_report
import numpy as np
import argparse
# glob to grab the paths of images off disk
import glob
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
                help="path to the image")
ap.add_argument("-m", "--masks", required=True,
                help="path to the image masks")
args = vars(ap.parse_args())

# Using glob to grab the paths of his images and masks.
imagePaths = sorted(glob.glob(args["image"] + "/*.png"))
maskPaths = sorted(glob.glob(args["masks"] + "/*.png"))

print("Got {} images".format(len(imagePaths)))
print("Got {} masks".format(len(maskPaths)))
data = []
target = []

# Instantiating image descriptor – a 3D RGB color histogram with 8 bins per
# channel. This image descriptor will yield an 8 × 8 × 8 = 512-dimensional feature
# vector used to characterize the color of the flower.
desc = RGBHistogram([8, 8, 8])

for (imagePath, maskPath) in zip(imagePaths, maskPaths):
    image = cv2.imread(imagePath)
    mask = cv2.imread(maskPath)
    mask = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)

    features = desc.describe(image, mask)

    data.append(features)
    # flower label
    target.append(imagePath.split("_")[-2])
# print("data.len:{}".format(len(data)))
# print("data[0]:{}".format(data[0]))
# The unique method of NumPy is used to find the unique species
# names, which are then fed into the LabelEncoder.
print("target:{}".format(target))
targetNames = np.unique(target)
print("targetNames:{}".format(targetNames))
le = LabelEncoder()
# A call to fit_transform “fits” the unique species names into integers,
# a category for each species, and then “transforms” the
# strings into their corresponding integer classes.
# The target variable now contains a list of integers, one for each data
# point, where each integer maps to a flower species name.
target = le.fit_transform(target)
print("target:{}".format(target))
(trainData, testData, trainTarget, testTarget) = train_test_split(data,
                                                                  target, test_size=0.3, random_state=42)

# using 25 decision trees in the forest.
# a pseudo random state is explicitly used so that Charles’ results are reproducible.
model = RandomForestClassifier(n_estimators=25, random_state=84)
model.fit(trainData, trainTarget)
# Prints out the accuracy of his model using the classification_report function.
# Passes in the actual testing targets as the first parameter and then lets
# the model predict what it thinks the flower species are for the testing data.
# The classification_report function then compares the predictions to the true
# targets and prints an accuracy report for both the overall system and each
# individual class label.
print(classification_report(testTarget, model.predict(testData),
                            target_names=targetNames))

for i in np.random.choice(np.arange(0, len(imagePaths)), 5):
    imagePath = imagePaths[i]
    maskPath = maskPaths[i]

    image = cv2.imread(imagePath)
    # image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # cv2.imshow("image", image)
    mask = cv2.imread(maskPath)
    mask = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)

    features = desc.describe(image, mask)

    flower = le.inverse_transform(model.predict([features]))[0]
    print(imagePath)
    print("I think this flower is a {}".format(flower.upper()))
    cv2.imshow(flower.upper(), image)
    cv2.waitKey(0)
