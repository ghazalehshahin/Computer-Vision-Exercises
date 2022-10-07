from genericpath import isfile
import numpy as np
import cv2 as cv
import os.path


def main():
    # captureCamera()
    # captureVideo()
    saveVideo()

def captureCamera():
    cap = cv.VideoCapture(0)
    if not cap.isOpened():
        print("Cannot open camera")
        exit()
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        cv.imshow('frame', gray)
        if cv.waitKey(1) == ord('q'):
            break
    cap.release()
    cv.destroyAllWindows()

def captureVideo():
    cap = cv.VideoCapture('movies/movie1.mkv')
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        cv.imshow('frame', gray)
        if cv.waitKey(1) == ord('q'):
            break
    cap.release()
    cv.destroyAllWindows()

def saveVideo():
    cap = cv.VideoCapture(0)
    fourcc = cv.VideoWriter_fourcc(*'DIVX')
    fileName = nameChecker()
    out = cv.VideoWriter(fileName, fourcc, 20.0, (640,  480))
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break
        frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        out.write(frame)
        cv.imshow('frame', frame)
        if cv.waitKey(1) == ord('q'):
            break
    cap.release()
    out.release()
    cv.destroyAllWindows()

def nameChecker():
    status = False
    i = 0
    while status == False:
        if os.path.isfile('movies/movie{}.mkv'.format(i)):
            i += 1
        else:
            fileName = 'movies/movie{}.mkv'.format(i) 
            status = True
    return fileName

if __name__ == "__main__":
    main()