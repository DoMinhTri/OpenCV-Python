import cv2
import numpy as np

img = cv2.imread("Resources/shapes.png")
imgCropped = img[46:119, 352:495]
imgResize = cv2.resize(img, (800, 400))
imgResize2 = cv2.resize(img, (0, 0), None, 0.5, 0.5)

cv2.imshow("Image", img)
cv2.imshow("Image Cropped", imgCropped)
cv2.imshow("Image Resize", imgResize)
cv2.imshow("Image Resize 2", imgResize2)

print(img.shape)
print(imgCropped.shape)
print(imgResize.shape)
print(imgResize2.shape)

cv2.waitKey(0)