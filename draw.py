import cv2 as cv
import numpy as np
blank=np.zeros((500,500,3),dtype='uint8')
cv.imshow('Blank',blank)
#blank[portion of image]=pixels color
#blank[200:300,300:400]=0,255,0 #To make a solid rectangle
#blank[:]=0,0,255 #To makeBackground Image
#blank[:]=0,0,255 #pixels and image colours in file

#cv.imshow('Green',blank)
#Draw a Rectangle
#cv.rectangle(<blank Draw>,<Position(100,100)>,<width and height(250,250)>,<color(0,255,0)>,thickness=2)

# cv.rectangle(blank,(300,600),(250,250),(0,255,0),thickness=2)
# cv.imshow('Rectangle',blank)
# #thickness=cv.Filled or -1 -filles the part 
# cv.rectangle(blank,(0,0),(25
# 0,250),(0,255,0),thickness=cv.FILLED)
# cv.imshow('Rectangle',blank)
#SCALE BY  THE IMAGE
# cv.rectangle(blank,(0,0),(blank.shape[1]//2,blank.shape[0]//2),(0,255,0),thickness=-1)
# cv.imshow('Rectangle',blank)


# #Draw a Circle
# cv.circle(blank,(blank.shape[1]//2,blank.shape[0]//2),40,(0,0,255),thickness=-1)
# cv.imshow('Circle',blank)
# #Draw a line
# cv.line(blank,(100,200),(blank.shape[1]//2,blank.shape[0]//2),(255,255,255),thickness=3)
# cv.line(blank,(100,25),(30,40),(255,255,255),thickness=3)
# cv.imshow('Line',blank)



#Write Text
#cv.putText(blank,<Text Input>,<position>,<font style>,<font scale>,<pixel color>,<thickness>)
cv.putText(blank, 'Ashok Vardhan', (100,225), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), 2)
cv.imshow('TEXT',blank)
cv.waitKey(0)