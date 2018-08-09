"""
Bitmap representation of shapes
"""
import numpy as np
from .shape import Shape
from .contour import Contour
from .point_set import PointSet
from skimage import measure
import skimage.io as skio
import matplotlib.pyplot as plt

class Bitmap(Shape):
    """Bitmap Shape representation.

    Stores the shape as a full bitmap, a 2D boolean array.
    Pixels with value 1 contain the shape; pixels with
    value 0 are background.

    Attributes
    ----------
    data : ndarray
        2D boolean array containing the shape representation data.
    """

    def __init__(self, data):
        self.data = data

    def scale(self, c, center=(0,0)):
        """Scales bitmap by a certain factor.

        Parameters:
        -----------
        c: {float, tuple of floats}
            Scale factors. Separate factors can be defined as (row_scale, col_scale)
        center: tuple of ints, optional
            (x,y)-coordinates of the center of the image

        Returns:
        --------
        scaled_shape: Bitmap
            Scaled version of this bitmap.
        """
        bitmap = self.data

        if type(c) != tuple:
            c = (c,c)

        scaled_shape = np.zeros((round(bitmap.shape[0]/c[0]),round(bitmap.shape[1]/c[1])))
        for i in range(scaled_shape.shape[0]):
            for j in range(scaled_shape.shape[1]):
                x = c[0]*(i - center[0]) + center[0]
                y = c[1]*(j - center[1]) + center[1]
                if x > 0 and y > 0:
                    try:
                        scaled_shape[i,j] = bitmap[int(np.around(x)), int(np.around(y))]
                    except IndexError:
                        scaled_shape[i,j] = 0
                else:
                    scaled_shape[i,j] = 0
        return Bitmap(scaled_shape)

    def shift(self, c):
        """Shifts bitmap by a certain factor.

        Parameters:
        -----------
        c: {float, tuple of floats}
            Shift factors. Separate factors can be defined as (row_scale, col_scale)

        Returns:
        --------
        shifted_shape: Bitmap
            Shifted version of this bitmap.
        """
        bitmap = self.data
        if isinstance(c, tuple):
            c1 = c[0]
            c2 = c[1]
        else:
            c1 = c2 = c

        shifted_shape = np.zeros_like(self.data)
        for i in range(bitmap.shape[0]):
            for j in range(bitmap.shape[1]):
                x = i - c1
                y = j - c2
                if x < bitmap.shape[0] and y < bitmap.shape[1]:
                    if x > 0 and y > 0:
                        shifted_shape[i, j] = bitmap[x, y]
                    else:
                        shifted_shape[i, j] = 0
        return Bitmap(shifted_shape)

    def normalize(self, width, height):
        """
            Normalize bitmap by rescaling its size to (width, height).

            Parameters:
            -----------
            width: int
                Shape width size
            --------
            height: int
                Shape height size
            Returns:
            --------
            normalized_shape: Shape
                Normalized version of the input bitmap
        """
        # Determining scaling ratios and center
        height_ratio = self.data.shape[0]/height
        width_ratio = self.data.shape[1]/width
        return self.scale((height_ratio, width_ratio))

    def to_bitmap(self):
        return self

    def to_contour(self):
        """Converts bitmap to Contour.

        Returns
        -------
        contour : Contour
            Converted bitmap in contour format.
        """
        contours = measure.find_contours(self.data, 0)
        contours_lens = np.array([len(c) for c in contours])
        sort_order = (-contours_lens).argsort()
        data = np.array([np.array([np.array([j, contours[i][j][0], contours[i][j][1]], dtype = int) for j in range(len(contours[i]))], dtype = int) for i in sort_order])
        return Contour(data)

    def to_pointSet(self, conn=8):
        """Converts this bitmap to a PointSet representation.

        TODO: allow for inner/outer selection

        Parameters:
        -----------
        conn: int
            Connectivity topology to be used (4 or 8-neighborhood)

        Returns:
        --------
        point_set: PointSet
            PointSet representation of this shape
        """
        assert conn == 4 or conn == 8, "Error in Bitmap.to_pointSet: 'conn' must be 4 or 8"

        # Building adjacency lists
        if conn == 4:
            adjacents = [(0,1),(1,0),(0,-1),(-1,0)]
        else:
            adjacents = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]

        point_set_data = []

        # Iterating over pixels and checking if they're contours
        bitmapImage = self.data
        for row, line in enumerate(bitmapImage):
            for col, pixel in enumerate(line):
                # If pixel is foreground, check neighbors
                if bitmapImage[row,col]:
                    # Building neighborhood
                    neighborhood = [bitmapImage[row+x,col+y] for x,y in adjacents if row+x > 0 and col+y > 0 and row+x < bitmapImage.shape[0] and col+y < bitmapImage.shape[1]] + [0 for x,y in adjacents if not(row+x > 0 and col+y > 0 and row+x < bitmapImage.shape[0] and col+y < bitmapImage.shape[1])]
                    # if any pixel is background, then this is part of the contour
                    if not all(neighborhood):
                        point_set_data.append([row,col])
        return PointSet(np.array(point_set_data))

    def save(self, filename):
        """Saves shape to file.

        Parameters
        -------
        filename : str
            Filename to save the shape to.
        """
        skio.imsave(filename,self.data)

    def read(self, filename):
        """Reads shape from file.

        Loads the content of the file into this object.

        Parameters
        -------
        filename : str
            Filename to read the shape from.
        """
        img = skio.imread(filename, as_grey=True)
        self.data = img

    def show(self):
        """Visualizes the bitmap.

        Plots the bitmap utilizing matplotlib's `imshow`.
        """
        plt.imshow(self.data, cmap='Greys')
        plt.show()
