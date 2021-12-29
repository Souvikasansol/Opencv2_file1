import numpy as np
import cv2

# Gray image store
img1 = cv2.imread('./pictures/1.jpeg',0)

canvas = np.zeros((300,300,3),dtype='uint8')
def display(win_name,img):
    cv2.imshow(win_name,img)
    cv2.waitKey(1000)
    cv2.destroyAllWindows()
    
#  bgr = blue / green / red
green=(0,255,0)
red=(0,0,255)
cv2.line(canvas,(0,0),(300,300),green)
cv2.line(canvas,(100,0),(300,300),red)
display('canvas',canvas)
