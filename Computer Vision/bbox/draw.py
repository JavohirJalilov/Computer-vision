import matplotlib.pyplot as plt
import numpy as np
import cv2
import drawing_bbox_label

points_arr = np.genfromtxt('bbox_road.csv',delimiter=',',dtype=np.str_)
points = (points_arr[:,:1],np.array(points_arr[:,1:5],dtype=np.uint16))
img = cv2.imread('crossing.jpg')
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

drawing_bbox_label.drawing_bbox(img,points)