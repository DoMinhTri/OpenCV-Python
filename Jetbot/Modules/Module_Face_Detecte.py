import cv2

def faceDetect(img, objCascade, scaleF = 1.1, minF = 4):
    imgObj = img.copy()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    objects = objCascade.detectMultiScale(imgGray, scaleF, minF)
    objectsOut = []
    for (x, y, w, h) in objects:
        cv2.rectangle(imgObj, (x, y), (x+w, y+h), (255, 0, 255), 1)
        objectsOut.append([[x ,y, w, h], w*h])

    objectsOut = sorted(objectsOut, key = lambda x:x[1], reverse = True)
    return imgObj, objectsOut

def main():
    img = cv2.imread("../Data/lena.png")
    faceCascade = cv2.CascadeClassifier("../Data/haarcascade_frontalface_default.xml")
    imgObjects, objects = faceDetect(img, faceCascade)
    cv2.imshow("Face  detect", imgObjects)
    cv2.waitKey(0)

if __name__ == "__main__":
    main()

