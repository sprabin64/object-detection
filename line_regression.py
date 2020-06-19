import math
import numpy as np
import cv2

## x and y are two end points of your line 
x = (160, 1180)
y = (590, 590)
m,b = np.polyfit(x, y, 1)

## this is the object box coordinate.. usually we take centroid of the box
box = (186, 704)
y_result = m * box[0] + b
[print("line crossed!!!") if box[1] >= y_result else print("not crossed!!")]

cv2.namedWindow('output', cv2.WINDOW_NORMAL)

image = cv2.imread("ele2.jpg")
image = cv2.resize(image, (1280, 720))
cv2.line(image, (x[0], y[0]), (x[1], y[1]), (0, 0, 255), 3)

cv2.imshow("output", image)
cv2.waitKey()
