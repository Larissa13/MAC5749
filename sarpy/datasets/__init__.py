"""
This module contains utilities to load datasets,
and includes some in-built datasets. Based on:
https://github.com/scikit-learn/scikit-learn/tree/master/sklearn/datasets
"""

from .datasets import load_mpeg7, load_nist, load_leaf, load_fashion_mnist, get_class_name, load_emnist
from .utils import sample

__all__ = ['load_mpeg7', 'get_class_name', 'load_nist', 'load_leaf', 'load_fashion_mnist', 'load_emnist']
