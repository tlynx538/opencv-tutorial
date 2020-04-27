import cv2
# imread function reads the image specified
img=cv2.imread('dispimg.jpg')
# imshow displays the image
cv2.imshow("Image",img)
cv2.waitKey(0)
