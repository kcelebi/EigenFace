import numpy as np
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import os
from tqdm import tqdm
from random mport sample

# -------

import sys
sys.path.append('../src/')

def load_image(file):
	img = mpimg.imread(file) #read img
	R,G,B = img.T #get RGB comps
	#Transform to Grayscale and reshape to n*nx1 vector
	grayscale = (0.2989 * R + 0.5870 * G + 0.1140 * B).T
	ds = down_sample(grayscale)
	return np.reshape(ds, -1)

 def down_sample(imgArray):
	img_ds = np.zeros((50,50))
	for i in range(50):
		for j in range(50):
			img_ds[i,j] = np.mean(imgArray[i*5:(i+1)*5, j*5:(j+1)*5])
	return img_ds

def getZ(files, mean_centered = True, size = 2500):
	Z = np.zeros((len(files), size)) #Empty Data matrix of numFiles x imgVectorSize
	for idx, file in enumerate(tqdm(files)):
		Z[idx] = load_image(file) #put to Z
	
	if mean_centered:
		#Subtract mean 'face'
		Z -= np.mean(Z, axis=0)
	return Z

def get_all_files(root = 'face_data'):
	files = []
	for file in os.listdir(root):
		files.extend([root + '/' + file + '/' + f for f in os.listdir(root + '/' + file)])
	
	return files


def test_train_split(p = 0.6):
	files = get_all_files()
	
	test = sample(files, int(p*len(files)))
	train = [f for f in files if f not in test]
	
	return test, train