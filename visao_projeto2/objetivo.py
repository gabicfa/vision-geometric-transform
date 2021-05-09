import cv2
import numpy as np
from matplotlib import pyplot as plt
import time
from pylab import *
from numpy import *
from PIL import Image


def what_to_find():
    webcam = cv2.VideoCapture(0)
    webcam.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH, 800)
    webcam.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT, 600)
    print('Cheese!!')
    time.sleep(2)
    value, image = webcam.read()
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    cv2.imwrite('objetivo.png', image_rgb)
    print("Ok!")   
    webcam.release()

print("Va para o seu objetivo")
time.sleep(5)
print('5')
time.sleep(1)
print('4')
time.sleep(1)
print('3')
time.sleep(1)
print('2')
time.sleep(1)
print('1')
what_to_find()
time.sleep(1)