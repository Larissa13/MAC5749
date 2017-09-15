import numpy as np
import matplotlib.pyplot as plt

def plotContour1D(c, show='default'):
    """
        Plot a contour as a graph of x, y coordinates in fuction of the parametric position. 

        Parameters:
        * c: nparray
          - Input contour type ndarray with at least 3 columns
        * show: string, optional, default: 'default'
		  - The show mode of two coordinates x, y. This parameter can be:
			o 'default' shows both of the coordinates plot in separated graphs
			o 'together' shows both of the coordinates plot in the same graph
			o 'line' shows only the graph of line coordinates x
			o 'column' shows only the graph of column coordinates y
        
    """
    if (type(c) == type(np.array(()))) & (c.shape[1] >= 3):
        
        if (show == 'default'):
        
            fig1 = plt.figure()
            ax1 = fig1.add_subplot(111)
            ax1.plot(c[:,0], c[:,1], color='blue', marker='*')
            ax1.set(ylabel='Contour Coordinate', xlabel='Position')
            ax1.legend(['line index'])
            
            fig2 = plt.figure()
            ax2 = fig2.add_subplot(111)
            ax2.plot(c[:,0], c[:,2], color='red', marker='o')
            ax2.set(ylabel='Contour Coordinate', xlabel='Position')
            ax2.legend(['column index'])
            
            plt.show()
            
        elif (show == 'together'):
        
            fig = plt.figure()
            ax = fig.add_subplot(111)
            ax.plot(c[:,0], c[:,1], color='blue', marker='*')
            ax.plot(c[:,0], c[:,2], color='red', marker='o')
            ax.set(ylabel='Contour Coordinate', xlabel='Position')
            ax.legend(['line index', 'column index'])
            
            plt.show()
            
        elif (show == 'line'):
        
            fig1 = plt.figure()
            ax1 = fig1.add_subplot(111)
            ax1.plot(c[:,0], c[:,1], color='blue', marker='*')
            ax1.set(ylabel='Contour Coordinate', xlabel='Position')
            ax1.legend(['line index'])
            
            plt.show()
            
        elif (show == 'column'):
            
            fig2 = plt.figure()
            ax2 = fig2.add_subplot(111)
            ax2.plot(c[:,0], c[:,2], color='red', marker='o')
            ax2.set(ylabel='Contour Coordinate', xlabel='Position')
            ax2.legend(['column index'])
            
            plt.show()
            
        else:
            raise ValueError('Error: the argument show has to be "default", "together", "line" or "column"')
            
    else:
        raise ValueError('Error: the argument c has to be a ndarray with at least 3 columns')
