"""
Methods for loading and returning in-built datasets.
"""

import os
import numpy as np
from skimage import io
import pandas as pd
import binascii

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


def load_leaf():
    """Loads the Leaf Shape dataset

Returns
    -------
    dataset : dict
        Dictionary object, the interesting attributes are: 'bitmaps',
        a vector of the images of the dataset as 2D NumPy arrays,
        and 'targets', a vector of the target/class of each image.
    """
    # List of image file names
    dataset_directory = os.path.join(root_directory,'Leaf_2')
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

def load_fashion_mnist():
    """Loads the Leaf Shape dataset

Returns
    -------
    dataset : dict
        Dictionary object, the interesting attributes are: 'bitmaps',
        a vector of the images of the dataset as 2D NumPy arrays,
        and 'targets', a vector of the target/class of each image.
    """
    # List of image file names
    dataset_directory = os.path.join(root_directory,'Fashion_MNIST')
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

def load_nist(block=0):
    """Loads the NIST character dataset. [add more info]
    Parameters
    ----------
        block : int
            size of database loaded, 
                0 - "100 images by class"       -> total 6200
                1 - "1000 images by class"      -> total 62000
                2 - "max 10000 images by class" -> total 397621 images

    Returns
    -------
    dataset : dict
        Dictionary object, the interesting attributes are: 'bitmaps',
        a vector of the images of the dataset as 2D NumPy arrays,
        and 'targets', a vector of the target/class of each image.
    """
    dataset_directory = os.path.join(root_directory,'NIST19')    
    if(block == 2):
        bitmaps = np.load(dataset_directory+'/train_nist19_bitmaps_lim10000.npz')['bitmaps']
        targets = np.load(dataset_directory+'/train_nist19_targets_lim10000.npz')['targets']
        names   = np.load(dataset_directory+'/train_nist19_names_lim10000.npz')['names']        
    else:
        if(block == 1):
            bitmaps = np.load(dataset_directory+'/train_nist19_bitmaps_1000.npz')['bitmaps']
            targets = np.load(dataset_directory+'/train_nist19_targets_1000.npz')['targets']
            names   = np.load(dataset_directory+'/train_nist19_names_1000.npz')['names']
        else:
            directory_class = os.path.join(dataset_directory,'by_class')    
            list_of_class = os.listdir(directory_class)
            list_of_class.sort()
            bitmaps = [];
            targets = [];
            names   = [];
            id_class = 0;

            for a_class in list_of_class:                
                    directory_subclass = os.path.join(directory_class,a_class)
                    list_of_subclass = [fn for fn in os.listdir(directory_subclass) if ("train" in fn)]
                    sorted(list_of_subclass)
                    for folder_of_images in list_of_subclass:
                            directory_of_images = os.path.join(directory_subclass,folder_of_images)
                            list_of_images = os.listdir(directory_of_images)
                            sorted(list_of_images)
                            for filename in list_of_images:
                                    img = np.where(io.imread(os.path.join(directory_of_images,filename),True) > 0, 0, 1)                                    
                                    bitmaps.append(img.astype(np.int8))
                                    targets.append(id_class);
                    id_class += 1
                    names.append(binascii.unhexlify(a_class).decode('UTF-8'));        
            
    
    return {'bitmaps': bitmaps, 'targets': targets, 'names':names}

