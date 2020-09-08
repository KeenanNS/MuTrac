# import cv2

# cv2.namedWindow("preview")
# vc = cv2.VideoCapture(0)

# if vc.isOpened(): # try to get the first frame
#     rval, frame = vc.read()
# else:
#     rval = False
# # while rval:
# #     cv2.imshow("preview", frame)
# #     rval, frame = vc.read()
# #     key = cv2.waitKey(20)
# #     if key == 27: # exit on ESC
# #         break
# # cv2.destroyWindow("preview")

# # Python program to illustrate HoughLine 
# # method for line detection 
# import cv2 
# import numpy as np 

# # Reading the required image in 
# # which operations are to be done. 
# # Make sure that the image is in the same 
# # directory in which this python program is 
# rval, frame = vc.read()
# img = cv2.imread('bars') 

# # Convert the img to grayscale 
# gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) 

# # Apply edge detection method on the image 
# edges = cv2.Canny(gray,50,150,apertureSize = 3) 

# # This returns an array of r and theta values 
# lines = cv2.HoughLines(edges,1,np.pi/180, 200) 

# # The below for loop runs till r and theta values 
# # are in the range of the 2d array 
# for r,theta in lines[0]: 
	
# 	# Stores the value of cos(theta) in a 
# 	a = np.cos(theta) 

# 	# Stores the value of sin(theta) in b 
# 	b = np.sin(theta) 
	
# 	# x0 stores the value rcos(theta) 
# 	x0 = a*r 
	
# 	# y0 stores the value rsin(theta) 
# 	y0 = b*r 
	
# 	# x1 stores the rounded off value of (rcos(theta)-1000sin(theta)) 
# 	x1 = int(x0 + 1000*(-b)) 
	
# 	# y1 stores the rounded off value of (rsin(theta)+1000cos(theta)) 
# 	y1 = int(y0 + 1000*(a)) 

# 	# x2 stores the rounded off value of (rcos(theta)+1000sin(theta)) 
# 	x2 = int(x0 - 1000*(-b)) 
	
# 	# y2 stores the rounded off value of (rsin(theta)-1000cos(theta)) 
# 	y2 = int(y0 - 1000*(a)) 
	
# 	# cv2.line draws a line in img from the point(x1,y1) to (x2,y2). 
# 	# (0,0,255) denotes the colour of the line to be 
# 	#drawn. In this case, it is red. 
# 	cv2.line(img,(x1,y1), (x2,y2), (0,0,255),2) 
	
# # All the changes made in the input image are finally 
# # written on a new image houghlines.jpg 
# cv2.imwrite('linesDetected.jpg', img) 
import cv2
import sys
from PIL import Image
import numpy as np
vc = cv2.VideoCapture(0)

if vc.isOpened():
	print("is open")
	rval, frame = vc.read()
else:
    rval = False
while rval:
    rval, frame = vc.read()
    # rgb = Image.fromarray(frame)
    # rgb2 = np.float32(rgb)
    cascPath = "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(cascPath)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray2 = np.array(gray, dtype='uint8')
    faces = faceCascade.detectMultiScale(gray2,scaleFactor=1.1,minNeighbors=5,minSize=(30, 30))
    #faces = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    
    key = cv2.waitKey(20)
    if key == 27:
    		break

    for (x, y, w, h) in faces:
    	cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
    cv2.imshow('image', frame)
    	
    	


