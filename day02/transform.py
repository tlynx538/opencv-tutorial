''' Building a 4 POINT perspective transform
    This method can help us get a birds eye 
    view of the image specified.
    It is useful in finding the distance between
    two objects if one object is behind another
'''
import numpy as np
import cv2 

'''
  we shall initially define order_points method
  that accepts the parameter pts which is a list 
  of coordinates of the rectangle. 
'''
def order_points(pts):
    #we shall initialize the rectangle with 
    # 0's containing 4 rows and 2 columns
    rect=np.zeros((4,2),dtype='float32')
    
    s=pts.sum(axis=1)
    #rect[0] i.e the top left will have lowest sum
    rect[0]=pts[np.argmin(s)]
    #rect[1] i.e the bottom right will have highest sum
    rect[2]=pts[np.argmax(s)]

    diff=np.diff(pts,axis=1)
    #rect[1] i.e the top right will have lowest difference
    rect[1]=pts[np.argmin(diff)]
    #rect[3] i.e the bottom left will have highest difference
    rect[3]=pts[np.argmax(diff)]

    # returns the rectangle itself
    return rect

def fourptransf(img,pts):
    #consistent ordering of points by order_point method
    rect=order_points(pts)
    (tl,tr,bl,br)=rect

    # compute max width of image 
    widthA=np.sqrt(((br[0]-bl[0])**2))+((br[1]-bl[1])**2)
    widthB=np.sqrt(((tr[0]-tl[0])**2))+((tr[1]-tl[1])**2)
    maxWidth=max(int(widthA),int(widthB))

    #compute max height of image
    heightA=np.sqrt(((tr[0]-br[0])**2))+((tr[1]-br[1])**2)
    heightB=np.sqrt(((tl[0]-bl[0])**2))+((tl[1]-bl[1])**2)
    maxHeight=max(int(heightA),int(heightB))

    #construct the birds eye view of the image
    dst=np.array([
        [0,0],
        [maxWidth-1,0],
        [maxWidth-1,maxHeight-1]
        [0,maxHeight-1]],dtype='float32')

    #computing the perspective transform matrix
    # perspectiveTransform Calculates a perspective transform from four pairs
    #  of the corresponding points.
    m = cv2.perspectiveTransform(rect,dst)
    # warpPerspective Applies a perspective transformation to an image.
    warp=cv2.warpPerspective(rect,m,(maxWidth,maxHeight))

    #return warped image
    return warp    

