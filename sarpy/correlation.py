def correlationFinder(image, template, c, color=1):
    """ 
    
        Calculate the correlation and find matches between an image and a template drawing a square around the higher values pixels according a given coeficient.
        
        Parameters:
        * image: nparray
          - image bitmap
        * template: nparray
          - template bitmap
        * c: int
          - match coeficient between 0 and 1, example: it will find the 100% correlation if c=1, it will find the 50% correlation if c=0.5
        * color: int, optional
          - binary level color which will be used to highlight the match, can be 0 or 1
          
        Returns:
        * matc: ndarray
          - 'recognized' image
          
    """
    from scipy import signal
    import numpy as np
    from math import ceil
    import matplotlib.pyplot as plt
    
    corr = signal.correlate2d(image, template, boundary='symm', mode='same')
    
    plt.imshow(corr, cmap='gray')
    plt.axis('off')
    plt.show()
    
    templateTrue = np.sum(template)
    corrLim = c * templateTrue
    
    squareDim = template.shape              #
    matc = np.copy(image)                   #
    for i in range(corr.shape[0]):          #
        for j in range(corr.shape[1]):      #
            if corr[i,j]> corrLim:          #  
                x = ceil(squareDim[0]/2)    #  draw a square with template dimensions in the original image
                y = ceil(squareDim[1]/2)    #  around the pixel with value over the limit in the correlated image
                for k in range(x):          #
                    matc[i-k,j-y] = matc[i+k,j-y] = matc[i-k,j+y] = matc[i+k,j+y] = color  
                for l in range(y):          #
                    matc[i-x,j-l] = matc[i+x,j-l] = matc[i-x,j+l] = matc[i+x,j+l] = color   

    return(matc)