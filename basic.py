import cv2

img = cv2.imread("images\wallpaper-imgs\yasuke-assassins-3840x2160-16782.jpeg")



resized_img = cv2.resize(img,(256, 144))

shape = resized_img.shape

# cv2.imshow(f"shape {shape}", resized_img)

cv2.waitKey(0)
