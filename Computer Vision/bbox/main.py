import matplotlib.pyplot as plt
import numpy as np
import cv2

points_arr = np.genfromtxt('bbox_road.csv',delimiter=',',dtype=np.str_)
points = (points_arr[:,:1],points_arr[:,1:5])

def drawing(img,points):
    labels,points = points
    print(labels)
    print(points)

img = cv2.imread('crossing.jpg')
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
drawing(img,points)