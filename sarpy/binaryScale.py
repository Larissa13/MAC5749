import numpy as np
from math import ceil

# shapeScale(img, c, center=(0,0))
# Scale image by a certain factor.
# Parameters:
# * img: ndarray
#   - Input binary image
# * c: {float, tuple of floats}
#    - Scale factors. Separate factors can be defined as (row_scale, col_scale)
# * center: tuple of ints, optional
#    - (x,y)-coordinates of the center of the image
# Returns:
# * g: ndarray
#     - Scaled version of the input image

def shapeScale(img, c, center=(0,0)):
    
    if type(c) == type((0,0)):
        c1 = c[0]
        c2 = c[1]
    else:
        c1 = c2 = c
    x0 = center[0]
    y0 = center[1]

    g = np.zeros_like(img)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            x = c1*(i - x0) + x0
            y = c2*(j - y0) + y0
            if x < img.shape[0] and y < img.shape[1]:
                if x > 0 and y > 0:
                    g[i,j] = img[ceil(x), ceil(y)]
                else:
                    g[i,j] = 0
    return g

def shapeScale2(img, c):
    if type(c) == type((0,0)):
        h2 = floor(c[0])
        w2 = floor(c[1])
    else:
        raise ValueError('Error in arguments')
        
    h1,w1=img.shape
    x_ratio = w1/w2;
    y_ratio = h1/h2;    
    g = np.zeros(h2*w2)
    for i in range(h2):
        for j in range(w2):
            px = floor(j*x_ratio) ;
            py = floor(i*y_ratio) ;
            g[(i*w2)+j] = img[py][px];
    g = g.reshape(h2,w2)
    return g;