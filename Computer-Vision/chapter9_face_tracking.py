import cv2
import chapter9_ObjectDetectModule as odm
import chapter8_window_serial as sm
import numpy as np


frameWidth = 640
frameHeight = 480

flip=2
#camSet='nvarguscamerasrc sensor-id=0 ! video/x-raw(memory:NVMM), width=3264, height=2464, framerate=21/1,format=NV12 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(frameWidth)+', height='+str(frameHeight)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
#camSet ='v4l2src device=/dev/video1 ! video/x-raw,width='+str(width)+',height='+str(height)+',framerate=24/1 ! videoconvert ! appsink'
#camSet = 'nvarguscamerasrc ! video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(frameWidth)+', height='+str(frameHeight)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
#camSet = 'nvarguscamerasrc sensor-id=0 ! video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(frameWidth)+', height='+str(frameHeight)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'

cap = cv2.VideoCapture(0)
ser = sm.initConnection("COM11", 9600)
faceCascade = cv2.CascadeClassifier("Resources/haarcascade_frontalface_default.xml")
perrorLR, perrorUD = 0,0

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

def trackObject(cx, cy, w, h):
    global perrorLR, perrorUD

    kLR = [0.5, 0.5]
    kUD = [0.5, 0.5]

    if cx!= -1:
        # Left and Right
        errorLR = w//2 - cx
        posX = kLR[0]* errorLR + kLR[1]* (errorLR-perrorLR)
        posX = int(np.interp(posX, [-w//2, w//2], [20, 160]))
        perrorLR = errorLR

        # Up and Down
        errorUD = h//2 - cy
        posY = kUD[0]* errorUD + kUD[1]* (errorUD-perrorUD)
        posY = int(np.interp(posY, [-h//2, h//2], [160, 20]))
        perrorUD = errorUD

        message = str(posX) + "," + str(posY)
        data = message
        sm.SendData(ser, data, message)

while True:
    suscess, img = cap.read()
    img = cv2.resize(img, (0, 0), None, 0.4, 0.4)
    imgObjects, objects = odm.faceDetect(img, faceCascade, 1.08, 10)
    cx, cy, imgObjects = findCenter(imgObjects, objects)
    ###########################
    h, w, c = imgObjects.shape
    cv2.line(imgObjects, (w//2, 0), (w//2, h), (255, 0, 255), 1)
    cv2.line(imgObjects, (0, h//2), (w, h//2), (255, 0, 255), 1)

    #trackObject(cx, cy, w, h)
    ##########################
    img = cv2.resize(imgObjects, (0, 0), None, 3, 3)
    cv2.imshow("Camera", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

