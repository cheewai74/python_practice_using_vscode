
import cv2


img = cv2.imread('doraemon.gif')
cv2.namedWindow("Image", cv2.WINDOW_NORMAL)
cv2.imshow('image', img)


# waits for user to press any key
# (this is necessary to avoid Python kernel form crashing)
cv2.waitKey(0)
cv2.imwrite("output.jpg", img)

# closing all open windows
cv2.destroyAllWindows()
