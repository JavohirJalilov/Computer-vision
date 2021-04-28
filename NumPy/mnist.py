import numpy as np

filename = 'mnist_test.csv'
data = np.genfromtxt(filename,delimiter=',')
print(data[0])