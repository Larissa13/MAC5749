'''Functions to Add noise to images.'''

import numpy as np

def poisson_noise(images, peak=10):
    '''
    Returns images with poisson noise applied to them.
    Input:
    - images (iterable): Dataset of images.
    - peak (float): Noise magnitude.
    '''
    noisy = []
    for image in images:
        noisy += [np.random.poisson(image/255.0*peak)/peak*255]

    return np.array(noisy)


def gaussian_noise(images, var=10):
    '''
    Returns images with gaussian noise applied to them.
    Input:
    - images (iterable): Dataset of images.
    - var (float): Variance.
    '''
    noisy = []
    for image in images:
        noise = np.random.randn(*image.shape)*var
        noisy += [image + noise]

    return np.array(noisy)

