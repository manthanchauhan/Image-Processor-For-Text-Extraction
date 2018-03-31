import cv2
from crop import crop_It
from binarization import binarize

input = cv2.imread('sample_image.jpg', cv2.IMREAD_GRAYSCALE)
cropped = crop_It(input)
binary = binarize(cropped)
cv2.imshow('output', cv2.resize(binary, (1366, 768)))
cv2.waitKey(0)
cv2.destroyAllWindows()

