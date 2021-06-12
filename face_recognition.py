import os
import numpy as np
import cv2 as cv
import os

haar_cascade = cv.CascadeClassifier('haar_face.xml')

p = []
for i in os.listdir(r'C:\Users\user_\OneDrive\Documents\OpenCv\Photos\Train'):
    p.append(i)
print(p)
# features=np.load('features.npy',allow_pickle=True)
# labels=np.load('labels.npy')

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('face_trained.yml')

img = cv.imread('20210110083634_IMG_4060.jpg')
cv.imshow('Color', img)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('GrayColor', gray)

faces_rect = haar_cascade.detectMultiScale(gray, 1.1, 4)
for (x, y, w, h) in faces_rect:
    faces_roi = gray[y:y + h, x:x + h]
    label, confidence = face_recognizer.predict(faces_roi)
    print(f'Label={p[label]} with a confidence pg  {confidence}')
    cv.putText(img, str(p[label]), (20, 20), cv.FONT_HERSHEY_COMPLEX, 1.0, (0, 255, 0), thickness=2)
    cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), thickness=2)
cv.imshow('detect face', img)
cv.waitKey(0)
