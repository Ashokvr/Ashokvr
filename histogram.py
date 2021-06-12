#This is to visualise the color intensity of the pixels in the picture
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
img=cv.imread('Photos\Chicago.jpg')
resized=cv.resize(img,(800,500),interpolation=cv.INTER_CUBIC)
cv.imshow('Resized',resized)

blank = np.zeros(resized.shape[:2], dtype='uint8')

# gray = cv.cvtColor(resized, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)

mask = cv.circle(blank, (resized.shape[1]//2,resized.shape[0]//2), 100, 255, -1)

masked = cv.bitwise_and(resized,resized,mask=mask)
cv.imshow('Mask', masked)


#Gray scale hsitogram
#cv.calHist(<List of images [gray]>,<no channels>,<mask image or None>,<No of Bins>,<range of pixels>)
# gray_hist= cv.calcHist([gray],[0],mask,[256],[0,256])
# plt.figure
# plt.title('Grayscale Histogram')
# plt.xlabel('Bins')
# plt.ylabel('Pixels')
# plt.plot(gray_hist)
# plt.xlim([0,256])


#Color Histogram
plt.figure
plt.title('Color Histogram')
plt.xlabel('Bins')
plt.ylabel('Pixels')
colors=('b','g','r')
for i,col in enumerate(colors):
    hist=cv.calcHist([resized],[i],mask,[256],[0,256])
    plt.plot(hist,color=col)
    plt.xlim([0,256])
plt.show()











if cv.waitKey(0)& 0xFF==ord('s'):
    cv.destroyAllWindows()