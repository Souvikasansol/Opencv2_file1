import numpy as np
import cv2

# Gray image store
img1 = cv2.imread('./bg.png',0)
img2 = cv2.imread('./Group 9.png',0)

canvas = np.zeros((300,300,3),dtype='uint8')
def display(win_name,img):
    cv2.imshow(win_name,img)
    cv2.waitKey(1000)
    cv2.destroyAllWindows()
    
#  bgr = blue / green / red

display('canvas',img2)
cv2.imwrite('form.png',img2)