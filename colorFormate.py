import cv2
import numpy as np

#convert BGR to Grayscale

img = cv2.imread("image.png")
resized_img = cv2.resize(img,(256, 144))

orginalShape = resized_img.shape
cv2.imshow(f"shape {orginalShape}", resized_img)

gray_img = cv2.cvtColor(resized_img,cv2.COLOR_BGR2GRAY)

grayScaleShape = gray_img.shape
cv2.imshow(f"shape {grayScaleShape}", gray_img)

cv2.waitKey(0)