"""Abstract Shape representation.

The ``Shape`` object is a catch-all  for representing the many types
of possible shape representations, allowing a degree of abstraction to the user,
and making some of the conversions transparent when possible.
"""
import numpy as np

class Shape:
    """Abstract Shape representation.

    The Shape class contains a few overloads, to make working with the
    `data` attribute easier, and a few function signatures which should
    be filled for all shape representations, such as conversions and
    transforms.

    Attributes
    ----------
    data : `obj`
        Object containing the shape representation data. Typically this
        is a NumPy `ndarray`, but any representation is possible.
    """

    def __init__(self, data):
        """Abstract Shape representation.

        Initializes an abstract Shape representation. Most of the time,
        however, you're going to want to use the children classes'
        constructors.

        Parameters
        ----------
        data : `obj`
            Object containing the shape representation data.
        """
        self.data = data

    # Overloads for lists/numpy arrays
    def __len__(self):
        return len(self.data)
    def __getitem__(self, key):
        return self.data[key]
    def __setitem__(self, key, value):
        self.data[key] = value
    def all(self, axis=None, out=None, keepdims=False):
        return self.data.all(axis, out, keepdims)
    def any(self, axis=None, out=None, keepdims=False):
        return self.data.any(axis, out, keepdims)

    def scale(self, c, center=(0,0)):
        """Scales shape by a certain factor.

        Parameters:
        -----------
        c: {float, tuple of floats}
            Scale factors. Separate factors can be defined as (row_scale, col_scale)
        center: tuple of ints, optional
            (x,y)-coordinates of the center of the image
        Returns:
        --------
        scaled_shape: Shape
            Scaled version of this shape.
        """
        raise NotImplementedError()
        pass

    def shift(self, c):
        """Shifts shape by a certain factor.

        Parameters:
        -----------
        c: {float, tuple of floats}
            Shift factors. Separate factors can be defined as (row_scale, col_scale)

        Returns:
        --------
        shifted_shape: Shape
            Shifted version of this shape.
        """
        raise NotImplementedError()
        pass

    def to_bitmap(self):
        """Converts shape to Bitmap.

        Returns
        -------
        bitmap : Bitmap
            Converted shape in bitmap format.
        """
        raise NotImplementedError()
        pass

    def to_pointSet(self):
        """Converts shape to PointSet.

        Returns
        -------
        pointSet : PointSet
            Converted shape in pointSet format.
        """
        raise NotImplementedError()
        pass

    def to_contour(self):
        """Converts shape to Contour.

        Returns
        -------
        contour : Contour
            Converted shape in contour format.
        """
        raise NotImplementedError()
        pass

    def to_complexPolar(self):
        """Converts shape to ComplexPolar.

        Returns
        -------
        complexPolar : ComplexPolar
            Converted shape in complexPolar format.
        """
        raise NotImplementedError()
        pass

    def save(self, filename):
        """Saves shape to file.

        Parameters
        -------
        filename : str
            Filename to save the shape to.
        """
        raise NotImplementedError()
        pass

    def read(self, filename):
        """Reads shape from file.

        Loads the content of the file into this object.

        Parameters
        -------
        filename : str
            Filename to read the shape from.
        """
        raise NotImplementedError()
        pass

    def show(self):
        """Visualizes the shape.
        """
        raise NotImplementedError()
        pass
