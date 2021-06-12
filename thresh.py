#Threshold is the intensity less then it will reset to o if intensity is high then to 255 
import cv2 as cv
import numpy as np
img=cv.imread('Photos\Chicago.jpg')
resized=cv.resize(img,(800,500),interpolation=cv.INTER_CUBIC)
cv.imshow('Resized',resized)

gray=cv.cvtColor(resized,cv.COLOR_RGB2GRAY)
cv.imshow('Gray',gray)

#Threshold
#threshold,thresh=cv.threshold(< IMAGE gray>,< instensity range 150>,< intensity 255>,< threshold formatcv.THRESH_BINARY>)
threshold,thresh=cv.threshold(gray,150,255,cv.THRESH_BINARY)
cv.imshow('Threshold',thresh)
hreshold,thresh=cv.threshold(gray,150,255,cv.THRESH_BINARY_INV)
cv.imshow('ThresholdInvese',thresh)

#Adptive Thresholding 
#cv.ADAPTIVE_THRESH_MEAN_C
#cv.ADAPTIVE_THRESH_GAUSSIAN_C
#adaptive_thresh=cv.adaptiveThreshold(<image gray>,<range 255>,< image adaptive threshold like mean,gaussian cv.ADAPTIVE_THRESH_MEAN_C>,< type threshold cv.THRESH_BINARY>,<LEVEL OF intensity11>,<MEAN DIFFRENCE>)
adaptive_thresh=cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,11,3)
cv.imshow('Adaptive',adaptive_thresh)



if cv.waitKey(0)& 0xFF==ord('s'):
    cv.destroyAllWindows()