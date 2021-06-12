#Edge Detection and EDGE DETECTION
import cv2 as cv
import numpy as np
img=cv.imread('Photos\Chicago.jpg')
resized=cv.resize(img,(800,500),interpolation=cv.INTER_CUBIC)
cv.imshow('Resized',resized)

gray=cv.cvtColor(resized,cv.COLOR_RGB2GRAY)
cv.imshow('Gray',gray)
#laplacian

lap=cv.Laplacian(gray,cv.CV_64F)
lap=np.uint8(np.absolute(lap)) #To make pixel values to positive because pixels shouldnt be negetive
cv.imshow('Laplacian',lap)

#sobel
sobelx=cv.Sobel(gray,cv.CV_64F,1,0)
sobely=cv.Sobel(gray,cv.CV_64F,0,1)
combined=cv.bitwise_or(sobelx,sobely)
cv.imshow('Combined',combined)
cv.imshow('sobelx',sobelx)
cv.imshow('sobely',sobely)

canny=cv.Canny(gray,150,175)
cv.imshow('Canny',canny)


if cv.waitKey(0)& 0xFF==ord('s'):
    cv.destroyAllWindows()