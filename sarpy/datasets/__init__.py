"""
This module contains utilities to load datasets,
and includes some in-built datasets. Based on:
https://github.com/scikit-learn/scikit-learn/tree/master/sklearn/datasets
"""

from .datasets import load_mpeg7, load_nist, load_leaf, load_fashion_mnist, mpeg7_get_class_name

__all__ = ['load_mpeg7', 'mpeg7_get_class_name', 'load_nist', 'load_leaf', 'load_fashion_mnist']
