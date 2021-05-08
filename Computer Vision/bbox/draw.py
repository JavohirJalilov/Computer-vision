import matplotlib.pyplot as plt
import numpy as np
import cv2
import drawing_bbox_label

filename = 'bbox_road.csv'
img = cv2.imread('crossing.jpg')
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

drawing_bbox_label.drawing_bbox(img,filename)