import cv2 as cv
import numpy as pm


img=cv.imread('Photos\double.jpg')
resized=cv.resize(img,(800,500),interpolation=cv.INTER_CUBIC)
cv.imshow('Resized',resized)

gray=cv.cvtColor(resized,cv.COLOR_RGB2GRAY)
cv.imshow('Gray',gray)

haar_cascade=cv.CascadeClassifier('haar_face.xml')
faces_rect=haar_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5)
print(f'Number of Faces ={len(faces_rect)}')

#For Better face recognise we can use DLLIBS face recogniser and less sensitve
for (x,y,w,h) in faces_rect:
    cv.rectangle(resized,(x,y),(x+w,y+h),(0,255,0),thickness=2)

cv.imshow('Faces Detected',resized) 
if cv.waitKey(0)& 0xFF==ord('s'):
    cv.destroyAllWindows()