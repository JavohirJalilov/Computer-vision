import numpy as np
import matplotlib.pyplot as plt
from mnist import get_data
filename = 'mnist_test.csv'

def imshow_data(label:np.ndarray,dataset:np.ndarray)->None:
    plt.figure(figsize=(7,10))
    for i in range(1,10):
        plt.subplot(3,3,i)
        plt.title(f'label = {label[i]}',pad=10)
        plt.imshow(dataset[i],cmap='gray')
        plt.axis('off')
    plt.show()

label,dataset = get_data(filename)
imshow_data(label,dataset)