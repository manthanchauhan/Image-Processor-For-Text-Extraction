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
    totlChars = len(chars)
    for j in range(0, totlChars, 2):
        cv2.rectangle(cropped, (chars[j] - 2, Lines[i] - 5), (chars[j + 1] + 2, Lines[i + 1] + 2), (255, 255, 255), 2)
cv2.imshow("text", cv2.resize(cropped,(1366, 768)))
cv2.waitKey(0)
cv2.destroyAllWindows()


