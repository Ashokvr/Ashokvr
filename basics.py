import cv2 as cv

def rescaleFrame(frame,scale=0.75):
    width=int(frame.shape[1]*scale) 
    height=int(frame.shape[0]*scale)
    dimenions=(width,height)

    return cv.resize(frame,dimenions,interpolation=cv.INTER_AREA)

img=cv.imread('Photos\Chicago.jpg')

frame_resized=rescaleFrame(img,0.20)
cv.imshow('Cat',frame_resized)
#Convert To GrayScale
gray=cv.cvtColor(frame_resized,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

#Convert Blur
frame_resized=rescaleFrame(img,0.25)
#blur=cv.GaussianBlur(frame_resized,<Kernal Size(7,7)>,<cv.BORDER_DEFAULT>)
blur=cv.GaussianBlur(frame_resized,(7,7),cv.BORDER_DEFAULT)
cv.imshow('Blur',blur)

#EdgeCascade
canny=cv.Canny(frame_resized,125,175)
#When we apply blur it will help to reduce edges in the image
canny=cv.Canny(blur,155,175)
cv.imshow('Canny',canny)

#Dilating the Image to capture the structure of the image
#dilated=cv.dilate(<image>,<kenal size(5,5)>,<iterations>)
dilated=cv.dilate(canny,(5,5),iterations=3)
cv.imshow('Dilated',dilated)

#Eroding This is final get back the  edge cascade image from dilated image
eroded=cv.erode(dilated,(3,3),iterations=3)
cv.imshow('Eroded',eroded)

#Resize
#resized=cv.resize(<IMAGE>,<size>(500,500),<INTER_CUBIC,INTER_AREA,INTER_LINEAR>interpolation=cv.INTER_AREA)
resized=cv.resize(img,(500,500),interpolation=cv.INTER_LINEAR)
cv.imshow('Resized',resized)

#Cropping
cropped=resized[50:200,200:400]
cv.imshow('Crop',cropped)

if cv.waitKey(0) & 0xFF==ord('s'): #0xFF is the keyboard input key which stops on key press 
        cv.destroyAllWindows()


