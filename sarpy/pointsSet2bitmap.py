import numpy as np

def pointsSet2Bitmap(setPoint, size=(0,0)):
    h1 = size[0]
    w1 = size[1]
    h2 = max(setPoint[:,0]) + 1
    w2 = max(setPoint[:,1]) + 1
    H = max([h1,h2])
    W = max([w1,w2])

    A = np.zeros((H,W))
    A[setPoint[:,0], setPoint[:,1]] = 1
    return A
