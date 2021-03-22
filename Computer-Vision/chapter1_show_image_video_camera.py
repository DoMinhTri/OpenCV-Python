###   https://www.youtube.com/watch?v=WQeoO7MI0Bs
### Bài 1: Image Show  :
### Bài 1: Video show  :
### Bài 1: Camera show :

################  Image Show
# import cv2

# img = cv2.imread("Resources/book.jpg")
# cv2.imshow("Book", img)
# cv2.waitKey(0)

################  Video show
# import cv2

# wwidth = 640
# wheight = 480
# cap = cv2.VideoCapture("Resources/test_video.mp4")
# while True:
#     success, img = cap.read()
#     img = cv2.resize(img, (wwidth, wheight))
#     cv2.imshow("Video", img)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

################  Camera show
import cv2

wwidth = 640
wheight = 480
cap = cv2.VideoCapture("http://192.168.1.4:8080/video") #http://192.168.1.4:8080/video

if not cap.isOpened():
    raise IOError("Cannot open webcam")

while True:
    suscess, img = cap.read()
    img = cv2.resize(img, (wwidth, wheight))
    cv2.imshow("Camera", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

