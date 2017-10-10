import numpy as np

from sarpy.utils import *
from transformations import shape_scale, shape_shift

# +------------------------------------------------------------+
# |                NORMALIZATION OPERATIONS                    |
# +------------------------------------------------------------+

def normalize(shape, width, height, center=(0,0)):
    """
        Normalize shape by rescaling its size to (width, height). 

        Parameters:
        * shape: Shape
          - Input shape
        * width: int
           - Shape width size
        * height: int
           - Shape height size
        * center: tuple of ints, optional
           - (x,y)-coordinates of the center of the image
        Returns:
        * normalizes_shape: Shape
            - Normalized version of the input shape
    """
    x,y = (shape.data).shape
    
    scale = width/x, height/y
    tmp = shape_scale(shape, scale, center)
    
    output = np.zeros([width, height])
    #crop img to reduce X axis size
    if(scale[0] < 1):
        padX = width//2
        output[:,0:min(y, height)] = tmp[x//2-padX:x//2+padX, 0:min(y, height)]
    #resize to larger img in X axis
    else:
        output[0:lin,0:min(y, height)] = tmp[:,0:min(y, height)]
        
    
    #crop img to reduce Y axis size
    if(scale[1] < 1):
        padY = height//2
        output[0:min(x, width),:] = tmp[0:min(x, width),y//2-padY:y//2+padY]
    #resize to larger img in Y axis
    else: 
        output[0:min(x, width),0:y] = tmp[0:min(x, width),:]
        
    return Shape(shape.shape_type, output)
