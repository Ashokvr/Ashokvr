import cv2 as cv
import numpy as np


img=cv.imread('Photos\Chicago.jpg')
resized=cv.resize(img,(500,500),interpolation=cv.INTER_CUBIC)
cv.imshow('Resized',resized)

#averaging average the surrounding pixels
average=cv.blur(resized,(3,3))
cv.imshow('blur',average)
#Gausian Blur less blur
#gaussian=cv.GaussianBlur(<image resized>,<blur scale(7,7)>,<Standard deviation of x direction 0>)
gaussian=cv.GaussianBlur(resized,(3,3),0)
cv.imshow('Gaussian',gaussian)

#MedianBlur as similar average find the median of surrounding image
#median=cv.medianBlur(<image resized>,<Auomatically takes the size with number>)
median=cv.medianBlur(resized,3)
cv.imshow('Median',median)

#bilateral
#sigma of x,y are such to get pixelposition in image to be average
bilateral=cv.bilateralFilter(resized,50,150,150)
cv.imshow('Bilateral',bilateral)



if cv.waitKey(0)& 0xFF==ord('s'):
    cv.destroyAllWindows()