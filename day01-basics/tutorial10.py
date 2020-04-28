import cv2
import imutils
img = cv2.imread('images/tetris_blocks.png')
## Part 02 : Counting objects on an image
## converting image to grayscale
'''
    Syntax for cvtColor(required)
    1.img
    2. conversion format (here we used BGR2GRAY to convert to grayscale)
'''    
gray1=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
## applying canny edge detection to find edges
edge1=cv2.Canny(gray1,30,100)
'''
    Syntax for canny (required)
    1.img (provide gray image)
    2.threshold 1
    3.threshold 2
'''    
## thresholding 
# thresholding removes lighter and darker parts regions of contour of images
'''
How thresholding works?
On passing the gray image we will get to know its color intensities
The color intensity of the tetris block is visible therefore it is assumed
that it can have greater 'gray' intensity, by tuning we find it ranges from 225
onwards towards white.

Syntax for threshold (required)
    1.gray image
    2.beginning intensity range
    3.ending intensity range
    4.enumerator (we used THRESH_BINARY_INV) 
       refer to 
https://docs.opencv.org/3.4.0/d7/d1b/group__imgproc__misc.html#ggaa9e58d2860d4afa658ef70a9b1115576a19120b1a11d8067576cc24f4d2f03754
'''
thresh=cv2.threshold(gray1,225,255,cv2.THRESH_BINARY_INV)[1]
'''
    threshold returns an array of size 2
    specifying thresh[1] returns the actual image with contours
    thresh[0] returns the starting range itself that is 225 
'''
# finding contours
'''
    cv2.findContours notes:
    1.this function accepts 8 bit image 
    it keeps non-zero pixels to be 1 otherwise 0
    the first argument is the img which should be an 8 bit image
    accepted images are canny,threshold etc (read OpenCV doc).

    2.contours -  detected contours
    we used CV_RETR_EXTERNAL 
    It retrieves only the extreme outer contours. 
    It sets hierarchy[i][2]=hierarchy[i][3]=-1 
    for all the contours.

    3. contour approximation method- 
    CV_CHAIN_APPROX_SIMPLE compresses horizontal, vertical, and diagonal segments
    and leaves only their end points. For example, an up-right rectangular contour
    is encoded with 4 points.
'''
cntr_cnt=cv2.findContours(thresh.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
cntr_cnt=imutils.grab_contours(cntr_cnt)
out=img.copy()
for i in cntr_cnt:
    cv2.drawContours(out,[i],-1,(240,0,155),4)
## final : writing the number of contours found
text="Number of contours found is {}".format(len(cntr_cnt))
cv2.putText(out,text,(10,20),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,255),2)

## erosion and dilations
# Erosions and dilations are typically used to reduce noise in binary images
# (a side effect of thresholding).
'''
 Syntax for erosion(required)
 1. threshold image
 2. kernel  is set to None
 3. iterations is set to 5
'''
erd=cv2.erode(thresh.copy(),None,iterations=5)
# performing dilations enlarges the contours 
## syntax for dilate is similar as that of erode (in this case)
dil=cv2.dilate(thresh.copy(),None,iterations=5)
## masking and bitwise ops
## we shall perform masking for the objects that got thresholded
mask=cv2.bitwise_and(img,img,mask=thresh.copy())
cv2.imshow("Final",mask) 
cv2.waitKey(0)