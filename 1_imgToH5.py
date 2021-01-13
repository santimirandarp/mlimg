import h5py # CRUD binary files
import math
import numpy as np # linear algebra
from glob import glob # get data path/names
import cv2 # CRUD images

"""
creates training datasets from features(images) & labels
"""

src = { # path to each feature set
        "one":"images/raw/cats/*.jpg", 
        "zero":"images/raw/elephants/*.jpg"
        }

outfile = "images/clean/datasets.hdf5" 

def splitAt(imgs):
    """
    split array at sqrt(length)
    input: array of images
    """
    return math.ceil(len(imgs) - math.sqrt(len(imgs)))

def zeros_or_ones(arr, ones=True):
    if(ones==True):
        return np.ones(len(arr), dtype="uint8")
    else:
        return np.zeros(len(arr), dtype="uint8")

def split_data(src=src):
  """ 
  we want to divide the images in 2 groups, 
  test / train, at the magic number 
  src: object with path to positive "p" and negative "n"
  returns an object with all the arrays in right order
  """
  # array of imgs
  one = glob(src["one"])
  zero = glob(src["zero"])

  # find good numbers to split the arrays
  magic_1 = splitAt(one)
  magic_0 = splitAt(zero)

  # make test and train arrays
  one_test = one[magic_1:]; one_train = one[0:magic_1]
  zero_train = zero[0:magic_0]; zero_test = zero[magic_0:]
 
 # create arrays of zeros or ones
  ones_train = zeros_or_ones(one_train)
  ones_test = zeros_or_ones(one_test)
  zeros_train = zeros_or_ones(zero_train, False)
  zeros_test = zeros_or_ones(zero_test, False)
  
  # create labels arrays
  features_train = np.concatenate((ones_train, zeros_train))
  features_test = np.concatenate((ones_test, zeros_test))
  labels_train = np.concatenate((ones_train, zeros_train))
  labels_test = np.concatenate((ones_test, zeros_test))
  return {
          "test":{ 
              "labels": labels_test, 
              "features": features_test
              },
           "train":{ 
               "labels": labels_train,
               "features": features_train
               }
           }
               

def make_all_dset(src=src, out=outfile, one="cat", zero="elephant"):

    with h5py.File(outfile, "w") as f:

      Pointers = split_data(src) # Dictionary
      
      features_train = []
      features_test = []

      for img in Pointers["train"]["features"]:
          thisImage = cv2.imread(img) 
          features_train.append(thisImage) 

      for img in Pointers["test"]["features"]:
          thisImage = cv2.imread(img) 
          features_test.append(thisImage) 

     # save dataset 
      f.create_dataset("train_X", data=features_train) 
      f.create_dataset("train_Y", data=Pointers["train"]["labels"]) 
      f.create_dataset("test_X", data=features_test) 
      f.create_dataset("test_Y", data=Pointers["test"]["labels"]) 
      f.create_dataset("classes", data=[zero, one])

make_all_dset()
