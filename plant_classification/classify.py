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
