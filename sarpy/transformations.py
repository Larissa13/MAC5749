"""
Module storing the many transformations that can be applied to Shapes.
"""

import numpy as np
from math import ceil, floor
from sarpy.utils import *

# +------------------------------------------------------------+
# |                      SCALE OPERATIONS                      |
# +------------------------------------------------------------+

def shape_scale(shape, c, center=(0,0)):
    """
        Scales shape by a certain factor. This function calls the appropriate `shape_scale`
        function for the type of the given shape.

        Parameters:
        * shape: Shape
          - Input shape
        * c: {float, tuple of floats}
           - Scale factors. Separate factors can be defined as (row_scale, col_scale)
        * center: tuple of ints, optional
           - (x,y)-coordinates of the center of the image
        Returns:
        * scaled_shape: Shape
            - Scaled version of the input shape
    """

    # performing the proper scaling function, based on type
    if shape.shape_type == type_bitmap:
        return shape_scale_bitmap(shape, c, center)
    if shape.shape_type == type_contour:
        return shape_scale_contour(shape, c)
    
    raise NotImplementedError("This function hasn't yet been implemented for shapes of type {}".format(shape.get_type_name()))

def shape_scale_bitmap(shape, c, center=(0,0)):
    """
        Scales bitmap by a certain factor.

        Parameters:
        * shape: Shape
          - Input shape
        * c: {float, tuple of floats}
           - Scale factors. Separate factors can be defined as (row_scale, col_scale)
        * center: tuple of ints, optional
           - (x,y)-coordinates of the center of the image
        Returns:
        * scaled_shape: Shape
            - Scaled version of the input shape
    """
    bitmap = shape.data

    if type(c) == type((0,0)):
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
                    g[i,j] = bitmap[ceil(x), ceil(y)]
                else:
                    g[i,j] = 0
    return Shape(type_bitmap, g)

def shape_scale_contour(shape, c):
    """
        Scales contour by a certain factor.

        Parameters:
        * shape: Shape
          - Input shape
        * c: {float, tuple of floats}
           - Scale factors. Separate factors can be defined as (row_scale, col_scale)
        Returns:
        * scaled_shape: Shape
            - Scaled version of the input shape
    """
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


# ^===================END OF SCALE OPERATIONS==================^

# +------------------------------------------------------------+
# |                      SHIFT OPERATIONS                      |
# +------------------------------------------------------------+

def shape_shift(shape, c):
    """
        Shifts shape by a certain factor. This function calls the appropriate `shift_scale`
        function for the type of the given shape.

        Parameters:
        * shape: Shape
          - Input shape
        * c: {float, tuple of floats}
           - Shift factors. Separate factors can be defined as (row_scale, col_scale)
        Returns:
        * shifted_shape: Shape
            - Shifted version of the input shape
    """

    # performing the proper shifting function, based on type
    if shape.shape_type == type_bitmap:
        return shape_shift_bitmap(shape, c)
    
    raise NotImplementedError("This function hasn't yet been implemented for shapes of type {}".format(shape.get_type_name()))
    
def shape_shift_bitmap(shape, c):
    """
        Shifts bitmap by a certain factor.

        Parameters:
        * shape: Shape
          - Input shape
        * c: {float, tuple of floats}
           - Shift factors. Separate factors can be defined as (row_scale, col_scale)
        Returns:
        * shifted_shape: Shape
            - Shifted version of the input shape
    """
    if type(c) == type((0, 0)):
        c1 = c[0]
        c2 = c[1]
    else:
        c1 = c2 = c

    g = np.zeros_like(shape)
    for i in range(shape.shape[0]):
        for j in range(shape.shape[1]):
            x = i - c1
            y = j - c2
            if x < shape.shape[0] and y < shape.shape[1]:
                if x > 0 and y > 0:
                    g[i, j] = shape[x, y]
                else:
                    g[i, j] = 0
    return Shape(type_bitmap, g)