import functnDefinitions
import cv2

input = cv2.imread('sample_image.jpg', cv2.IMREAD_GRAYSCALE)
cropped = functnDefinitions.crop_It(input)
binary = functnDefinitions.binarize(cropped)
functnDefinitions.printToFile(binary)


