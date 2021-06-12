import cv2 as cv
import numpy as np
img=cv.imread('Photos\Starlit Valley.png')
resized=cv.resize(img,(500,500),interpolation=cv.INTER_CUBIC)
cv.imshow('Resized',resized)

blank=np.zeros(resized.shape,dtype='uint8')
cv.imshow('Blank',blank)

gray=cv.cvtColor(resized,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)
blur=cv.GaussianBlur(gray,(5,5),cv.BORDER_DEFAULT)
cv.imshow('Blur',blur)
canny=cv.Canny(blur,125,175)
cv.imshow('Canny',canny)


#Thershold used below 125 set to black above 125 set to white
ret,thresh=cv.threshold(gray,125,255,cv.THRESH_BINARY)
cv.imshow('Thresh',thresh)
#Threshold contours and canny are mostly same
#This is a hierarchy to find contours
contours,hierarchies=cv.findContours(canny,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE) #RETURNS ALL THE COUTOURS
#cv.CHAIN_APPROX_NONE --> RETURNS ALL CORDINATES OF LINE
#cv.CHAIN_APPROX_SIMPLE --> RETURNS COMPRESS WITH TWO ENDPOINTS
#
#contours,hierarchies=cv.findContours(canny,cv.RETER_EXTERNAL,cv.CHAIN_APPROX_NONE) # RETURNS External contours
#contours,hierarchies=cv.findContours(canny,cv.RETER_TREE,cv.CHAIN_APPROX_NONE) #RETURNS ALL HIERARCIAL CONTOURS
print(F'{len(contours)} contour(s) found')

#it is used to draw the coutours
#cv.drawContours(<iamge to be drawn "blank">,<contours to be captures>,<to what level for all =-1>,<line colour(0,0,255)>,<thickness 3>)
cv.drawContours(blank,contours,-1,(0,0,255),1)
cv.imshow('Contours',blank)











if cv.waitKey(0)& 0xFF==ord('s'):
    cv.destroyAllWindows()
