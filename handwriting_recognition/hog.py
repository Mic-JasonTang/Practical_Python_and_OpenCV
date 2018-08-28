# -*- coding: utf-8 -*-
# @Author:   MR_Radish
# @Date:     2018-08-26 22:47:40
# @E-mail:   ty_2016@foxmail.com
# @FileName: hog.py
# @TODO: HOG descriptor

from skimage import feature
# API: http://scikit-image.org/docs/dev/api/skimage.feature.html#skimage.feature.hog
# API: http://scikit-image.org/docs/dev/auto_examples/features_detection/plot_hog.html#sphx-glr-auto-examples-features-detection-plot-hog-py
class HOG:
	# The first, orientations, defines how many gradient orientations
	# will be in each histogram (i.e., the number of bins).
	# The pixelsPerCell parameter defines the number of pixels
	# that will fall into each cell.
	# HOG will then normalize each of the histograms according to the
	# number of cells that fall into each block using the cellsPerBlock
	# argument.
	# Optionally, HOG can apply power law compression (taking the
	# log/square-root of the input image), which can lead
	# to better accuracy of the descriptor.
	def __init__(self, orientations = 9, pixelsPerCell = (8, 8),
				cellsPerBlock = (3, 3), transform = False):
		self.orientations = orientations
		self.pixelsPerCell = pixelsPerCell
		self.cellsPerBlock = cellsPerBlock
		self.transform = transform

	def describe(self, image):

		# The image for which the HOG descriptor should be computed.
		hist = feature.hog(image,
			orientations = self.orientations,
			pixels_per_cell = self.pixelsPerCell,
			cells_per_block = self.cellsPerBlock,
			transform_sqrt = self.transform)
		# Return the resulting HOG feature vector.
	# out : (n_blocks_row, n_blocks_col, n_cells_row, n_cells_col, n_orient) ndarray

	# 	HOG descriptor for the image. If feature_vector is True, a 1D (flattened) array is returned.

	# 	hog_image : (M, N) ndarray, optional

	# 	A visualisation of the HOG image. Only provided if visualize is True.
		return hist
