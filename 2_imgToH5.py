import h5py
import numpy as np
from glob import glob 
import cv2
import matplotlib.pyplot as plt

"""
this is part of the execution,
creates training datasets from the images
"""

src = {
        "cat":"images/raw/cats/*.jpg", 
        "elephant":"images/raw/elephants/*.jpg"
        }
outfile = "images/clean/train_datasets.hdf5" 

def make_train_dset(srcdir=src, out=outfile, p="cat", n="elephant"):

    with h5py.File(outfile, "w") as f:

      p = glob(src[p]); n = glob(src[n])

      # set the arrays of ones and zeros
      ones = np.ones(len(p), dtype="uint8")
      zeros = np.zeros(len(n), dtype="uint8")
      labels = np.concatenate((ones, zeros))
      counter = 0
      features = [] 
      for key in src.keys():
        for img in glob(src[key]):
          thisImage = cv2.imread(img) 
          features.append(thisImage) # narray 200x200x3

     # save dataset 
      f.create_dataset("train_X", data=features) 
      f.create_dataset("train_Y", data=labels) 

def load_datasets(outfile=outfile):
    with h5py.File(outfile, "r") as f:
        features = f['train_X']
        labels = f['train_Y']
        print(features, labels)
        #plt.imshow(image)
        #plt.show()

make_train_dset()

load_datasets()
