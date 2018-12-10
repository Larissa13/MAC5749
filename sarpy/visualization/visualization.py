"""
Methods for visualizing dataset content and analise performance
"""

import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
from skimage.measure import label

def get_examples(labels, classes, num_rows, at_random):
    '''
    Returns chosen samples indexes from the dataset.
    Input:
    - labels (numpy array): Dataset's images corresponding labels.
    - classes (iterable): Possible values a label can assume.
    - num_rows (int): Number of samples of each class that should be chosen.
    - at_random (boolean): If the samples should be chosen at random or sequentially.
    '''

    samples = []
    for cls in classes:
        cls_rows = np.where(labels == cls)[0]

        if num_rows is None:
            num_cls_samples = len(cls_rows)
        else:
            num_cls_samples = min(num_rows, len(cls_rows))

        if at_random:
            cls_rows = np.random.permutation(cls_rows)

        cls_rows = cls_rows[:num_cls_samples]

        samples.append(cls_rows)

    return samples


def build_mosaic_header(class_names, shape):
    '''
    Returns the upper part of the mosaic, containing the label of images below.
    Input:
    - class_names (iterable): Iterable of strings containing each label's name.
    - shape (tuple): Tuple o ints containing images size and number of channels.
    '''

    image_height, image_width, channels = shape
    mosaic_header = np.zeros((image_height, len(class_names)*image_width, channels), dtype=np.uint8)

    font = cv.FONT_HERSHEY_SIMPLEX
    font_scale = 0.8
    font_color = [255] * channels
    line_type = 2

    for cls_id in range(len(class_names)):
        cv.putText(mosaic_header, class_names[cls_id][1], (cls_id*image_width, image_height//2),
                   font, font_scale, font_color, line_type)

    return mosaic_header


def mosaic(images,
           labels,
           classes = None,
           class_names = None,
           image_size = (100, 100),
           num_rows = 6,
           at_random = False,
           display = False):
    '''
    Returns an image composed of num_rows examples of images of each class, forming a grid og images.
    Input:
    - images (numpy array): The images dataset.
    - labels (numpy array): Labels corresponding to the images in the dataset. There must be the same number of labels as the number of images.
    - classes (iterable): Possible labels.
    - class_names (iterable): Name of possible labels.
    - image_size (tuple): A tuple of format (height, width) containing the size of the images in the dataset.
    - num_rows (int): Number indicating number of examples of each image that should compose the mosaic.
    - at_random (boolean): If the samples hould be chosen at random or sequentially.
    - display (boolean): If the resulting mosaic should be displayed or not.
    '''


    if len(images) != len(labels):
        raise Exception('Mismatch between number of images and labels')

    if classes is None:
        classes = np.unique(labels)

    samples = get_examples(labels, classes, num_rows, at_random)

    max_num_images = max([len(cls_samples) for cls_samples in samples])
    image_height, image_width = image_size

    channels = 3 if len(images[0].shape) == 3 else 1
    mosaic = np.zeros((max_num_images*image_height, len(classes)*image_width, channels), dtype=np.uint8)
    for column, cls_samples in enumerate(samples):

        image_samples = [cv.resize(img, (image_width, image_height)) for img in images[cls_samples]]
        image_samples = np.array(image_samples).reshape((-1, image_width, channels))
        mosaic[0:image_width*len(image_samples), column*image_width:(column+1)*image_width, :] = image_samples

    # Labels de título
    if class_names is not None:
        mosaic_header = build_mosaic_header(class_names, (image_height, image_width, channels))
        mosaic = np.concatenate((mosaic_header, mosaic), axis=0)

    if channels == 1:
        mosaic = mosaic.reshape((mosaic.shape[0], mosaic.shape[1]))

    if display:
        cv.imshow('Image', mosaic)
        cv.waitKey(0)
        cv.destroyAllWindows()

    return mosaic


def hist_components(imgs, text, show=True):
    '''
    Returns a plot showing the frequency of images with number of connected components n, for each n possible in the dataset.
    Input:
    - imgs (iterable): Images dataset.
    - text (string): Plot title.
    - show (boolean): If the resulting histogram should be displayed or not.
    '''

    new_imgs = [label(img) for img in imgs]
    comps = [np.max(new_img) for new_img in new_imgs]

    if show:
        plt.hist(comps)
        plt.title(text)
        plt.show()

    return comps


def visual_describe():
    pass



