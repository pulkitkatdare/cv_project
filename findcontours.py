import numpy as np
import math 
import matplotlib.pyplot as plt
#from cv2.cv import *
from PIL import Image
from tempfile import TemporaryFile
from numpy import linalg as LA
import numpy as np
import cv2
from cv2.cv import *


im = cv2.imread('groundtruth/Images/0000000041.jpg');#Read the Input Image 
imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)# Converting it into gray scale 
ret,thresh = cv2.threshold(imgray,127,255,0)#thresholding of image 
contours, im2 = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)# contour detection 
#dist = cv2.pointPolygonTest(contours[0],(50,50),True)
#for h,cnt in enumerate(contours):
cnt = contours[0];
mask = np.zeros(imgray.shape,np.uint8)
cv2.drawContours(im,[cnt],0,255,3)
mean = cv2.mean(im,mask = mask)

cv2.imwrite('newone.jpg',imgray);
