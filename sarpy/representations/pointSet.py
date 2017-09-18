"""
PointSet representation of shape
"""
import numpy as np
from .shape import Shape

class PointSet(Shape):
    def __init__(self, data):
        self.data = data
        self.shape = data.shape

    def to_bitmap(self):
        # Need to define the size of the final image? TODO
        h1 = size[0]
        w1 = size[1]
        setPoint = np.array(setPoint)
        h2 = max(setPoint[:,0]) + 1
        w2 = max(setPoint[:,1]) + 1
        H = max([h1,h2])
        W = max([w1,w2])
        A = np.zeros((H,W))
        A[setPoint[:,0], setPoint[:,1]] = 1
        return A
    
    def to_pointSet(self):
        return self

