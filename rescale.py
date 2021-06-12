import cv2 as cv

#RescaleImage Function
def rescaleFrame(frame,scale=0.75):
    #Works for all photos and videos and live steams
    width=int(frame.shape[1]*scale) 
    height=int(frame.shape[0]*scale)
    dimenions=(width,height)

    return cv.resize(frame,dimenions,interpolation=cv.INTER_AREA)
def changeRes(width,height):
    #Works only for live webcam and the streamvideo
    capture.set(3,width)
    capture.set(4,height)

# img=cv.imread('Photos\After Hours.png')
# frame_resized=rescaleFrame(img,0.20)
# cv.imshow('Cat',img)
# cv.imshow('Video Resized',frame_resized)

# #Video Open Code
capture = cv.VideoCapture(1)#for webcam or streaming
#capture =cv.VideoCapture('#Give the Vide Path Here')
while True:
    isTrue,frame =capture.read()
    frame_resized=rescaleFrame(frame)
    #frame_resol=changeRes(23,34)
    cv.imshow('Video Live Resized',frame_resol)
    cv.imshow('Video Resized',frame_resized)
    cv.imshow('Video',frame)
    if cv.waitKey(20) & 0xFF==ord('s'): #0xFF is the keyboard input key which stops on key press 
        break
capture.release()
cv.destroyAllWindows()
cv.waitKey(0)
#Video Close