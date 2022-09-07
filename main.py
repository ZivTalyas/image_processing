import cv2
import numpy as np
from numpy import sin, cos, pi
from matplotlib import image
from matplotlib import pyplot
import matplotlib.pyplot as plt


if __name__ == "__main__":
    image = cv2.imread('test1.jpg')
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    #cv2.imshow('Original image', image)
    matrix_pic = np.copy(image)
    cv2.imshow('Gray image', gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    #print(np.copy(image))