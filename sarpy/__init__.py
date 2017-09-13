"""
Shape Analysis & Recognition module
===================================
[module description goes here]

Requires:
- NumPy
- Pandas
- Scikit Image
"""

from .transformations import shape_scale, shape_shift
from .conversions import convert_shape

__all__ = ['datasets', 'utils', 'shape_scale', 'shape_shift', 'convert_shape']