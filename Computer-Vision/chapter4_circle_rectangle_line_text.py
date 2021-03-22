import cv2
import numpy as np

img = np.zeros((512,512,3),np.uint8)
#print(img)
#img[:]= 255,0,0

cv2.line(img,(10,10),(img.shape[1] -10,img.shape[0] - 10),(0,255,0),3)
cv2.rectangle(img,(0,0),(250,350),(0,0,255),2)
cv2.circle(img,(400,50),30,(140,137,255),3)
cv2.putText(img," OPENCV  ",(300,200),cv2.FONT_HERSHEY_COMPLEX,1,(255,150,0),1)


cv2.imshow("Image",img)
cv2.waitKey(0)