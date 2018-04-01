import cv2
import numpy as np
from PIL import Image
import pytesseract

def crop_It(input):
    aftrCnny = cv2.Canny(input, 100, 160)
    aftrdilat = cv2.dilate(aftrCnny, np.ones((5, 5), np.uint8), iterations=1)
    aftrdilat = cv2.dilate(aftrdilat, np.ones((5, 5), np.uint8), iterations=1)

    #finding boundary box of crop
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
    crop = input[inity1 - 5:inity2 + 5, initx1 - 5:initx2 + 5]
    return crop

def binarize(crop):
    output1 = cv2.Canny(crop, 37, 160)
    output1 = cv2.dilate(output1, np.ones((5, 5), np.uint8), iterations=1)
    output3 = cv2.adaptiveThreshold(crop, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 41, 2)
    output3 = cv2.erode(output3, np.ones((4, 4), np.uint8), iterations=1)
    output2 = cv2.bitwise_and(output3, output1)
    output2 = cv2.dilate(output2, np.ones((8, 8), np.uint8), iterations=1)
    output2 = cv2.bitwise_not(output2)
    output2 = cv2.dilate(output2, np.ones((4, 4), np.uint8), iterations=1)
    return output2

def printToFile(binary):
    image = Image.fromarray(binary)
    text = pytesseract.image_to_string(image, lang='eng')
    string = text.encode('utf-8')
    with open('output.txt', 'w') as file:
        print(f"{string}", file=file)
