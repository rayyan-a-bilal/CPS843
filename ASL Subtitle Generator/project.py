import cv2 #openCV
import os
import time
import uuid #to name our files

IMAGES_PATH = r"C:\Users\rayya\PycharmProjects\CPS843 project\RealTimeObjectDetection\Tensorflow\workspace\images\collectedImages"

labels = ['hello', 'thanks','yes', 'no', 'ily']
number_images = 15

#Code for collecting images

for label in labels:
    ## Label Collection ##
    os.makedirs(os.path.join(IMAGES_PATH, label), exist_ok=True)
    cap = cv2.VideoCapture(0)
    print("Collecting images for {}", format(label))
    time.sleep(5)
    for imageNum in range(number_images):
        ret,frame = cap.read()
        imagename = os.path.join(IMAGES_PATH, label, label+'.'+'{}.jpg'.format(str(uuid.uuid1())))
        cv2.imwrite(imagename, frame)
        cv2.imshow('frame', frame)
        time.sleep(2)

        if cv2.waitKey(0) & 0xFF == ord('q'):
            break
    cap.release()
cv2.destroyAllWindows()  # Close all OpenCV windows at the end
