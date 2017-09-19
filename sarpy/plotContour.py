import numpy as np
import matplotlib.pyplot as plt

def plotContour(c):
    """
        Plot a contour as an image. 

        Parameters:
        * c: nparray
          - Input contour type ndarray with at least 3 columns
        
    """
    
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
    """
        Convert contour to bitmap. 

        Parameters:
        * c: nparray
          - Input contour type ndarray with at least 3 columns
          
        Returns:
        * img: Bitmap
            - Bitmap representation of the input contour
        
    """
	if (type(c) == type(np.array(()))) & (c.shape[1] >= 3):        
	        #
	        copy = np.asarray(c.copy())        
	        copy = copy - np.min(copy,axis=0)
	        #
	        maxv = np.max(copy,axis=0)        
	        img = np.zeros((maxv[1]+1,maxv[2]+1), dtype='int8')        
	        for i in range(c.shape[0]):
	            x = copy[i,1]
	            y = copy[i,2]
	            img[x,y] = 1            
	        return img;
	    else:
	        raise ValueError('Error: the argument has to be a contour')        

