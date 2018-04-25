import cv2
import numpy as np

def crop_It(input):
    afterDilat = cv2.dilate(input, np.ones((5, 5), np.uint8),iterations=15)
    # cv2.imshow("afterdilat", cv2.resize(afterDilat, (1366, 768)))
    im2, countours, heirarchy = cv2.findContours(afterDilat, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    initx1 = 10e9
    inity1 = 10e9
    initx2 = -1
    inity2 = -1
    for cntr in countours:
        if cv2.contourArea(cntr) <= 5000:
            continue
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
    crop = input[inity1:inity2,initx1:initx2]
    # cv2.imshow("cropped", cv2.resize(crop, (1366, 768)))
    # crop = cv2.erode(crop, np.ones((3, 3), np.uint8), iterations=1)
    return crop

def binarize(crop):
    output1 = cv2.Canny(crop, 37, 160)
    output1 = cv2.dilate(output1, np.ones((5, 5), np.uint8), iterations=1)
    output3 = cv2.adaptiveThreshold(crop, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 41, 2)
    output3 = cv2.erode(output3, np.ones((4, 4), np.uint8), iterations=1)
    output2 = cv2.bitwise_and(output3, output1)
    # cv2.imshow('1', cv2.resize(output1, (1366, 768)))
    # cv2.imshow('1', output1)
    # cv2.imshow('3', cv2.resize(output3, (1366, 768)))
    # cv2.imshow('3', output3)
    # cv2.imshow('2', cv2.resize(output2, (1366, 768)))
    # cv2.imshow('2', output2)
    return output2

def removeTilt(binary):
    textSpace = np.column_stack((np.where(binary > 0)))
    angle = cv2.minAreaRect(textSpace)[2]
    if angle < -45:
        angle = -(90 + angle)
    else:
        angle = - angle
    # print(angle)
    (h, w) = binary.shape[:2]
    centre = (w / 2, h / 2)
    M = cv2.getRotationMatrix2D(centre, angle, 1.0)
    tiltCrrctd = cv2.warpAffine(binary, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
    return tiltCrrctd

def getLines(cropped):
    lines = []
    h = cropped.shape[0]
    isline = False
    for i in range(0, h):
        segmntn = sum(cropped[i])
        if segmntn == 0 and isline == True:
            lines.append(i)
            isline = False
        if segmntn > 0 and isline == False:
            lines.append(i)
            isline = True
    return lines

def getchars(cropped, lwr, upr):
    chars = []
    w = cropped.shape[1]
    ischar = False
    for i in range(0, w):
        segmntn = 0
        for j in range(lwr + 1, upr):
            segmntn = segmntn + cropped[j][i]
        if segmntn <= 5 and ischar == True:
            chars.append(i)
            ischar = False
        elif segmntn > 5 and ischar == False:
            chars.append(i)
            ischar = True
    return chars





