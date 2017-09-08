import numpy as np
import matplotlib.pyplot as plt

def plotContour1D(c):
    
    if (type(c) == type(np.array(()))) & (c.shape[1] >= 3):
        
            fig = plt.figure()
            ax = fig.add_subplot(111)
            ax.plot(c[:,0], c[:,1], color='blue', marker='*')
            ax.plot(c[:,0], c[:,2], color='red', marker='o')
            ax.set(ylabel='Contour Coordinate', xlabel='Position')
            ax.legend(['line index', 'column index'])
            plt.show()
            
    else:
        raise ValueError('Error: the argument has to be a ndarray with at least 3 columns')