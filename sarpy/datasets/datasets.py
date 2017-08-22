"""
Methods for loading and returning in-built datasets.
"""

import os
import numpy as np
from skimage import io
import pandas as pd

# Root directory for this package
root_directory = os.path.dirname(__file__)

def load_mpeg7():
    """Loads the MPEG7 Shape dataset, containing 1400 images of
    70 classes (20 images per class).
    Returns
    -------
    dataset : dict
        Dictionary object, the interesting attributes are: 'bitmaps',
        a vector of the images of the dataset as 2D NumPy arrays,
        and 'targets', a vector of the target/class of each image.
    """
    # List of image file names
    dataset_directory = os.path.join(root_directory,'MPEG7')
    filenames = os.listdir(dataset_directory)
    filenames.sort()

    # List of numpy array; each row is a Image of the dataset
    data = []

    # Numpy array of labels associated to each class of image
    target = np.empty([len(filenames), ])

    previous_label = ''
    class_num = -1
    index = 0

    for index, filename in enumerate(filenames):
        data.append(io.imread(os.path.join(dataset_directory, filename)))
        file_label = filename.split('-')[0]
        
        if(previous_label != file_label):
            previous_label = file_label
            class_num += 1
            target[index] = class_num
        else:
            target[index] = class_num

    return {'bitmaps': data, 'targets': target}

def load_mnist():
    """Loads the MNIST character dataset. [add more info!]
    Returns
    -------
    dataset : dict
        Dictionary object, the interesting attributes are: 'bitmaps',
        a vector of the images of the dataset as 2D NumPy arrays,
        and 'targets', a vector of the target/class of each image.
    """
    dataset_directory = os.path.join(root_directory,'MNIST')
    MNIST_dataset = pd.read_csv(os.path.join(dataset_directory,'MNIST.csv'))
    X = MNIST_dataset.iloc[0:5000,1:]
    y = MNIST_dataset.iloc[0:5000,:1]

    return {'bitmaps': X, 'targets': y}

def load_nist():
    """Loads the NIST character dataset. [add more info]
    Returns
    -------
    dataset : dict
        Dictionary object, the interesting attributes are: 'bitmaps',
        a vector of the images of the dataset as 2D NumPy arrays,
        and 'targets', a vector of the target/class of each image.
    """

    return {'bitmaps': None, 'targets': None}