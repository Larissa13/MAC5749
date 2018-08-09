"""
Contour representation of shapes
"""
import numpy as np
from .shape import Shape
from .bitmap import Bitmap
import skimage.io as skio
from skimage import measure
from math import floor

# This function must be removed. Check if it doesn't break anything!
def extract_contours(img):
    warn(DeprecationWarning)
    contours = measure.find_contours(img, 0)
    contours_lens = np.array([len(c) for c in contours])
    sort_order = (-contours_lens).argsort()
    data = np.array([np.array([np.array([j, contours[i][j][0], contours[i][j][1]], dtype = int) for j in range(len(contours[i]))], dtype = int) for i in sort_order])
    return Contour(data)

class Contour(Shape):
    """Contour Shape representation.

    Stores the shape as a set of parametric contours, represented
    as an array of [t,x,y] arrays. #TODO: needs updating-

    Attributes
    ----------
    data : ndarray
        -needs updating-
    """

    def __init__(self, data):
        self.data = data

    def scale(self, c, center=(0,0)):
        """Scales contour by a certain factor.

        Parameters:
        -----------
        c: {float, tuple of floats}
            Scale factors. Separate factors can be defined as (row_scale, col_scale)
        center: tuple of ints, optional
            (x,y)-coordinates of the center of the image
        Returns:
        --------
        scaled_contour: Contour
            Scaled version of this contour.
        """
        contour = self.shape.data
        if type(c) == type((0,0)):
            h2 = floor(c[0])
            w2 = floor(c[1])
        else:
            raise ValueError('Error in arguments')

        h1,w1=contour.shape
        x_ratio = w1/w2;
        y_ratio = h1/h2;
        g = np.zeros(h2*w2)
        for i in range(h2):
            for j in range(w2):
                px = floor(j*x_ratio) ;
                py = floor(i*y_ratio) ;
                g[(i*w2)+j] = contour[py][px];
        g = g.reshape(h2,w2)
        return Contour(g);

    def to_contour(self):
        return self

    def to_bitmap(self):
        """Converts shape to Bitmap.

        Returns
        -------
        bitmap : Bitmap
            Converted shape in bitmap format.
        """
        copy = np.asarray(self.data.copy())
        copy = copy - np.min(copy,axis=0)
        #
        maxv = np.max(copy,axis=0)
        img = np.zeros((maxv[1]+1,maxv[2]+1), dtype='int8')
        for i in range(self.data.shape[0]):
            x = copy[i,1]
            y = copy[i,2]
            img[x,y] = 1
        return Bitmap(img);

    def save(self, filename):
        pass

    def read(self, filename):
        pass
