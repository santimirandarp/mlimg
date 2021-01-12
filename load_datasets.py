
outfile = "images/clean/datasets.hdf5" 

def load_datasets(outfile=outfile):
    with h5py.File(outfile, "r") as f:
        train_set_X = np.array(f['train_X'])
        train_set_Y = np.array(f['train_Y'])
        train_set_Y = train_set_Y.reshape((1, train_set_Y.shape[0])) 
        test_set_X = np.array(f['test_X'])
        test_set_Y = np.array(f['test_Y'])
        test_set_Y = test_set_Y.reshape((1, test_set_Y.shape[0])) 
#        classes = f['classes']
        print(train_set_Y.shape, train_set_X.shape)
        return train_set_X, train_set_Y, test_set_X, test_set_Y#, classes 


