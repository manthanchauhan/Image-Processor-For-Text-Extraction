import cv2
import numpy as np

input = cv2.imread('sample_image_4.jpg', cv2.IMREAD_GRAYSCALE)
input = cv2.resize(input, (1366, 768))
aftrCnny = cv2.Canny(input, 100, 200)
# cv2.imshow('canny', aftrCnny)
aftrdilat = cv2.dilate(aftrCnny, np.ones((5, 5), np.uint8), iterations=1)
aftrdilat = cv2.dilate(aftrdilat, np.ones((5, 5), np.uint8), iterations=1)
# cv2.imshow('dilate', aftrdilat)

#counting boundary box
im2, countours, heirarchy = cv2.findContours(aftrdilat, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
initx1 = 10e9
inity1 = 10e9
initx2 = -1
inity2 = -1
for cntr in countours:
    x1, y1, w, h = cv2.boundingRect(cntr)
    x2 = x1 + w
    y2 = y1 + h
    if x1 < initx1:
        initx1 = x1
    if y1 < inity1:
        inity1 = y1
    if x2 > initx2:
        initx2 = x2
    if y2 > inity2:
        inity2 = y2
x1 = max(10, initx1 - 5)
y1 = max(10, inity1 - 5)
x2 = min(1366, initx2 + 5)
y2 = min(768, inity2 + 5)
# print(x1)
# print(x2)
# print(y1)
# print(y2)
crop = input[y1:y2, x1:x2]
cv2.imshow('crop', crop)
cv2.waitKey(0)
cv2.destroyAllWindows()

