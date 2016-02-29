import numpy as np
import cv2  
import math 
import matplotlib.pyplot as plt
from PIL import Image
from tempfile import TemporaryFile
img = Image.open('groundtruth/Images/1-deer-valley-living-room6.jpg')
img = np.asarray(img);
edges = cv2.Canny(img,100,200);

#img = np.asarray(img)
#edges = np.asarray(edges)
print np.shape(img)

#print im1.dtype; Check points in the code 
#print im1.dtype; #check points in the code
###############################
img = cv2.imread('groundtruth/Images/1-deer-valley-living-room6.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,50,150,apertureSize = 3)
minLineLength = 100
maxLineGap = 5
lines = cv2.HoughLinesP(edges,1,np.pi/180,100,minLineLength,maxLineGap)
for x1,y1,x2,y2 in lines[0]:
    cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)

cv2.imwrite('houghlines5.jpg',img)
#print np.shape(lines[0])Check point for lines data type 
lines = lines.astype(float);
#####################The part after this is only for testing ##########333
line = lines[0];
m1 = (line[0,3]-line[0,1])/(line[0,2]-line[0,0]);
m2 = (line[1,3]-line[1,1])/(line[1,2]-line[1,0]);
#print m1,m2 Another testing point 
x_intersection =( line[1,1] - line[0,1])/(m1-m2) + x1;
y_intersection =line[1,1] + m2*(x_intersection - line[1,0]);
print x_intersection , y_intersection

