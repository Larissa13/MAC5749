"""
Methods for converting shape representations into other shape representations.
"""

from skimage import measure
from warnings import warn

from sarpy.utils import *

def convert_shape(shape, new_type, **kwargs):
    warn(DeprecationWarning)
    """
        Converts a given shape into another representation.

        Parameters:
        * shape: Shape
          - Input shape
        * new_type: int
          - New type of the shape. Must be one of the types defined in sarpy.utils.
        * kwargs
          - Arguments for the different conversions.
        Returns:
        * converted_shape: Shape
            - Converted representation of the input shape
    """

    # Verifying if the new_type is valid
    assert is_type_valid(new_type), "Error in convert_shape: new_type ({}) is not a valid type".format(new_type)

    # Here, we call the proper functions for converting every type into every other type.

    if shape.shape_type == new_type: # New type is the same as current type, i.e.: no conversion
        return shape
    if new_type == type_bitmap:
        return convert_to_bitmap(shape)
    if new_type == type_contour:
        return convert_to_contour(shape)
    if new_type == type_point_set:
        return convert_to_point_set(shape)
    if new_type == type_complex_contour:
        return convert_to_complex_contour(shape)
    if new_type == type_landmark:
        return convert_to_landmark(shape)
    if new_type == type_polar_contour:
        return convert_to_polar_contour(shape)


def convert_to_bitmap(shape):
    pass

def convert_to_contour(shape):
    warn(DeprecationWarning)
    """
    Converts a given shape into a contour.
    Parameters:
        * shape: Shape
          - Input shape
        Returns:
        * converted_shape: Shape
            - Contour representation of the input shape
    """

    if shape.shape_type == type_contour: # New type is the same as current type, i.e.: no conversion
        return shape

    if shape.shape_type == type_bitmap: # Bitmap to contour
        contours = measure.find_contours(img, 0)
        contours_lens = np.array([len(c) for c in contours])
        sort_order = (-contours_lens).argsort()
        return Shape(type_contour, [[np.array([j, contours[i][j][0], contours[i][j][1]], dtype = int) for j in range(len(contours[i]))] for i in sort_order])

    if new_type == type_point_set: # Point set to contour
        pass
    if new_type == type_complex_contour: # Complex contour to contour
        pass
    if new_type == type_landmark: # Landmark to contour
        pass
    if new_type == type_polar_contour: # Polar contour to contour
        pass


def convert_to_point_set(shape):
    warn(DeprecationWarning)
    """
    Converts a given shape into a pointset.
    Parameters:
        * shape: Shape
          - Input shape
        Returns:
        * converted_shape: Shape
            - Point set representation of the input shape
    """

    if shape.shape_type == type_point_set: # New type is the same as current type, i.e.: no conversion
        return shape

    if shape.shape_type == type_bitmap: # Bitmap to point set
        bitmapImage = shape.data
        pointSet = []
        row = 0
        while row < bitmapImage.shape[0]:
            column = 0
            while column + 1 < bitmapImage.shape[1]:
                if (bitmapImage[row][column] != bitmapImage[row][column + 1]):
                     if ((not bitmapImage[row][column]) and (bitmapImage[row][column + 1])) or ((bitmapImage[row][column]) and not (bitmapImage[row][column + 1])):
                        pointSet.append([row + 1, column + 1])
                column += 1
            row += 1
        
        return Shape(type_point_set, pointSet)

    if new_type == type_contour: # Contour to point set
        pass
    if new_type == type_complex_contour: # Complex contour to point set
        pass
    if new_type == type_landmark: # Landmark to point set
        pass
    if new_type == type_polar_contour: # Polar contour to point set
        pass


def convert_to_complex_contour(shape):
    pass
def convert_to_landmark(shape):
    pass
def convert_to_polar_contour(shape):
    pass