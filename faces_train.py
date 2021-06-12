import os
import cv2 as cv
import numpy as np

# img=cv.imread('Photos\double.jpg')
# resized=cv.resize(img,(800,500),interpolation=cv.INTER_CUBIC)
# cv.imshow('Resized',resized)

# gray=cv.cvtColor(resized,cv.COLOR_RGB2GRAY)
# cv.imshow('Gray',gray)

haar_cascade = cv.CascadeClassifier('haar_face.xml')
p = []
for i in os.listdir(r'C:\Users\user_\OneDrive\Documents\OpenCv\Photos\Train'):
    p.append(i)
print(p)
DIR = r'C:\Users\user_\OneDrive\Documents\OpenCv\Photos\Train'
features = []
labels = []


def create_train():
    for person in p:
        path = os.path.join(DIR, person)
        label = p.index(person)

        for img in os.listdir(path):
            img_path = os.path.join(path, img)
            img_array = cv.imread(img_path)
            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)
            faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)
            for (x, y, w, h) in faces_rect:
                faces_roi = gray[y:y + h, x:x + w]
                features.append(faces_roi)
                labels.append(label)


create_train()
print('Training Done------------')
# print(f'length of the features list={len(features)}')
# print(f'length of the features lables={len(labels)}')

features = np.array(features, dtype='object')
labels = np.array(labels)

face_recognizer = cv.face.LBPHFaceRecognizer_create()

face_recognizer.train(features, labels)
face_recognizer.save('face_trained.yml')
print('Training Done------------')
np.save('features.npy', features)
np.save('labels.npy', labels)
