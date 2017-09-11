import os
import numpy as np
from skimage import io
import binascii

# Root directory for this package
root_directory = os.path.dirname(__file__)

print('Read data')
bitmaps = np.load('train_nist19_bitmaps.npz')['bitmaps']
#bitmaps = [0];
targets = np.load('train_nist19_targets.npz')['targets']
names   = np.load('train_nist19_names.npz')['names']
print(len(bitmaps),len(targets),len(names))
print(type(bitmaps[0]),type(targets[0]),type(names[0]));
print(names)
