from sarpy.datasets import load_emnist
from sarpy.datasets import sample
import numpy as np
import unittest

class DatasetsTest(unittest.TestCase):

    def test_sample(self):
        train_imgs, train_labels, test_imgs, test_labels, val_imgs, val_labels, _, n_classes = load_emnist('letters')

        train_red1, train_label_red1 = sample(train_imgs.copy(), train_labels.copy(), 15, n_classes, np.unique(train_labels))

        self.assertEqual((15*n_classes, *train_imgs.shape[1:]), train_red1.shape)

        train_red2, train_label_red2 = sample(train_imgs.copy(), train_labels.copy(), train_imgs.shape[0] + 10, n_classes, np.unique(train_labels))

        self.assertEqual(((train_imgs.shape[0] + 10)*n_classes, *train_imgs.shape[1:]), train_red2.shape)


    def test_load_emnist(self, mode='balanced', values={'train_imgs':(112800, 28, 28, 1),
                                                        'test_imgs':(18800, 28, 28, 1),
                                                        'val_imgs':None,
                                                        'train_labels':(112800, 1),
                                                        'test_labels':(18800, 1),
                                                        'val_labels':None,
                                                        'n_classes':47}):

        train_imgs, train_labels, test_imgs, test_labels, val_imgs, val_labels, _, n_classes = load_emnist(mode)

        self.assertEqual(train_imgs.shape, values['train_imgs'], 'train images wrong shape in ' + mode)
        self.assertEqual(test_imgs.shape, values['test_imgs'], 'test images wrong shape in ' + mode)
        self.assertEqual(val_imgs, values['val_imgs'], 'validation images should be None in ' + mode)
        self.assertEqual(train_labels.shape, values['train_labels'], 'train labels wrong shape in ' + mode)
        self.assertEqual(test_labels.shape, values['test_labels'], 'test labels wrong shape in ' + mode)
        self.assertEqual(val_labels, values['val_labels'], 'validation labels should be None in ' + mode)
        self.assertEqual(n_classes, values['n_classes'])


    def test_load_emnist_bymerge(self):
        self.test_load_emnist(mode='bymerge', values={'train_imgs':(697932, 28, 28, 1),
                                                        'test_imgs':(116322, 28, 28, 1),
                                                        'val_imgs':None,
                                                        'train_labels':(697932, 1),
                                                        'test_labels':(116322, 1),
                                                        'val_labels':None,
                                                        'n_classes':47})


    def test_load_emnist_digits(self):
        self.test_load_emnist(mode='digits', values={'train_imgs':(240000, 28, 28, 1),
                                                        'test_imgs':(40000, 28, 28, 1),
                                                        'val_imgs':None,
                                                        'train_labels':(240000, 1),
                                                        'test_labels':(40000, 1),
                                                        'val_labels':None,
                                                        'n_classes':10})


    def test_load_emnist_byclass(self):

        self.test_load_emnist(mode='byclass', values={'train_imgs':(697932, 28, 28, 1),
                                                        'test_imgs':(116322, 28, 28, 1),
                                                        'val_imgs':None,
                                                        'train_labels':(697932, 1),
                                                        'test_labels':(116322, 1),
                                                        'val_labels':None,
                                                        'n_classes':62})
    def test_load_emnist_letters(self):

        self.test_load_emnist(mode='letters', values={'train_imgs':(124800, 28, 28, 1),
                                                        'test_imgs':(20800, 28, 28, 1),
                                                        'val_imgs':None,
                                                        'train_labels':(124800, 1),
                                                        'test_labels':(20800, 1),
                                                        'val_labels':None,
                                                        'n_classes':26})
    def test_load_emnist_mnist(self):

        self.test_load_emnist(mode='mnist', values={'train_imgs':(60000, 28, 28, 1),
                                                        'test_imgs':(10000, 28, 28, 1),
                                                        'val_imgs':None,
                                                        'train_labels':(60000, 1),
                                                        'test_labels':(10000, 1),
                                                        'val_labels':None,
                                                        'n_classes':10})
