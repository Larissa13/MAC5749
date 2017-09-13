"""
Methods for converting shape representations into other shape representations.
"""

from sarpy.utils import *

def convert_shape(shape, new_type):
    """
        Converts a given shape into another representation.

        Parameters:
        * shape: Shape
          - Input shape
        * new_type: int
          - New type of the shape. Must be one of the types defined in sarpy.utils.
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
    pass
def convert_to_point_set(shape):
    pass
def convert_to_complex_contour(shape):
    pass
def convert_to_landmark(shape):
    pass
def convert_to_polar_contour(shape):
    pass