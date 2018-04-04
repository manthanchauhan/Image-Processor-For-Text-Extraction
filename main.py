import functnDefinitions
import cv2

input = cv2.imread('sample_image.jpg', cv2.IMREAD_GRAYSCALE)
binary = functnDefinitions.binarize(input)
tiltCrrctd = functnDefinitions.removeTilt(binary)
cropped = functnDefinitions.crop_It(tiltCrrctd)
# cv2.imshow('binary', cropped)
functnDefinitions.printToFile(cropped)
cv2.waitKey(0)


