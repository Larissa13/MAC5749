import os
import numpy as np
from skimage import io

# Path to the MPEG7 dataset files
path = './MPEG7'

def load_mpeg7_images():
	# List of image file names
	filename = os.listdir(path)
	filename.sort()

	# List of numpy array; each row is a Image of the dataset
	data = []

	# Numpy array of labels associated to each class of image
	target = np.empty(len(filename), dtype='uint8')

	previous_label = ''
	class_num = -1
	index = 0

	for index, file in enumerate(filename):
		data.append(io.imread(os.path.join(path, file)))
		file_label = file.split('-')[0]
		
		if(previous_label != file_label):
			previous_label = file_label
			class_num += 1
			target[index] = class_num
		else:
			target[index] = class_num

	return data, target