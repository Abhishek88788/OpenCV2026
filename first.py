import cv2
#.imaread() function is used to read an image from a specified file.    
img1 = cv2.imread("images\\wallpaper-imgs\\assassins-creed-12000x6871-16786.jpeg")
# img2 = cv2.imread("images\\wallpaper-imgs\\ananta-video-game-1920x1080-24099.jpg")

# resize (scale down)
#resize() function is used to resize an image to a specified width and height.
# Here, we are resizing img1 to 1200x700 pixels.
img_resized1 = cv2.resize(img1, (1200, 700))
# img_resized2 = cv2.resize(img2, (600, 400))

cv2.imshow("My Image", img_resized1)
cv2.waitKey(0)
cv2.destroyAllWindows()
