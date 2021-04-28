import numpy as np

filename = 'mnist_test.csv'
def get_data(filename):
    '''
    Edit the data using the numpy genfromtxt() function.
  
    Parametrs:
        str: filename
    returns:
        Numpy array: array,label and dataset
  '''
    data = np.genfromtxt(filename,delimiter=',',dtype=np.int64)
    dataset = np.array([np.reshape(row[1:],(28,28)) for row in data])
    label = np.array([row[0] for row in data])
    
    return label,dataset

print(get_data(filename)[0][0])