import cv2
import chapter9_ObjectDetectModule as odm
import numpy as np




cap = cv2.VideoCapture(0)
#faceCascade = cv2.CascadeClassifier("haarcascades/haarcascade_frontalface_default.xml")
faceCascade = cv2.CascadeClassifier("haarcascades/haarcascade_fullbody.xml")

def findCenter(imgObjects, objects):
    cx, cy = -1, -1
    if len(objects) != 0:
        x, y, w, h = objects[0][0]
        cx = x + w//2
        cy = y + h//2
        cv2.circle(imgObjects, (cx, cy), 1, (0, 255, 0), cv2.FILLED)
        #############
        ih, iw, ic = imgObjects.shape
        cv2.line(imgObjects, (iw//2, cy), (cx, cy), (0, 255, 0), 1)
        cv2.line(imgObjects, (cx, ih//2), (cx, cy), (0, 255, 0), 1)
        #############
        data = str(cx-iw//2)
        #sm.SendData(ser, data, data)
        print(data)
    return cx, cy, imgObjects



while True:
    suscess, img = cap.read()
    img = cv2.resize(img, (0, 0), None, 0.5, 0.5)
    imgObjects, objects = odm.faceDetect(img, faceCascade, 1.08, 10)
    cx, cy, imgObjects = findCenter(imgObjects, objects)
    ###########################
    h, w, c = imgObjects.shape
    cv2.line(imgObjects, (w//2, 0), (w//2, h), (255, 0, 255), 1)
    cv2.line(imgObjects, (0, h//2), (w, h//2), (255, 0, 255), 1)


    ##########################
    img = cv2.resize(imgObjects, (0, 0), None, 4, 4)
    cv2.imshow("Camera", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

