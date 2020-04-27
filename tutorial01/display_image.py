import cv2
## imread function reads the image specified
img=cv2.imread('dispimg.jpg')
## read size of the image
(h,w)=img.shape[:2]
## imshow displays the image
print("The size of the image is",h,"x",w)
cv2.imshow("Image",img)
cv2.waitKey(0)
