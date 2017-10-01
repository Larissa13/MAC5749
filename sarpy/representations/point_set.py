"""
PointSet representation of shape
"""
import numpy as np
from .shape import Shape

class PointSet(Shape):
    def __init__(self, data):
        self.data = data
        self.shape = data.shape

    def scale(self, c):
        """
            Scales point set by a certain factor.

            Parameters:
            * shape: Shape
              - Input shape
            * c: {float, tuple of floats}
               - Scale factors. Separate factors can be defined as (row_scale, col_scale)
            Returns:
            * scaled_shape: Shape
                - Scaled version of the input shape
        """
        pass

    def shift(self, c):
        """
            Shifts point set by a certain factor.

            Parameters:
            * shape: Shape
              - Input shape
            * c: {float, tuple of floats}
               - Shift factors. Separate factors can be defined as (row_shift, col_shift)
            Returns:
            * shifted_shape: Shape
                - Shifted version of the input shape
        """
        # Converting scalar factor to tuple
        if type(c) != tuple:
            c = (c,c)

        # Creating new point_set
        shifted_shape = PointSet(np.copy(self.data))
        for i, point in enumerate(shifted_shape.data):
            shifted_shape.data[i] = (point[0] - c[0], point[1] - c[1])

        return shifted_shape

    def to_bitmap(self):
        # Need to define the size of the final image? TODO
        H = max(self.data[:,0]) + 1
        W = max(self.data[:,1]) + 1
        A = np.zeros((H,W))
        A[self.data[:,0], self.data[:,1]] = 1
        return A
    
    def to_pointSet(self):
        return self