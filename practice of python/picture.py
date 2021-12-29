import numpy as np
import cv2

# Gray image store
img1 = cv2.imread('./pictures/1.jpeg',0)

# print(img)
img1.shape
def image(img):
    cv2.imshow('window',img)
    cv2.waitKey(2000)
    cv2.destroyAllWindows()

# Save an image
# cv2.imwrite('exaple.png',img1)

image(img1)