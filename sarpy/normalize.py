import numpy as np

from sarpy.utils import *
from transformations import shape_scale, shape_shift

# +------------------------------------------------------------+
# |                NORMALIZATION OPERATIONS                    |
# +------------------------------------------------------------+

def normalize(shape, line, column, center=(0,0)):
    """
        Normalize shape by rescaling its size by (line, column). 

        Parameters:
        * shape: Shape
          - Input shape
        * line: int
           - Shape line size
        * column: int
           - Shape column size
        * center: tuple of ints, optional
           - (x,y)-coordinates of the center of the image
        Returns:
        * normalizes_shape: Shape
            - Normalized version of the input shape
    """
    x,y = (shape.data).shape
    
    scale = line/x, column/y
    tmp = shape_scale(shape, scale, center)
    
    output = np.zeros([line, column])
    #crop img to reduce X axis size
    if(scale[0] < 1):
        padX = line//2
        output[:,0:min(y, column)] = tmp[x//2-padX:x//2+padX, 0:min(y, column)]
    #resize to larger img in X axis
    else:
        output[0:lin,0:min(y, column)] = tmp[:,0:min(y, column)]
        
    
    #crop img to reduce Y axis size
    if(scale[1] < 1):
        padY = column//2
        output[0:min(x, line),:] = tmp[0:min(x, line),y//2-padY:y//2+padY]
    #resize to larger img in Y axis
    else: 
        output[0:min(x, line),0:y] = tmp[0:min(x, line),:]
        
    return Shape(shape.shape_type, output)
