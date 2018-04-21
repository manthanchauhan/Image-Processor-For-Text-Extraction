import functnDefinitions
import cv2
import sys

inputFile = str(sys.argv[-1])
input = cv2.imread(inputFile, cv2.IMREAD_GRAYSCALE)
binary = functnDefinitions.binarize(input)
tiltCrrctd = functnDefinitions.removeTilt(binary)
# tiltCrrctd = binary
cropped = functnDefinitions.crop_It(tiltCrrctd)
# cropped = tiltCrrctd
Lines = functnDefinitions.getLines(cropped)
(h, w) = cropped.shape[:2]
totlLines = len(Lines)
for i in range(0, totlLines, 2):
    chars = functnDefinitions.getchars(cropped, Lines[i], Lines[i + 1])
    for j in chars:
        cv2.line(cropped, (j, Lines[i]), (j, Lines[i + 1]), (255, 255, 255), 2)
for i in Lines:
    cv2.line(cropped, (0, i), (w, i), (255, 255, 255), 2)
cv2.imshow('binary', cropped)
functnDefinitions.printToFile(tiltCrrctd)
cv2.waitKey(0)


