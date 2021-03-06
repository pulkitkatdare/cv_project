import numpy as np
import cv2  
import math
import sys 
import matplotlib.pyplot as plt
from PIL import Image
from tempfile import TemporaryFile
import pdb

img = Image.open('groundtruth/Images/0000000041.jpg')
img = np.asarray(img);
edges = cv2.Canny(img,00,200);
cv2.imwrite('check.jpg',edges);
img = cv2.imread('groundtruth/Images/0000000041.jpg')
#gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(img,50,150,apertureSize = 3)
minLineLength = 50
maxLineGap = 10
lines = cv2.HoughLinesP(edges,1,np.pi/180,100,minLineLength,maxLineGap)
for x1,y1,x2,y2 in lines[0]:
    cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)

cv2.imwrite('houghlines5.jpg',img)
img = cv2.imread('groundtruth/Images/0000000041.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
equ = cv2.equalizeHist(img)
edges = cv2.Canny(equ,50,150,apertureSize = 3)
minLineLength = 50
maxLineGap = 10
lines = cv2.HoughLinesP(edges,1,np.pi/180,100,minLineLength,maxLineGap)
img = cv2.imread('groundtruth/Images/0000000041.jpg')
for x1,y1,x2,y2 in lines[0]:
    cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)
cv2.imwrite('houghlines.jpg',img)

