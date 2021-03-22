import cv2

def faceDetect(img, objCascade, scaleF = 1.1, minF = 4):

    imgObj = img.copy()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    objects = objCascade.detectMultiScale(imgGray, scaleF, minF)
    for (x, y, w, h) in objects:
        cv2.rectangle(imgObj, (x, y), (x+w, y+h), (255, 0, 255), 1)

    return imgObj, objects

def main():
    img = cv2.imread("Resources/lena.png")
    faceCascade = cv2.CascadeClassifier("Resources/haarcascade_frontalface_default.xml")
    imgObjects, objects = faceDetect(img, faceCascade)
    cv2.imshow("Face  detect", imgObjects)
    cv2.waitKey(0)

if __name__ == "__main__":
    main()

