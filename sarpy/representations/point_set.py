"""
PointSet representation of shape
"""
import numpy as np
from .shape import Shape

class PointSet(Shape):
    """PointSet Shape representation.

    A PointSet defines a shape by

    Attributes
    ----------
    data : `obj`
        Object containing the shape representation data. Typically this
        is a NumPy `ndarray`, but any representation is possible.
    """
    def __init__(self, data):
        self.data = data

    def shift(self, c):
        """Shifts point set by a certain factor.

        Parameters:
        -----------
        c: {float, tuple of floats}
            Shift factors. Separate factors can be defined as (row_scale, col_scale)

        Returns:
        --------
        shifted_pointSet: PointSet
            Shifted version of this point set.
        """
        # Converting scalar factor to tuple
        if type(c) != tuple:
            c = (c,c)

        # Creating new point_set
        shifted_shape = PointSet(np.copy(self.data))
        for i, point in enumerate(shifted_shape.data):
            shifted_shape.data[i] = (point[0] - c[0], point[1] - c[1])

        return PointSet(shifted_shape)

    def to_bitmap(self):
        """Converts point set to Bitmap.

        Returns
        -------
        bitmap : Bitmap
            Converted point set in bitmap format.
        """
        # Need to define the size of the final image? TODO
        H = max(self.data[:,0]) + 1
        W = max(self.data[:,1]) + 1
        A = np.zeros((H,W))
        A[self.data[:,0], self.data[:,1]] = 1
        return A

    def to_pointSet(self):
        return self
