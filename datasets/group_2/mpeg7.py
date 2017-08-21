import os
import numpy as np
from skimage import io
from dataset import Dataset

# Path to the MPEG7 dataset files
path = '../datasets/group_2/MPEG7'

def load_mpeg7_images():
	# List of image file names
	filename = os.listdir(path)
	filename.sort()

	# List of numpy array; each row is a Image of the dataset
	data = []

	# Numpy array of labels associated to each class of image
	target = np.empty([len(filename), ])

	label = ''
	class_num = -1
	index = 0

	for file in filename:
		try:
			data.append(io.imread(path + '/' + file))
			tmp = file.split('-')
			
			if(label != tmp[0]):
				label = tmp[0]
				class_num += 1
				target[index] = class_num
			else:
				target[index] = class_num
			index += 1

		except OSError:
			print('Cannot identify image file ' + file)

	return(Dataset(data, target))