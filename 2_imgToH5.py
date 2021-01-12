import h5py, math
import numpy as np
from glob import glob 
import cv2

"""
creates training datasets from the images
"""

src = {
        "cat":"images/raw/cats/*.jpg", 
        "elephant":"images/raw/elephants/*.jpg"
        }

outfile = "images/clean/datasets.hdf5" 

def splitAt(imgs):
    """
    finds a good number to divide the array
    input: array of images
    """
    return math.ceil(len(imgs) - math.sqrt(len(imgs)))

def zeros_or_ones(arr, one=True):
    if(one==True):
        return np.ones(len(arr), dtype="uint8")
    else:
        return np.zeros(len(arr), dtype="uint8")

def split_data(src=src, p="cat", n="elephant"):
  """ 
  we want to divide the images in 2 groups, 
  test / train, at the magic number 
  src: object with path to positive "p" and negative "n"
  returns an object with all the arrays in right order
  """
  # all images
  p = glob(src[p])
  n = glob(src[n])

  # fine good numbers to split the arrays
  magic_p = splitAt(p)
  magic_n = splitAt(n)

  #make test and train arrays
  p_test = p[magic_p:]; p_train = p[0:magic_p]
  n_train = n[0:magic_n]; n_test = n[magic_n:]
 
 # create arrays of zeros or ones for n or p
  ones_train = zeros_or_ones(p_train)
  ones_test = zeros_or_ones(p_test)
  zeros_train = zeros_or_ones(n_train)
  zeros_test = zeros_or_ones(n_test)
  
  # create labels arrays
  features_train = np.concatenate((p_train, n_train))
  features_test = np.concatenate((p_test, n_test))
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
               

def make_train_dset(src=src, out=outfile, p="cat", n="elephant"):

    with h5py.File(outfile, "w") as f:

    # Dictionary
      Pointers = split_data(src, p="cat", n="elephant")
      
      features_train = []
      features_test = []
      for key in Pointers.keys(): # train or test
          if(key=="train"):
              for img in Pointers[key]["features"]:
                  thisImage = cv2.imread(img) 
                  features_train.append(thisImage) # narray 200x200x3
          else:
              for img in Pointers[key]["features"]:
                  thisImage = cv2.imread(img) 
                  features_test.append(thisImage) 
     # save dataset 
      f.create_dataset("train_X", data=features_train) 
      f.create_dataset("train_Y", data=Pointers["train"]["labels"]) 
      f.create_dataset("test_X", data=features_test) 
      f.create_dataset("test_Y", data=Pointers["test"]["labels"]) 
      f.create_dataset("classes", data=[n, p])

make_train_dset()
