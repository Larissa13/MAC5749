'''Some useful functions to handle and transform datasets'''
import numpy as np


def sample(data, labels, n_samples, n_class, mapping):
    '''
    Returns a class balanced partition of the dataset of size n_class*n_samples

    Input:
    - data (numpy array): data to partition.
    - labels (numpy array): classes corresponding to data (if data is of shape (n, ?, ..., ?), labels must have shape (n,)).
    - n_samples (int): Wished resulting number of samples for each class.
    - n_class (int): Number of classes present in dataset.
    - mapping (iterable): Iterable containing classes.
    '''

    images_class = []
    for class_ in mapping:
        images_class += [np.where(labels == class_)[0]]

    data_red = []
    label_red = []
    for class_ in images_class:
        index_class = np.random.choice(class_, n_samples, replace=False)
        data_red += [data[index_class]]
        label_red += [labels[class_[0]]]*n_samples

    data_red = np.array(data_red).reshape((n_samples*n_class, 28, 28))
    label_red = np.array(label_red)

    return data_red, label_red
