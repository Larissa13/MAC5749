"""
The "Shape" general object is a catch-all for representing the many types
of possible shape representations, allowing a degree of abstraction to the user,
and making some of the conversions transparent when possible.
"""
import numpy as np

# Available shape types:
type_bitmap, contour, type_point_set, type_complex_contour, type_polar_contour, type_landmarks = range(6)
type_names = ["type_bitmap", "contour", "type_point_set", "type_complex_contour", "type_polar_contour", "type_landmarks"]

def is_type_valid(shape_type):
    """
    Verifies if a given shape type is valid.
    Parameters:
        * shape_type: int
          - Shape type being verified
        Returns:
        * valid: bool
          - True if valid, False otherwise.
    """
    return shape_type in range(6)

def is_data_valid(data, shape_type):
    """
    Verifies is a given data object is valid for a given shape type.
    Verifies if a given shape type is valid.
    Parameters:
        * data: Object
          - Data object being verified
        * shape_type: int
          - Shape type to check against
        Returns:
        * valid: bool
          - True if valid, False otherwise.
    """
    if shape_type == type_bitmap:
        # A bitmap is a 2-dimensional numpy ndarray
        if len(data.shape) > 2:
            return False

    # TODO: other shape types
    if shape_type == contour:
        pass

    if shape_type == type_point_set:
        pass
    #...

    return True

class Shape:
    def __init__(self, shape_type, data):
        """
        Initializing the Shape object with the specified type and data.
        """
        assert is_type_valid(shape_type), "Error initializing Shape: Invalid shape_type given ({})".format(type_names[shape_type])
        assert type(data) == np.ndarray, "Error initializing Shape: data is not a ndarray"
        assert is_data_valid(data, shape_type), "Error initializing Shape: data does not fit shape_type"

        self.shape_type = shape_type
        self.data = data
        self.shape = data.shape

    def get_type_name(self):
        return type_names[self.shape_type]

    # Overloads
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