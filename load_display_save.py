# -*- coding: utf-8 -*-
# @Author:   MR_Radish
# @Date:     2018-07-23 18:00:01
# @E-mail:   ty_2016@foxmail.com
# @FileName: load_display_save.py
# @TODO: 利用argparse解析命令行参数实现文件读写


import argparse
import cv2

# print(cv2.__version__) #3.4.1
ap = argparse.ArgumentParser()
ap.add_argument("--image", "-i", required=True, help="Path to the image")
print(ap.parse_args())
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
print("width: {} pixels".format(image.shape[1]))
print("height: {} pixels".format(image.shape[0]))
print("channels: {} pixels".format(image.shape[2]))

cv2.imshow("image", image)
cv2.waitKey(0)
cv2.imwrite("./images/newcat.png", image)

