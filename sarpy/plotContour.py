import numpy as np
import matplotlib.pyplot as plt

def plotContour(c):
    
    if (type(c) == type(np.array(()))) & (c.shape[1] >= 3):
            
        x = np.amax(c[:,1])+1
        y = np.amax(c[:,2])+1
        img = np.zeros((x,y), dtype='int16')
        
        for i in range(c.shape[0]):
            a = c[i,1]
            b = c[i,2]
            img[a,b] = 1
            
        fig, ax = plt.subplots()
        ax.imshow(img)
        ax.axis('off')
        plt.show()
        
    else:
        raise ValueError('Error: the argument has to be a ndarray with at least 3 columns')