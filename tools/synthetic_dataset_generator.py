"""
Tool for generating a synthetic object matching dataset based on the
included datasets: NIST, Leaf, Fashion and MPEG7.

TODOs: implement distortion, distribution per dataset,
non-overlapping shapes, shapes outside image borders
"""
import sys, os
sys.path.append('../')

import random
import matplotlib.pyplot as plt

import numpy as np

from class_target_namer import get_class_name
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

    generated_image = np.zeros(size, dtype="bool")

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
        generated_image[x:x+w, y:y+h] = np.logical_or(generated_image[x:x+w, y:y+h], shape.data)

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
    return (random.randrange(lower_x, upper_x), random.randrange(lower_y, upper_y))


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


def load_datasets(size):
    """
        Loads all datasets into a single vector, along with the corresponding targets
        
        Parameters:
        -----------
        * size: tuple of int
          - Size to normalize bitmaps to

        Returns:
        --------
        * bitmaps: list of Bitmaps
          - All of the loaded shapes as Bitmaps
        * targets: list of strings
          - Dataset targets, in the "class target name" format
    """
    bitmaps, targets = [], []

    # loading mpeg7
    print("Loading MPEG7...", end=" ", flush=True)
    dataset = load_mpeg7()
    for bitmap, target in zip(dataset['bitmaps'][:210], dataset['targets'][:210]):
        bitmaps.append(bitmap.normalize(*size))
        targets.append(get_class_name("mpeg7", target))
    print("Done.")

    # loading fashion_mnist
    print("Loading Fashion_MNIST...", end=" ", flush=True)
    #dataset = load_fashion_mnist()
    #for bitmap, target in zip(dataset['bitmaps'], dataset['targets']):
    #    bitmaps.append(bitmap.normalize(*size))
    #    targets.append(get_class_name("fashion_mnist", target))
    print("Done.")

    # loading leaf
    print("Loading Leaf...", end=" ", flush=True)
    #dataset = load_leaf()
    #for bitmap, target in zip(dataset['bitmaps'], dataset['targets']):
    #    bitmaps.append(bitmap.normalize(*size))
    #    targets.append(get_class_name("leaf", target))
    print("Done.")

    # loading nist
    print("Loading NIST...", end=" ", flush=True)
    #dataset = load_nist()
    #for bitmap, target in zip(dataset['bitmaps'], dataset['targets']):
    #    bitmaps.append(bitmap.normalize(*size))
    #    targets.append(get_class_name("nist", target))
    print("Done.")

    return bitmaps, targets

def generate_synthetic_dataset(dataset_name, number_of_images, size_of_image, size_of_shape, shapes_per_image, dataset_distribution=(0.25,0.25,0.25,0.25), distortion_chance=0):
    """
        Generates a synthetic object matching dataset from the
        shapes in the included datasets, and stores it in a folder.
        Datasets will be generated as a set of numbered images,
        alongside a similarly-named text file containing the truth
        of each image (classes and central positions).

        Parameters:
        -----------
        * dataset_name: string
          - Name of the synthetic dataset to be generated. This is
            going to be the name of the folder. 
        * number_of_images: int
          - Number of images to be generated.
        * size_of_image: tuple
          - Image size as a tuple: `(width, height)`
        * size_of_shape: tuple
          - Shape size as a tuple: `(width, height)`
        * shapes_per_image: int, list of ints
          - Total of shapes per image. If given a list, each image
            will have a number of shapes randomly selected from the list.
        * dataset_distribution: tuple of 4 floats
          - Percentage of each dataset to be included as examples, as: 
            `(mpeg7, leaf, fashion_mnist, nist)` [not implemented]
        * distortion_chance: float
          - Percentual chance of applying distortion to a shape. [not implemented]
    """
    # If shapes_per_image is an int, convert it to list of single int
    if type(shapes_per_image) != list:
        shapes_per_image = [shapes_per_image] 

    # Generating output folder
    try:
        os.mkdir(dataset_name)
    except FileExistsError:
        pass

    # Loading datasets
    bitmaps, targets = load_datasets(size_of_shape)
    total_dataset = len(bitmaps)

    # Generating images
    print("\nGenerating images:\n")
    for i in range(number_of_images):
        print("On image {}".format(i))
        # Selecting shapes
        shapes_in_this_image = random.choice(shapes_per_image)
        indexes = random.sample(range(total_dataset), shapes_in_this_image)
        sampled_bitmaps, sampled_targets = [bitmaps[i] for i in indexes], [targets[i] for i in indexes]
        # Randomizing positions for each shape
        positions = [randomize_position(0, size_of_image[0]-bitmap.shape[0], 0, size_of_image[1]-bitmap.shape[1]) for bitmap in sampled_bitmaps]

        generated_image = generate_image(size_of_image, sampled_bitmaps, positions)
        generated_targets = "\n".join(["{} ({},{})".format(target, position[1] + int(bitmap.shape[1]/2), position[0] + int(bitmap.shape[0]/2)) for bitmap, target, position in zip(sampled_bitmaps, sampled_targets, positions)])

        plt.imsave(os.path.join(dataset_name, "{}.png".format(i)), generated_image, cmap="gray")
        open(os.path.join(dataset_name, "{}.txt".format(i)), "w").write(generated_targets)

#generate_synthetic_dataset("test", 2, (500,500), (50,50), 10)