import numpy as np
import matplotlib.pyplot as plt

def plotContour(c):
    
    if (type(c) == type(np.array(()))) & (c.shape[1] >= 3):
            
        w = np.amax(c[:,1])+1
        h = np.amax(c[:,2])+1
        img = np.zeros((h,w), dtype='int8')
        
        for i in range(c.shape[0]):
            a = c[i,1]
            b = c[i,2]
            img[b,a] = 1
            
        fig, ax = plt.subplots()
        ax.imshow(img,cmap='gray')
        ax.axis('off')
        plt.show()
        
    else:
        raise ValueError('Error: the argument has to be a ndarray with at least 3 columns')

def contour2bm(c):
    
    if (type(c) == type(np.array(()))) & (c.shape[1] >= 3):
            
        w = np.amax(c[:,1])+1  # replace with img width 
        h = np.amax(c[:,2])+1  # replace with img height
        img = np.zeros((h,w), dtype='int8')
        
        for i in range(c.shape[0]):
            x = c[i,1]
            y = c[i,2]
            img[y,x] = 1
            
        return img;       

    else:
        raise ValueError('Error: the argument has to be a contour')        
