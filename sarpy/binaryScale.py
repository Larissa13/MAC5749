import numpy as np
from math import ceil

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
