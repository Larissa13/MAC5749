"""
Methods for loading and returning built-in datasets.
"""

import os
import numpy as np
from skimage import io
import binascii

from sarpy.representations import Bitmap

# Root directory for this package
root_directory = os.path.dirname(__file__)

def get_class_name(dataset, target):
    """
    Returns the human-readable name of a given target number in a given dataset.
    Parameters
    ----------
    dataset: {'mpeg7', 'leaf', 'nist', or 'fashion_mnist'
        name of the target dataset
    target : int
        target representing the target/class label.
    Returns
    -------
    label : string
        return label of the target.
    """
    if dataset == "mpeg7":
        if target == 0: return "Bone"
        if target == 1: return "Comma"
        if target == 2: return "Glas"
        if target == 3: return "HCircle"
        if target == 4: return "Heart"
        if target == 5: return "Misk"
        if target == 6: return "apple"
        if target == 7: return "bat"
        if target == 8: return "beetle"
        if target == 9: return "bell"
        if target == 10: return "bird"
        if target == 11: return "bottle"
        if target == 12: return "brick"
        if target == 13: return "butterfly"
        if target == 14: return "camel"
        if target == 15: return "car"
        if target == 16: return "carriage"
        if target == 17: return "cattle"
        if target == 18: return "cellular_phone"
        if target == 19: return "chicken"
        if target == 20: return "children"
        if target == 21: return "chopper"
        if target == 22: return "classic"
        if target == 23: return "crown"
        if target == 24: return "cup"
        if target == 25: return "deer"
        if target == 26: return "device0"
        if target == 27: return "device1"
        if target == 28: return "device2"
        if target == 29: return "device3"
        if target == 30: return "device4"
        if target == 31: return "device5"
        if target == 32: return "device6"
        if target == 33: return "device7"
        if target == 34: return "device8"
        if target == 35: return "device9"
        if target == 36: return "dog"
        if target == 37: return "elephant"
        if target == 38: return "face"
        if target == 39: return "fish"
        if target == 40: return "flatfish"
        if target == 41: return "fly"
        if target == 42: return "fork"
        if target == 43: return "fountain"
        if target == 44: return "frog"
        if target == 45: return "guitar"
        if target == 46: return "hammer"
        if target == 47: return "hat"
        if target == 48: return "horse"
        if target == 49: return "horseshoe"
        if target == 50: return "jar"
        if target == 51: return "key"
        if target == 52: return "lizzard"
        if target == 53: return "lmfish"
        if target == 54: return "octopus"
        if target == 55: return "pencil"
        if target == 56: return "personal_car"
        if target == 57: return "pocket"
        if target == 58: return "rat"
        if target == 59: return "ray"
        if target == 60: return "sea_snake"
        if target == 61: return "shoe"
        if target == 62: return "spoon"
        if target == 63: return "spring"
        if target == 64: return "stef"
        if target == 65: return "teddy"
        if target == 66: return "tree"
        if target == 67: return "truck"
        if target == 68: return "turtle"
        if target == 69: return "watch"

    if dataset == "leaf":
        if target == 0: return "Acer_Capillipes"
        if target == 1: return "Betula_Austrosinensis"
        if target == 2: return "Castanea_Sativa"
        if target == 3: return "Eucalyptus_Glaucescens"
        if target == 4: return "Fagus_Sylvatica"
        if target == 5: return "Ginkgo_Biloba"
        if target == 6: return "Ilex_Aquifolium"
        if target == 7: return "Liquidambar_Styraciflua"
        if target == 8: return "Magnolia_Heptapeta"
        if target == 9: return "Olea_Europaea"
        if target == 10: return "Populus_Adenopoda"
        if target == 11: return "Quercus_Afares"
        if target == 12: return "Rhododendron_x_Russellianum"
        if target == 13: return "Salix_Fragilis"
        if target == 14: return "Tilia_Oliveri"
        if target == 15: return "Ulmus_Bergmanniana"
        if target == 16: return "Viburnum_x_Rhytidophylloides"
        if target == 17: return "Zelkova_Serrata"

    if dataset == "fashion_mnist":
        if target == 0: return "Ankle_boot"
        if target == 1: return "Bag"
        if target == 2: return "Coat"
        if target == 3: return "Dress"
        if target == 4: return "Pullover"
        if target == 5: return "Sandal"
        if target == 6: return "Shirt"
        if target == 7: return "Sneaker"
        if target == 8: return "T_shirt"
        if target == 9: return "Trouser"

    if dataset == "nist":
        if target == 0: return "0"
        if target == 1: return "1"
        if target == 2: return "2"
        if target == 3: return "3"
        if target == 4: return "4"
        if target == 5: return "5"
        if target == 6: return "6"
        if target == 7: return "7"
        if target == 8: return "8"
        if target == 9: return "9"
        if target == 10: return "A"
        if target == 11: return "B"
        if target == 12: return "C"
        if target == 13: return "D"
        if target == 14: return "E"
        if target == 15: return "F"
        if target == 16: return "G"
        if target == 17: return "H"
        if target == 18: return "I"
        if target == 19: return "J"
        if target == 20: return "K"
        if target == 21: return "L"
        if target == 22: return "M"
        if target == 23: return "N"
        if target == 24: return "O"
        if target == 25: return "P"
        if target == 26: return "Q"
        if target == 27: return "R"
        if target == 28: return "S"
        if target == 29: return "T"
        if target == 30: return "U"
        if target == 31: return "V"
        if target == 32: return "W"
        if target == 33: return "X"
        if target == 34: return "Y"
        if target == 35: return "Z"
        if target == 36: return "a"
        if target == 37: return "b"
        if target == 38: return "c"
        if target == 39: return "d"
        if target == 40: return "e"
        if target == 41: return "f"
        if target == 42: return "g"
        if target == 43: return "h"
        if target == 44: return "i"
        if target == 45: return "j"
        if target == 46: return "k"
        if target == 47: return "l"
        if target == 48: return "m"
        if target == 49: return "n"
        if target == 50: return "o"
        if target == 51: return "p"
        if target == 52: return "q"
        if target == 53: return "r"
        if target == 54: return "s"
        if target == 55: return "t"
        if target == 56: return "u"
        if target == 57: return "v"
        if target == 58: return "w"
        if target == 59: return "x"
        if target == 60: return "y"
        if target == 61: return "z"

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
        data.append(Bitmap(io.imread(os.path.join(dataset_directory, filename))))
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

    # List of bitmap Shapes; each row is a Image of the dataset
    data = []

    # Numpy array of labels associated to each class of image
    target = np.empty([len(filenames), ])

    previous_label = ''
    class_num = -1
    index = 0

    for index, filename in enumerate(filenames):
        data.append(Bitmap(io.imread(os.path.join(dataset_directory, filename))))
        file_label = filename.split('-')[0]

        if(previous_label != file_label):
            previous_label = file_label
            class_num += 1
            target[index] = class_num
        else:
            target[index] = class_num

    return {'bitmaps': data, 'targets': target}

def load_fashion_mnist():
    """Loads the Fashion MNIST dataset

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
        data.append(Bitmap(io.imread(os.path.join(dataset_directory, filename))))
        file_label = filename.split('-')[0]

        if(previous_label != file_label):
            previous_label = file_label
            class_num += 1
            target[index] = class_num
        else:
            target[index] = class_num

    return {'bitmaps': data, 'targets': target}

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
                                    bitmaps.append(Bitmap(img.astype(np.int8)))
                                    targets.append(id_class);
                    id_class += 1
                    names.append(binascii.unhexlify(a_class).decode('UTF-8'));


    return {'bitmaps': bitmaps, 'targets': targets, 'names':names}
