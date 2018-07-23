# -*- coding: utf-8 -*-
# @Author:   MR_Radish
# @Date:     2018-07-23 18:49:55
# @E-mail:   ty_2016@foxmail.com
# @FileName: argparse_demo.py
# @TODO: 学习argparse的一些常用参数


import argparse
import cv2

class A:
	pass

a = A()
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the image")
ap.add_argument("-b", "--bb", help = "bbb")
ap.add_argument("-c", "--cc", help = "ccc")
# 这里的a要是已经存在的对象的实例
args = ap.parse_args("-i asd -b bbbbbbb -c ccccccc".split(), namespace=a)
print(type(args))
print(vars(args))
print(a.image, a.bb)
# print help
print(ap.print_help())
