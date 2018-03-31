import cv2
import numpy as np
def binarize(crop):
    output1 = cv2.Canny(crop, 37, 160)
    output1 = cv2.dilate(output1, np.ones((5, 5), np.uint8), iterations=1)
    output3 = cv2.adaptiveThreshold(crop, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 41, 2)
    output3 = cv2.erode(output3, np.ones((4, 4), np.uint8), iterations=1)
    output2 = cv2.bitwise_and(output3, output1)
    output2 = cv2.dilate(output2, np.ones((8, 8), np.uint8), iterations=1)
    output2 = cv2.bitwise_not(output2)
    return output2
