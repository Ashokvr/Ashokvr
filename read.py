import cv2 as cv
# img=cv.imread('Photos\After Hours.png')
# cv.imshow('Cat',img)


def rescaleFrame(frame,scale=0.75):
    width=int(frame.shape[1]*scale) 
    height=int(frame.shape[0]*scale)
    dimenions=(width,height)

    return cv.resize(frame,dimenions,interpolation=cv.INTER_AREA)
#Video Open Code
capture = cv.VideoCapture(1)
while True:
    isTrue,frame =capture.read()
    frame_resized=rescaleFrame(frame,1.5) #function called 
    cv.imshow('Video Resized',frame_resized)
    cv.imshow('Video',frame)
    if cv.waitKey(20) & 0xFF==ord('s'): #0xFF is the keyboard input key which stops on key press 
        break
capture.release()
cv.destroyAllWindows()
cv.waitKey(0)
#Video Close