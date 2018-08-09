"""
Complex polar representation of shape
"""

from math import cos, sin
import numpy as np
from .shape import Shape
from .contour import Contour

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
		return Contour(np.array(contours))
