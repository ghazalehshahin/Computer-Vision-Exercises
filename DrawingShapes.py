from webbrowser import get
import cv2 as cv
import numpy as np

def drawShape(img, type):
    color = tuple(map(int,input("Color (Blue Green Red): ").split()))
    thickness = int(input("Thickness: "))
    if type == 1:
        point1 = tuple(map(int, input("Starting Coordinate (x y): ").split()))
        point2 = tuple(map(int, input("Ending Coordinate (x y): ").split()))
        cv.line(img, point1, point2, color, thickness)
    elif type == 2:
        point1 = tuple(map(int, input("Top-left Corner (x y): ").split()))
        point2 = tuple(map(int, input("Bottom-right Corner (x y): ").split()))
        cv.rectangle(img, point1, point2, color, thickness)
    elif type == 3:
        center = tuple(map(int, input("Center (x y): ").split()))
        radios = int(input("Radios: "))
        cv.circle(img, center, radios, color, thickness)
    elif type == 4:
        center = tuple(map(int, input("Center (x y): ").split()))
        axes = tuple(map(int, input("Axes Length (Major Minor): ").split()))
        angle = int(input("Angle of Rotation: "))
        startAngle = int(input("Start Angle: "))
        endAngle = int(input("End Angle: "))
        cv.ellipse(img, center, axes, angle, startAngle, endAngle, color, thickness)
    elif type == 5:
        lst = []
        n = int(input("Number of Coordinates: "))
        isClosed = bool(input("isClose: "))
        for i in range(0, n):
            el = [int(input()), int(input())]
            lst.append(el)
        pts = np.array(lst, np.int32)
        pts = pts.reshape((-1,1,2))
        cv.polylines(img, [pts], isClosed, color, thickness)
    else:
        text = input("Text to Insert: ")
        position = tuple(map(int, input("Position Coordinates (x y): ").split()))
        scale = int(input("Size of the Font: "))
        font = cv.FONT_HERSHEY_SIMPLEX
        cv.putText(img, text, position, font, scale, color, thickness)

def getInput():
    type = int(input("What shape do you want to make? 1-line, 2-rectangle, 3-circle, 4-ellipse, 5-polygon, 6-text"))
    if type < 1 or type > 6:
        print("please enter the correct number (between 1 to 6)")
        getInput()
    return type

def main():
    img = np.zeros((512,512,3), np.uint8)
    drawShape(img, getInput())
    cv.imshow("img", img)
    cv.waitKey(0)
    cv.destroyAllWindows()


if __name__ == "__main__":
    main()