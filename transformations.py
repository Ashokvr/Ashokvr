import cv2 as cv
import numpy as np


def rescaleFrame(frame,scale=0.75):
    width=int(frame.shape[1]*scale) 
    height=int(frame.shape[0]*scale)
    dimenions=(width,height)

    return cv.resize(frame,dimenions,interpolation=cv.INTER_AREA)

img=cv.imread('Photos\Starlit Valley.png')

frame_resized=rescaleFrame(img,0.20)
cv.imshow('REZIE',frame_resized)
#Transaltion
def translate(frame_resized,x,y):
    transMat=np.float32([[1,0,x],[0,1,y]]) #Transformation to be done in matrix
    dimensions=(frame_resized.shape[1],img.shape[0]) 
    return cv.warpAffine(frame_resized,transMat,dimensions)
#-x -->Left
#-y -->Up
# x -->Right
# y -->Down
translated=translate(frame_resized,-100,100)
cv.imshow('Transulated',translated)

#Rotation
#anlge "-" will rotae clockwise
def rotate(img,angle,rotpoint=None):
    (height,width)=img.shape[:2]
    if rotpoint is None:
        rotpoint=(width//2,height//2)
    rotMot=cv.getRotationMatrix2D(rotpoint,angle,1.0)
    dimensions=(width,height)
    return cv.warpAffine(img,rotMot,dimensions)
rotated = rotate(frame_resized,-45)
#rotate = rotate(frame_resized,-45) #i we rotae the rotaed image then it will give another image as it is considering the whole  blank space
rotate_rotated=rotate(rotated,-90)
cv.imshow('Rotae',rotate_rotated)

#Resize
#shirnking --->INTER_AREA,INTER_LINEAR
#Enlarge -->INTER_CUBIC
resized=cv.resize(frame_resized,(500,500),interpolation=cv.INTER_CUBIC)
cv.imshow('Resized',resized)

#Flip
#0-- vertical flip
#1-- horizontal
#-1--horizontal and vertical

flip=cv.flip(frame_resized,1)
cv.imshow('Flip',flip)

#Cropping
cropped= frame_resized[200:400,300:400]
cv.imshow('Crop',cropped)






if cv.waitKey(0)& 0xFF==ord('s'):
    cv.destroyAllWindows()