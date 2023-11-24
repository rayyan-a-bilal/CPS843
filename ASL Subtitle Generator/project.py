import cv2 #openCV
import os
import time
import uuid #to name our files

IMAGES_PATH = "Tensorflow/workspace/images/collectedImages" # where all the images are saved

labels = ['hello', 'thanks','yes', 'no', 'ily']
number_images = 15

#Code for collecting images

for label in labels:
    !mkdir{'Tensorflow/workspace/images/collectedImages\\'+label}
    cap = cv2.VideoCapture(0)
    print("Collecting ")