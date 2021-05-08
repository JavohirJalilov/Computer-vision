import matplotlib.pyplot as plt
import numpy as np
import cv2


def drawing_bbox(img,filename_csv):
    '''
    Image object detection.
    file CSV, Points format: COCO
    Parameters:
        img: numpy.array.
        filename_csv: str.
    '''
    points_arr = np.genfromtxt(filename_csv,delimiter=',',dtype=np.str_)
    points = (points_arr[:,:1],np.array(points_arr[:,1:5],dtype=np.uint16))
    labels,points = points
    for i,item in enumerate(points):
        (x,y),(w,h) = item.reshape((2,2))
        start_point = (x,y)
        end_point = (x+w,y+h)
        label = labels[i][0]

        cv2.rectangle(img,start_point,end_point,color=(255, 0, 0),thickness=2)
        cv2.putText(img,label,(start_point[0]-15,start_point[1]-15),cv2.FONT_HERSHEY_SIMPLEX,1.2,color=(255, 0, 0),thickness=2)
        plt.imshow(img)
    plt.show()