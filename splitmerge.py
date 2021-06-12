import cv2 as cv
import numpy as np

img=cv.imread('Photos\iPad Pro 2020.png')
resized=cv.resize(img,(500,500),interpolation=cv.INTER_CUBIC)
cv.imshow('Resized',resized)
blank=np.zeros(resized.shape[:2],dtype='uint8')
cv.imshow('Blank',blank)

#split image directly without blank
b,g,r=cv.split(resized)
cv.imshow('Blue',b)
cv.imshow('Green',g)
cv.imshow('Red',r)

#split an image with blank
blue=cv.merge([b,blank,blank])
green=cv.merge([blank,g,blank])
red=cv.merge([blank,blank,r])
cv.imshow('Blue',blue)
cv.imshow('Green',green)
cv.imshow('Red',red)



print(resized.shape)
print(b.shape)
print(g.shape)
print(r.shape)
#merge seperated image
merged=cv.merge([b,g,r])
cv.imshow('MergedImage',merged)







if cv.waitKey(0)& 0xFF==ord('s'):
    cv.destroyAllWindows()