"""
Tool for generating a synthetic object matching dataset based on the included datasets: NIST, Leaf, Fashion and MPEG7.
"""
import sys
sys.path.append('../')

from random import randrange

import numpy as np

from sarpy.representations import Bitmap
from sarpy.datasets import load_mpeg7, load_leaf, load_nist, load_fashion_mnist


def generate_image(size, shape_images, shape_positions):
    """
        This function generates and returns an image of size `size`,
        with the shapes in `shape_images` placed on the position in
        `shape_positions` (the lists will be zipped).

        Parameters:
        * size: tuple
          - Image size as a tuple: `(width, height)`
        * shape_images: list of Bitmaps
          - List of shape bitmaps
        * shape_positions: list of tuples
          - List of shape upper-left positions as tuples: `(x,y)`
        Returns:
        * generated_image: ndarray
            - Generated image as a NumPy 2D array.
    """
    assert len(shape_positions) >= len(shape_images), "Not enough positions for each shape ({}, need {})".format(len(shape_positions), len(shape_images))

    generated_image = np.zeros(size)

    for shape, position in zip(shape_images, shape_positions):
        # Getting coordinates for slice
        x,y = position
        w,h = shape.data.shape

        # Cutting the shape, if it crosses the limits of the generated image
        if x < 0:
            x_offset = -x
            x = 0
            shape.data = shape.data[x_offset:, :]
            w -= x_offset
        if x+w >= generated_image.shape[0]:
            x_offset = generated_image.shape[0] - (x+w)
            shape.data = shape.data[:-x_offset, :]
            w -= x_offset
        if y < 0:
            y_offset = -y
            y = 0
            shape.data = shape.data[:, y_offset:]
            h -= y_offset
        if y+h >= generated_image.shape[0]:
            y_offset = generated_image.shape[0] - (y+h)
            shape.data = shape.data[:, :-y_offset]
            h -= y_offset

        # Adding the shape to the image
        generated_image[x:x+w, y:y+h] = shape.data

    # Returning the generated image
    return generated_image


def randomize_position(lower_x, upper_x, lower_y, upper_y):
    """
        Generates a random tuple of positions, within the given limits.

        Parameters:
        * lower_x: int
          - Lower limit of the x coordinate, inclusive
        * upper_x: int
          - Upper limit of the x coordinate, exclusive
        * lower_y: int
          - Lower limit of the y coordinate, inclusive
        * upper_y: int
          - Upper limit of the y coordinate, exclusive
        Returns:
        * position: tuple
            - Shape upper-left position as a tuple: `(x,y)`
    """
    return (randrange(lower_x, upper_x), randrange(lower_y, upper_y))


def distort_shape(shape, distortion_type, distortion_intensity):
    """
        Distorts a shape in a specified way, with a specified intensity.

        Parameters:
        * shape: Bitmap
          - Shape of the Bitmap type
        * distortion_type: int
          - Type of the distortion. Options are: [TODO]
        * distortion_intensity: float
          - Intensity of the given distortion, normalized from 0 to 1.
        Returns:
        * distorted_shape: Bitmap
          - Distorted input shape
    """
    raise(NotImplementedError)


def load_datasets():
    """
        Loads all datasets into a single vector, along with the corresponding targets
        Returns:
        * bitmaps: list of Bitmaps
          - All of the loaded shapes as Bitmaps
        * targets: list of strings
          - Dataset targets, in the "template" format
    """

    

print(generate_image((5,5), [Bitmap(np.ones((2,2)))], [(1,1)]))
print(generate_image((5,5), [Bitmap(np.ones((2,5)))], [(-1,-1)]))
print(generate_image((5,5), [Bitmap(np.ones((4,4)))], [(3,3)]))

