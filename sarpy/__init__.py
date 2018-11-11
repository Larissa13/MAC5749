"""
Shape Analysis & Recognition module
===================================
[module description goes here]

Requires:
- NumPy
- Pandas
- Scikit Image
"""

from .representations import *
from .datasets import *
from .visualization import *

__all__ = ['representations', 'datasets', 'visualization', 'plotContour', 'plotContour1D']
