import numpy as np
import cv2

bw = cv2.imread('doraemon.gif',0)
height, width = bw.shape[0:2]
cv2.imshow("Original BW", bw)

binary = np.zeros([height, width, 1],'uint8')
thresh = 85

for row in range(0, height):
    for col in range(0, width):
        if bw[row][col]> thresh:
            binary[row][col] = 255

cv2.imshow("Slow Binary", binary)

cv2.waitKey(0)
cv2.destroyAllWindows()
