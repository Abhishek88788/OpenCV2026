import cv2
import numpy as np

#create a black image
img = np.zeros((512,512,3), np.uint8)
#np.unit8 meaans each pixel value can be from 0 to 255

# print(img.shape)

#rectangle
# cv2.rectangle(image, start_point, end_point, color, thickness)
cv2.rectangle(img, (100,100), (500,500), (255,255,255), 1)

cv2.line(img, (300,100), (300,500), (0,255,0), 1)
cv2.line(img, (100,300), (500,300), (0,255,0), 1)

#line though origin(of rectangle) to end(of rectangle)
cv2.line(img, (100,100), (500,500), (255,0,0), 1)

#line though top-right to bottom-left
cv2.line(img, (500,100), (100,500), (255,0,0), 1)

# w = (400-20)//2
# h = (400-20)//2
#circle
# cv2.circle(image, center_coordinates, radius, color, thickness)
cv2.circle(img, (300,300), 50, (123,25,231), 1)

cv2.circle(img, (300,300), 100, (123,25,231), 1)

cv2.imshow("Black Image", img)

cv2.waitKey(0)
cv2.destroyAllWindows()