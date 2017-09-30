"""
Complex polar representation of shape
"""

import numpy as np
from .shape import Shape
from math import cos, sin

class ComplexPolar(Shape):
	def __init__(self, data):
		self.data = data
		self.shape = data.shape

	def to_complex_polar(self):
		return self

	def to_contour(self):
		contours = []
		complex_polar = self.data
		for polar in complex_polar:
			t, rho, theta = polar
			x = rho * cos(theta)
			y = rho * sin(theta)
			contour = [t, x, -y]
			contours.append(contour)
		return np.array(contours)