import numpy as np

filename = 'mnist_test.csv'
def get_data(filename):
    '''
    Edit the data using the numpy genfromtxt() function.
  
    Parametrs:
        str: filename
    returns:
        Numpy array: array
  '''
    data = np.genfromtxt(filename,delimiter=',',dtype=np.int64)
    dataset = np.array([np.reshape(row[1:],(28,28)) for row in data])
    print(dataset[0].ndim)

get_data(filename)