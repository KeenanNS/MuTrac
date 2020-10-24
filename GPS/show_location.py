
import numpy as np
import cv2
import time
import os
import gpsd
import matplotlib.pyplot as plt

os.system('killall gpsd')
os.system('sudo gpsd /dev/ttyACM0 -F /var/run/gpsd.sock')

#coords = [45.416254, -73.961567, 45.400113, -73.929394]
coords = [45.4268, -73.9718, 45.4017, -73.9172]

max_x = coords[0]
min_x = coords[2]
max_y = coords[3]
min_y = coords[1]

BBox = (min_x,  max_x,      
         min_y, max_y)

# lat_dimensions = abs(max_y - min_y)
# lon_dimensions = abs(max_x - min_x)

# img = cv2.imread('map.png')
# dimensions = img.shape

# pixels_per_x = dimensions[0] / lon_dimensions 
# pixels_per_y =  dimensions[1] / lat_dimensions

# img = plt.imread('map.png')
# fig, ax = plt.subplots(figsize = (8,7))
# ax.scatter(df.longitude, df.latitude, zorder=1, alpha= 0.2, c='b', s=10)
# ax.set_title('Plotting Spatial Data on Riyadh Map')
# ax.set_xlim(min_x,max_x)
# ax.set_ylim(min_y,max_y)
# ax.imshow(img , zorder=0, extent = BBox, aspect= 'equal')



gpsd.connect()
time.sleep(1)
packet = gpsd.get_current()
print(packet.position())

img = plt.imread('map.png')
fig, ax = plt.subplots(figsize = (8,7))
ax.scatter(packet.position()[0], packet.position()[1], zorder=1, alpha= 0.2, c='b', s=30)

#ax.set_xlim(min_x,max_x)
#ax.set_ylim(min_y,max_y)
ax.imshow(img , zorder=0,  aspect= 'equal')
plt.show()

# x = packet.position()[0] * pixels_per_x 
# y = packet.position()[1] * pixels_per_y 
# print('measured')
# print(x,y)

# diff_x = (packet.position()[0] - min_x) * pixels_per_x 
# print(diff_x)
# diff_y = (packet.position()[1] - min_y) * pixels_per_y
# print(diff_y)

# x = int(diff_x)
# y = int(diff_y)
# x1 = x + 4
# x2 = x - 4
# y1 = y + 4
# y2 = y - 4
# p1 = (x1, y1)
# p2 = (x2, y2)
# print(p1)
# print(p2)
# colour = (255,0,0) 

# cv2.rectangle(img, p1, p2, colour, 2)
# cv2.imshow('image',img)
# cv2.waitKey(0) 

# #closing all open windows  
# cv2.destroyAllWindows()






