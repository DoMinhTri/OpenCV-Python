import cv2
import numpy as np
import Modules.Module_Center_Point as TamAnh
import jetbot_driver.robot as jetbot
import time


robot = jetbot.JetRobot()
cap = cv2.VideoCapture(-1)



while True:
    _, img = cap.read()
    x_center, y_center = TamAnh.ToaDoTam(img)
    ###############  Red color
    low_red = np.array([161, 155, 84])
    hight_red = np.array([179, 255, 255])
    hsv_frame = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    red_mask = cv2.inRange(hsv_frame, low_red, hight_red)
    #cv2.imshow("Mask", red_mask)
    ###############
    contours, _ = cv2.findContours(red_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=lambda x: cv2.contourArea(x), reverse=True)
    for cnt in contours:
        (x, y, w, h) = cv2.boundingRect(cnt)
        x_medium = int(x + w/2)
        y_medium = int(y + h/2)
        #########
        cv2.circle(img, (x_medium, y_medium), 20, (0, 255, 0))
        cv2.line(img, (x_center, y_center), (x_medium, y_medium), (0, 255, 255), 2)
        ######### Xe tu lay
        vitri = x_center - x_medium
        sms = ""
        if vitri > 20:
            sms = "Trai: " + str(vitri)
            robot.left_motor.value = 0
            robot.right_motor.value = 0.3
        elif vitri < -20:
            sms = "Phai: " + str(vitri)
            robot.right_motor.value = 0
            robot.left_motor.value = 0.3
        else:
            sms = "|" + str(vitri)
            robot.stop()
        break

    cv2.putText(img, sms, (10, 20), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 255, 255), 1)
    cv2.imshow("Camera", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()