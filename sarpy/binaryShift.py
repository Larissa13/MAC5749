import numpy as np

def shapeShift(img, c):
    if type(c) == type((0, 0)):
        c1 = c[0]
        c2 = c[1]
    else:
        c1 = c2 = c

    g = np.zeros_like(img)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            x = i - c1
            y = j - c2
            if x < img.shape[0] and y < img.shape[1]:
                if x > 0 and y > 0:
                    g[i, j] = img[x, y]
                else:
                    g[i, j] = 0
    return g