import os
import numpy as np
from skimage import io
import binascii

# Root directory for this package
root_directory = os.path.dirname(__file__)

def load_nist19():
        # directory_class = os.path.join(root_directory,'nist19_by_class')
        directory_class = os.path.join(root_directory,'by_class')
        list_of_class = os.listdir(directory_class)
        list_of_class.sort()

        data    = [];
        targets = [];
        names   = [];
        id_class = 0;
        for a_class in list_of_class:
                num_images_save = 0
                print(binascii.unhexlify(a_class).decode('UTF-8'),end='');
                directory_subclass = os.path.join(directory_class,a_class)
                list_of_subclass = [fn for fn in os.listdir(directory_subclass) if ("train" in fn)]
                # list_of_subclass = [fn for fn in os.listdir(directory_subclass) if ("hsf" in fn)]
                sorted(list_of_subclass)
                for folder_of_images in list_of_subclass:
                        directory_of_images = os.path.join(directory_subclass,folder_of_images)
                        list_of_images = os.listdir(directory_of_images)
                        sorted(list_of_images)
                        for filename in list_of_images:
                                data.append(io.imread(os.path.join(directory_of_images,filename)));
                                targets.append(id_class);
                                num_images_save += 1
                                #--
                                if (num_images_save == 1000):
                                        break;
                                #--
                print(' - ',num_images_save)
                id_class += 1
                names.append(binascii.unhexlify(a_class).decode('UTF-8'));

        print(len(data))

        return {'bitmaps': data, 'targets':targets,'names':names}

print('Load dataset')
dataset = load_nist19()
bitmaps=dataset['bitmaps']
targets=dataset['targets']
names = dataset['names'];
np.savez_compressed('train_nist19_bitmaps',bitmaps=bitmaps);
np.savez_compressed('train_nist19_targets',targets=targets);
np.savez_compressed('train_nist19_names',names=names);
