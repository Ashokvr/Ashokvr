import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt #intall  python -m pip install -U pip #python -m pip install -U matplotlib

                               

img=cv.imread('Photos\Ferrari.jpg')
resized=cv.resize(img,(800,500),interpolation=cv.INTER_CUBIC)
cv.imshow('Resized',resized)
#dimesions of mask should be as same as image then only that will work
blank=np.zeros(resized.shape[:2],dtype='uint8')
cv.imshow('BlankImge',blank)

mask=cv.circle(blank.copy(),(resized.shape[1]//2,resized.shape[0]//2),200,255,-1)
cv.imshow('Mask',mask)

mask_shape=cv.rectangle(blank.copy(),(30,30),(370,370),255,-1)
wierd_shape=cv.bitwise_and(mask,mask_shape)
cv.imshow('Wiered_shape',wierd_shape)

#interseting region to find the masked part
masked=cv.bitwise_and(resized,resized,mask=wierd_shape)
cv.imshow('Masked Image',masked)








if cv.waitKey(0)& 0xFF==ord('s'):
    cv.destroyAllWindows()