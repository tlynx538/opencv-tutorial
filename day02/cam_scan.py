from transform import four_point_transform
from skimage.filters import threshold_local
import imutils 
import cv2
import numpy as np 

img=cv2.imread('images/receipt.jpg')
orig=img.copy()
ratio=img.shape[0]/500.0
img=imutils.resize(img,height=500)

# converting color
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# adding gaussian blur
gray=cv2.GaussianBlur(gray,(5,5),0)
# finding edges in the image
edge=cv2.Canny(gray,75,200)
# finding contours in the edged image 
cntr=cv2.findContours(edge.copy(),cv2.RETR_EXTERNAL ,cv2.CHAIN_APPROX_SIMPLE)
cntr=imutils.grab_contours(cntr)
cntr=sorted(cntr,key=cv2.contourArea,reverse=True)[:5]

for c in cntr:
      per=cv2.arcLength(c,True)
      approx=cv2.approxPolyDP(c,0.02*per,True)
      if(len(approx)==4):
          screenCnt = approx
          break
warped=four_point_transform(orig,screenCnt.reshape(4,2)*ratio)
warped=cv2.cvtColor(warped,cv2.COLOR_BGR2GRAY)
T=threshold_local(warped,11,offset=10,method="gaussian")
warped=(warped>T).astype("uint8")*255
warped=imutils.resize(warped,height=500)
final=imutils.rotate_bound(warped,-90)
cv2.imshow("Result",final)         
cv2.waitKey(0)