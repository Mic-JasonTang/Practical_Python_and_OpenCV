# -*- coding: utf-8 -*-
# @Author:   MR_Radish
# @Date:     2018-07-23 20:38:11
# @E-mail:   ty_2016@foxmail.com
# @FileName: drawing.py
# @TODO: 使用OpenCV绘图

import numpy as np
import cv2

# 创建一个8bits的图像，像素范围是[0,255]，所以这里的数据类型是uint8
canvas = np.zeros((300, 300, 3), dtype=np.uint8)

green = (0, 255, 0)
# 参数1：绘制对象，参数2：起点，参数3：终点，参数4：颜色
cv2.line(canvas, (0,0), (300, 300), green)
# winname：如果窗口名已被创建，则会显示在一个图中，mat：图像
cv2.imshow("Canvas", canvas)


red = (0, 0, 255)
# 参数1：绘制对象，参数2：起点，参数3：终点，参数4：颜色，参数5（thickness）：线粗 默认1 pixels
cv2.line(canvas, (300, 0), (0,300), red, 3)
cv2.imshow("Canvas", canvas)

# 参数1：绘制对象，参数2：矩形的左上，参数3：矩形的右下，参数4：颜色，参数5：线粗 默认1 pixels
cv2.rectangle(canvas, (10, 10), (60, 60), green, 1)
cv2.rectangle
cv2.imshow("Canvas", canvas)

cv2.rectangle(canvas, (50, 200), (200, 225), red, 5)
cv2.imshow("Canvas", canvas)

blue = (0, 0, 255)
# 如果参数5 thickness是负数时，则会填充图形。
cv2.rectangle(canvas, (200, 50), (225, 125), blue, -1)
cv2.imshow("Canvas", canvas)
# cv2.waitKey(0)


canvas2 =np.zeros((300, 300, 3), dtype=np.uint8)
# shape[1]表示宽度，shape[0]表示高度
# //在python3中表示整除
(centerX, centerY) =(canvas2.shape[1] //2, canvas2.shape[0] //2)
white = (255, 255, 255)

for r in range(0, 175, 25):
	# 参数1：img, 参数2（元组）：center, 参数3：radius, 参数4：color
	cv2.circle(canvas2, (centerX, centerY), r, white)
	# output: 0 25 50 75 100 125 150
	# print(r)
	# 如果是下面的输出方法则会被缓存。知道cv2.waitKey结束之后才会执行。
	# print(r, end="")

cv2.imshow("Canvas2", canvas2)

# 随机绘制圆形
canvas3 = np.zeros((300, 300, 3), dtype=np.uint8)
for i in range(0, 25):
	radius = np.random.randint(5, high=200)
	# randint返回的是数组,经过tolist()之后转为列表
	color = np.random.randint(0, high=256, size=(3)).tolist()
	print(color, type(color))
	center = np.random.randint(0, high=300, size=(2))
	print(center, type(center))
	cv2.circle(canvas3, tuple(center), radius, color, -1)


cv2.imshow("Canvas3", canvas3)
cv2.waitKey(0)
