import matplotlib.pyplot as plt
import numpy as np
import cv2

def drawing(img,points):
    labels,points = points
    for i,item in enumerate(points):
        (x,y),(w,h) = item.reshape((2,2))
        start_point = (x,y)
        end_point = (x+w,y+h)
        label = labels[i][0]

        cv2.rectangle(img,start_point,end_point,color=(255, 0, 0),thickness=3)
        cv2.putText(img,label,(start_point[0]-15,start_point[1]-15),cv2.FONT_HERSHEY_SIMPLEX,2.0,color=(255, 0, 0),thickness=3)
        plt.imshow(img)
    plt.show()

points_arr = np.genfromtxt('bbox_road.csv',delimiter=',',dtype=np.str_)
points = (points_arr[:,:1],np.array(points_arr[:,1:5],dtype=np.uint16))
img = cv2.imread('crossing.jpg')
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

drawing(img,points)