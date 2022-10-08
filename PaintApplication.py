from cmath import rect
import cv2 as cv
import numpy as np
import tkinter as tk
from tkinter import ttk

line, circle, rectangle, ellipse, text = 0,0,0,0,0
img = np.zeros((2000,2000,3), np.uint8)
shape = 'Shape: \n1-line \n2-circle \n3-rectangle \n4-ellipse \n5-text'
color = (255,255,255)
thickness = -1
drawing = False
ix,iy = -1,-1
content = ''
filled = 0
win= tk.Tk()
entry= tk.Entry(win, width= 40)

def getText():
    global entry, content
    string= entry.get()
    content = string

def getInput():
    global win, entry
    win.geometry("750x250")
    getText()
    label=tk.Label(win, text="", font=("Courier 22 bold"))
    label.pack()
    entry.focus_set()
    entry.pack()
    ttk.Button(win, text= "Okay",width= 20, command= getText).pack(pady=20)
    win.mainloop()

def getParams():
    global color, line, circle, rectangle, ellipse, text, thickness, filled
    red = cv.getTrackbarPos('Red','paint')
    green = cv.getTrackbarPos('Green','paint')
    blue = cv.getTrackbarPos('Blue','paint')
    color = (red, green, blue)
    filled = cv.getTrackbarPos('Filled:1 \nUnfilled: 0', 'paint')
    thickness = cv.getTrackbarPos('Brush Size', 'paint')
    if cv.getTrackbarPos(shape, 'paint') == 0:
        line = 1
        circle, rectangle, ellipse, text = 0,0,0,0
    elif cv.getTrackbarPos(shape, 'paint') == 1:
        circle = 1
        line, rectangle, ellipse, text = 0,0,0,0
    elif cv.getTrackbarPos(shape, 'paint') == 2:
        rectangle = 1
        line, circle, ellipse, text = 0,0,0,0
    elif cv.getTrackbarPos(shape, 'paint') == 3:
        ellipse = 1
        line, circle, rectangle, text = 0,0,0,0
    else:
        text = 1
        line, circle, rectangle, ellipse = 0,0,0,0
        getInput()

def drawShape(event,x,y,flags,param):
    global ix,iy,drawing,img, color, thickness, line, circle, rectangle, ellipse, text
    getParams()
    if event == cv.EVENT_LBUTTONDOWN:
        drawing = True
        ix,iy = x,y
    elif event == cv.EVENT_MOUSEMOVE:
        if drawing == True:
            if filled == 1:
                if rectangle == 1:
                    cv.rectangle(img,(ix,iy),(x,y),color,-1)
                elif line == 1: 
                    cv.line(img,(ix,iy), (x,y), color,thickness)
                elif circle == 1:
                    cv.circle(img,(x,y),5,color,-1)
                elif ellipse == 1:
                    cv.ellipse(img, (ix,iy), (x,x), 0, 0, 360, color, -1)
                elif text == 1:
                    cv.putText(img, content, (ix,iy), cv.FONT_HERSHEY_COMPLEX, 4, color, thickness)
                else:
                    print('please indicate the shape you want to add')
    elif event == cv.EVENT_LBUTTONUP:
        drawing = False
        if filled == 1:
            if rectangle == 1:
                cv.rectangle(img,(ix,iy),(x,y),color,-1)
            elif line == 1: 
                cv.line(img,(ix,iy), (x,y), color,thickness)
            elif circle == 1:
                cv.circle(img,(x,y),5,color,-1)
            elif ellipse == 1:
                cv.ellipse(img, (ix,iy), (x,x), 0, 0, 360, color, -1)
            else:
                cv.putText(img, text, (ix,iy), cv.FONT_HERSHEY_COMPLEX, 4, color, thickness)  
        else:
            if rectangle == 1:
                cv.rectangle(img,(ix,iy),(x,y),color,1)
            elif line == 1: 
                cv.line(img,(ix,iy), (x,y), color,thickness)
            elif circle == 1:
                cv.circle(img,(x,y),5,color,1)
            elif ellipse == 1:
                cv.ellipse(img, (ix,iy), (x,x), 0, 0, 360, color, 1)
            else:
                cv.putText(img, text, (ix,iy), cv.FONT_HERSHEY_COMPLEX, 4, color, thickness)                

def trackbar():
    cv.createTrackbar('Red','paint',0,255,nothing)
    cv.createTrackbar('Green','paint',0,255,nothing)
    cv.createTrackbar('Blue','paint',0,255,nothing)
    cv.createTrackbar('Brush Size', 'paint', 0, 10, nothing)
    cv.createTrackbar(shape,'paint', 0, 4, nothing)
    cv.createTrackbar('Filled:1 \nUnfilled: 0', 'paint', 0, 1, nothing)

def nothing():
    pass

def main():
    cv.namedWindow('paint')
    trackbar()
    cv.setMouseCallback('paint',drawShape)
    while(1):
        cv.imshow('paint',img)
        k = cv.waitKey(1) & 0xFF
        if k == 27:
            break
    cv.destroyAllWindows()

if __name__ == "__main__":
    main()
