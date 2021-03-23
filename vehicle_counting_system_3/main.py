import numpy as np
import cv2
cap = cv2.VideoCapture('video.mp4')
#set the width and height
static_back = None
while(cap.isOpened()):
  ret, frame = cap.read()
  scale_percent = 50 # percent of original size
  width = int(frame.shape[1] * scale_percent / 100)
  height = int(frame.shape[0] * scale_percent / 100)
  dim = (width, height)
  gray = cv2.resize(frame, dim, interpolation = cv2.INTER_AREA)
  final=gray
  gray = cv2.cvtColor(gray, cv2.COLOR_BGR2GRAY)

  if static_back is None: 
        static_back = gray 
        continue
  diff_frame = cv2.absdiff(static_back, gray)
  
  thresh_frame = cv2.threshold(diff_frame, 50, 30, cv2.THRESH_BINARY)[1] 
  thresh_frame = cv2.dilate(thresh_frame, None, iterations = 0) 
  #cnts = cv2.findContours(thresh_frame.copy(), cv2.RETR_EXTERNAL,g
#		cv2.CHAIN_APPROX_SIMPLE)
  contours, hierarchy = cv2.findContours(thresh_frame.copy(),cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
  for contour in contours:
     
      if cv2.contourArea(contour) < 500 or cv2.contourArea(contour) > 10000:
        continue
      (x, y, w, h) = cv2.boundingRect(contour)
      cv2.rectangle(final, (x, y), (x+w, y+h), (255, 255, 12), 2)   
      #areas = [cv2.contourArea(c) for c in contours]
      #max_index = np.argmax(areas)
      #cnt=contours[max_index]
      #x,y,w,h = cv2.boundingRect(cnt)
      #cv2.rectangle(thresh_frame,(x,y),(x+w,y+h),(0,255,0),2)
      #cv2.imshow('frame2',thresh_frame)
  #cv2.putText(im,result,(x,y), font, 1, (200,0,0), 3, cv2.LINE_AA)
  font = cv2.FONT_HERSHEY_SIMPLEX
  cv2.putText(final, 'aInven!', (230, 50), font, 2, (0, 0, 0), 2 )

  cv2.imshow('frame',final)
  
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break

cap.release()
cv2.destroyAllWindows()