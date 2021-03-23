import cv2
import numpy as np
import utlis

def getLaneCuve(img):
    imgThres = utlis.thresholding(img)

    cv2.imshow("Thres", imgThres)
    return None

def main():
    cap = cv2.VideoCapture("data/video2.mp4")
    while True:
        _, img = cap.read()
        img = cv2.resize(img, (460, 380))
        getLaneCuve(img)


        cv2.imshow("Video ", img)
        cv2.waitKey(1)

if __name__ == "__main__":
    main()