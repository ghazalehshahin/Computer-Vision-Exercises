import cv2 as cv
import numpy as np

#print possible events happens by mouse

# events = [i for i in dir(cv) if 'EVENT' in i]
# print(events)

#Output: ['EVENT_FLAG_ALTKEY', 'EVENT_FLAG_CTRLKEY', 'EVENT_FLAG_LBUTTON', 'EVENT_FLAG_MBUTTON',
#  'EVENT_FLAG_RBUTTON', 'EVENT_FLAG_SHIFTKEY', 'EVENT_LBUTTONDBLCLK', 'EVENT_LBUTTONDOWN', 'EVENT_LBUTTONUP',
#  'EVENT_MBUTTONDBLCLK', 'EVENT_MBUTTONDOWN', 'EVENT_MBUTTONUP', 'EVENT_MOUSEHWHEEL', 'EVENT_MOUSEMOVE',
#  'EVENT_MOUSEWHEEL', 'EVENT_RBUTTONDBLCLK', 'EVENT_RBUTTONDOWN', 'EVENT_RBUTTONUP']

drawing = False
mode = True
ix,iy = -1,-1
img = np.zeros((512,512,3), np.uint8)


def draw_circle(event,x,y,flags,param):
    global img
    if event == cv.EVENT_LBUTTONDBLCLK:
        cv.circle(img,(x,y),100,(255,0,0),-1)

def draw_circle_rectangle(event,x,y,flags,param):
    global ix,iy,drawing,mode,img
    if event == cv.EVENT_LBUTTONDOWN:
        drawing = True
        ix,iy = x,y
    elif event == cv.EVENT_MOUSEMOVE:
        if drawing == True:
            if mode == True:
                cv.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
            else:
                cv.circle(img,(x,y),5,(0,0,255),-1)
    elif event == cv.EVENT_LBUTTONUP:
        drawing = False
        if mode == True:
            cv.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
        else:
            cv.circle(img,(x,y),5,(0,0,255),-1)

def draw_unfilled_rectangle(event,x,y,flags,param):
    global ix,iy,drawing,mode,img
    if event == cv.EVENT_LBUTTONDOWN:
        drawing = True
        ix,iy = x,y
    elif event == cv.EVENT_LBUTTONUP:
        drawing = False
        if mode == True:
            cv.rectangle(img,(ix,iy),(x,y),(0,255,0),1)

cv.namedWindow('image')
cv.setMouseCallback('image',draw_unfilled_rectangle)
while(1):
    cv.imshow('image',img)
    k = cv.waitKey(1) & 0xFF

    if k == ord('m'):
        mode = not mode
    elif k == ord('q'):
        break
    

