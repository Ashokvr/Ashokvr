import cv2 as cv
import matplotlib.pyplot as plt #intall  python -m pip install -U pip #python -m pip install -U matplotlib

                               

img=cv.imread('Photos\Starlit Valley.png')
resized=cv.resize(img,(500,500),interpolation=cv.INTER_CUBIC)
cv.imshow('Resized',resized)

#To convert any image to BGR REPLACE THE POSTIONS bgr2gray to gray2bgr
#BGR TO GRAY SCALE
gray=cv.cvtColor(resized,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)
#Grayscale cannot be converted to HSV,LAB directly

#BGR TO HSV
hsv=cv.cvtColor(resized,cv.COLOR_BGR2HSV)
cv.imshow('HSV',hsv)

#bgr to l*a*b
lab=cv.cvtColor(resized,cv.COLOR_BGR2LAB)
cv.imshow('LAB',lab)

#BGR TO RGB this shoudl be done to get plotimage as RGB the below line inverts first then goes to plot so we will get rgb

rgb=cv.cvtColor(resized,cv.COLOR_BGR2RGB)
cv.imshow('RGB',rgb)
plt.imshow(rgb)
plt.show()

# #matplotlib image will be displayeed as inverted
# plt.imshow(resized)
# plt.show()









if cv.waitKey(0)& 0xFF==ord('s'):
    cv.destroyAllWindows()
