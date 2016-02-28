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
cv2.imwrite('edges.jpg',edges)
im1 = Image.open('groundtruth/Images/1-deer-valley-living-room6.jpg',);
im1 = np.asarray(im1);   
#print im1.dtype; Check points in the code 
im1 = im1.astype(float);
#print im1.dtype; #check points in the code 
	