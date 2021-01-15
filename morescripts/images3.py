# Using H5
import h5py
import matplotlib.pyplot as plt
f = h5py.File('../images/clean/datasets.hdf5', 'r')

# file objects have keys() method:
print("datasets are: ", f.keys())

# we can access one dataset, example:
pics = f['train_X']
print(pics.shape) # 279 pictures, 200x200, RGB

OnePic = pics[0]
plt.imshow(OnePic)
plt.show()
