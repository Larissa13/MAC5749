"""
Bitmap representation of shapes
"""
import numpy as np
from .shape import Shape
from .contour import Contour, extract_contours
from .pointSet import PointSet
from skimage import measure
import skimage.io as skio

class Bitmap(Shape):
    def __init__(self, data):
        self.data = data
        self.shape = data.shape

    def scale(self, c, center=(0,0)):
        bitmap = self.data

        if isinstance(c,tuple):
            c1 = c[0]
            c2 = c[1]
        else:
            c1 = c2 = c
        x0 = center[0]
        y0 = center[1]

        g = np.zeros_like(bitmap)
        for i in range(bitmap.shape[0]):
            for j in range(bitmap.shape[1]):
                x = c1*(i - x0) + x0
                y = c2*(j - y0) + y0
                if x < bitmap.shape[0] and y < bitmap.shape[1]:
                    if x > 0 and y > 0:
                        g[i,j] = bitmap[np.ceil(x), np.ceil(y)]
                    else:
                        g[i,j] = 0
        self.data = g

    def shift(self, c):
        bitmap = self.data
        if isinstance(c, tuple):
            c1 = c[0]
            c2 = c[1]
        else:
            c1 = c2 = c

        g = np.zeros_like(self.data)
        for i in range(bitmap.shape[0]):
            for j in range(bitmap.shape[1]):
                x = i - c1
                y = j - c2
                if x < bitmap.shape[0] and y < bitmap.shape[1]:
                    if x > 0 and y > 0:
                        g[i, j] = bitmap[x, y]
                    else:
                        g[i, j] = 0
        self.data = g

    def to_bitmap(self):
        return self

    def to_contour(self):
        return extract_contours(self.data)

    def to_pointSet(self):
        bitmapImage = self.data
        data = []
        row = 0
        while row < bitmapImage.shape[0]:
            column = 0
            while column + 1 < bitmapImage.shape[1]:
                if (bitmapImage[row][column] != bitmapImage[row][column + 1]):
                     if ((not bitmapImage[row][column]) and (bitmapImage[row][column + 1])) or ((bitmapImage[row][column]) and not (bitmapImage[row][column + 1])):
                        data.append([row + 1, column + 1])
                column += 1
            row += 1
        return PointSet(np.array(data))

    def save(self, filename):
        skio.imsave(filename,self.data)

    def read(self, filename):
        img = skio.imread(filename, as_grey=True)
        self.data = img
        self.shape = img.shape
        
    def show(self):
        skio.imshow(self.data)
