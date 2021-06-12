import cv2 as cv
import numpy as np

#pixel is tured of is called as 0 if it is on thenit is 1
blank =np.zeros((400,400),dtype='uint8')
rectangel=cv.rectangle(blank.copy(),(30,30),(370,370),255,-1)
circle=cv.circle(blank.copy(),(200,200),200,255,-1)

cv.imshow('Rectangle',rectangel)
cv.imshow('Circle',circle)

#bitwise AND
#we will use this in masking
bitwise_and=cv.bitwise_and(rectangel,circle)
bitwise_or=cv.bitwise_or(rectangel,circle)
bitwise_xor=cv.bitwise_xor(rectangel,circle)
bitwise_not=cv.bitwise_not(rectangel,circle)
cv.imshow('Bitwise_and',bitwise_and)
cv.imshow('Bitwise_or',bitwise_or)
cv.imshow('Bitwise_xor',bitwise_xor)
cv.imshow('Bitwise_not',bitwise_not)

if cv.waitKey(0)& 0xFF==ord('s'):
    cv.destroyAllWindows()