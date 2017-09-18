import numpy as np

from math import sqrt
from cmath import phase

# +------------------------------------------------------------+
# |            CONVERT CONTOUR TO COMPLEX POLAR                |
# +------------------------------------------------------------+

def Contour2ComplexPolar(contour):
    """
        Transform parametric contour to polar representation

        Parameters:
        * contour: Contour
          - Input contour shape (numpy.ndarray) where each element contains [t, x, y]
        Returns:
        * complexpolar: Polar 
            - Polar Representation (numpy.ndarray) where each element contains [t, rho, theta]
    """
    
    complexpolar = []

    for points in contour:
        t, x, y = points
        rho = sqrt(x*x+y*y)
        theta = phase(complex(x, -y))
        polar = [t, rho, theta]
        complexpolar.append(polar)
    
    return np.array(complexpolar)

