import cv2
## reading the image 
img=cv2.imread('duck.jpeg')
## Part 1: drawing over image
''' Syntax of rectangle (required)
    1.image
    2.pt1 (length)
    3.pt2 (breadth)
    4.color (specify in (B,G,R) format)
'''
rect=img.copy()
cv2.rectangle(rect,(100,200),(200,300),(255,0,255))

'''
    Syntax of circle (required)
    1.image 
    2.center (coordinates for the location)
    3.radius (set radius)
    4.color in BGR format
    5.thickness (negative for solid, positive for circle)
'''
circle=img.copy()
cv2.circle(circle,(200,100),100,(0,0,255),2)
''' Syntax for drawing line (required)
    1.image
    2.pt1 
    3.pt2
    4.color
    5.thickness
'''
line1=img.copy()
cv2.line(line1,(100,200),(200,300),(0,0,255),2)

''' Syntax for displaying text (required)
    1. image
    2. text
    3. coordinate
    4. Font face
    5. Scale factor
    6. Color
    7. Thickness
'''
text1= img.copy()
cv2.putText(text1,"Donald Duck",(20,30),cv2.FONT_HERSHEY_PLAIN,1,(255,0,255),1)
cv2.imshow("Image",text1)
cv2.waitKey(0)