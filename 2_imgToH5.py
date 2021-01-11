import h5py
import numpy as np
from glob import glob # import "submodule"
from PIL import Image
import matplotlib.pyplot as plt

# img source directory
src = "images/raw/cats/*"

# self explanatory
outfile = "images/clean/cat.hdf5" 


listOfImages = glob(src)

# img loaded as JpegImageFile Object
oneImage = Image.open(listOfImages[0])

# open file
f = h5py.File(outfile, "w")
data  =  np.array(oneImage) #this is an array 200x200x3

# save dataset (ndarray but with more features)
dset = f.create_dataset("images", data=data) # array 200x200x3

# Check if files can be read from the h5py file
with h5py.File(outfile, "r") as f:
    image = f['images']
    print(image.shape, image.dtype)
    plt.imshow(image)
    plt.show()

