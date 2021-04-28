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
    print(data[0])

get_data(filename)