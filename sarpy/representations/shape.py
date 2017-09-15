"""
The "Shape" general object is a catch-all for representing the many types
of possible shape representations, allowing a degree of abstraction to the user,
and making some of the conversions transparent when possible.
"""
import numpy as np

class Shape:
    def __init__(self, data):
        pass

    # Overloads
    def __len__(self):
        return len(self.data)
    def __getitem__(self, key):
        return self.data[key]
    def __setitem__(self, key, value):
        self.data[key] = value
    def all(self, axis=None, out=None, keepdims=False):
        return self.data.all(axis, out, keepdims)
    def any(self, axis=None, out=None, keepdims=False):
        return self.data.any(axis, out, keepdims)

    def scale(self, c, center=(0,0)):
        raise NotImplementedError()
        pass

    def shift(self, c):
        raise NotImplementedError()
        pass

    def to_bitmap(self):
        raise NotImplementedError()
        pass

    def to_pointSet(self):
        raise NotImplementedError()
        pass

    def to_contours(self):
        raise NotImplementedError()
        pass
