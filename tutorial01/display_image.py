import cv2
## Part 00: Reading the image
## imread function reads the image specified
img=cv2.imread('dispimg.jpg')
## Part 01: Reading the size of the image and performing operations
## reading and printing size of the image
(h,w)=img.shape[:2] 
print("The size of the image is",h,"x",w)

## to access the image's pixel at x=250 y=500 we can use the following
''' Sidenote #1:  
 OpenCV uses BGR ordering because it was a standard when OpenCV
 was being built.But now, RGB is the most common standard for ordering,
 even OpenCV could change its ordering to RGB but modifying it could break the code. 
'''
(b,g,r)=img[250,500]
print("R:",r," G:",g," B:",b)

##cropping the image to 400x600,220x500
Region_of_Interest = img[400:600,220:500] 

## resizing image 
# use cv2.resize function along with size
small=cv2.resize(img,(500,500))
# resize image to smaller size with fixed aspect ratio
# below is the standard formulae to perform the latter
r = 300.0/w
dim = (300,int(h * r))
# pass the args to resize the image
asp=cv2.resize(img,dim)
# resizing with imutils
import imutils
asp =imutils.resize(img,width=300)

# rotation of image 
#compute the center
center = (w//2,h//2)
## using getRotationMatrix2D to get the affine matrix
''' SideNotes 02- Syntax for getRotation2DMatrix
    1.center
    2.angle of rotation
    3.scale (uses isotropic scale factor)
    refer to https://docs.opencv.org/2.4/modules/imgproc/doc/geometric_transformations.html
'''
m = cv2.getRotationMatrix2D(center,-45.0,1.00)
## applying affine transformation
rotated=cv2.warpAffine(img,m,(w,h))

## performing rotation using imutils library
rotated_imutils=imutils.rotate(img,-45)
## non clipped rotation using imutils
rotate_bound=imutils.rotate_bound(img,45)
cv2.imshow("Image",rotate_bound)
cv2.waitKey(0)
