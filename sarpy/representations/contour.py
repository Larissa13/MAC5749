"""
Contour representation of shapes
"""
import numpy as np
from .shape import Shape

class Contour(Shape):
    def __init__(self, data):
        self.data = data
        self.shape = data.shape

    def scale(self, c, center=(0,0)):
        contour = shape.data
        if type(c) == type((0,0)):
            h2 = floor(c[0])
            w2 = floor(c[1])
        else:
            raise ValueError('Error in arguments')
            
        h1,w1=contour.shape
        x_ratio = w1/w2;
        y_ratio = h1/h2;    
        g = np.zeros(h2*w2)
        for i in range(h2):
            for j in range(w2):
                px = floor(j*x_ratio) ;
                py = floor(i*y_ratio) ;
                g[(i*w2)+j] = contour[py][px];
        g = g.reshape(h2,w2)
        return Shape(type_contour, g);

    def to_contour(self):
        return self
    
