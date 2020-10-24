import numpy as np
import csv
import matplotlib.pyplot as plt


class field:
	def __init__(self, coordinate_array, theta, num_rows):
		self.fake = 0
		self.coords = coordinate_array
		self.theta = theta
		self.num_rows = num_rows

	def normal_to_tilted(self, x, y):
		original = np.array([x,y])
		original = np.transpose(original)
		transform = np.array([[np.cos(self.theta), np.sin(self.theta)], [-np.sin(self.theta), np.cos(self.theta)]])
		return np.matmul(transform , original)

	def tilted_to_normal(self, x, y):
		original = np.array([x,y])
		original = np.transpose(original)
		transform = np.array([[np.cos(self.theta), -np.sin(self.theta)], [np.sin(self.theta), np.cos(self.theta)]])
		return np.matmul(transform , original)

	def get_width (self, transformed_coords):
		Xs = transformed_coords[:,0]
		left = np.amin(Xs)
		print(left)
		right = np.amax(Xs)
		print(right)
		return abs(left-right)

	def get_height(self, upper_coord_pair, row_node):
		a = row_node[0]
		b = row_node[1]
		x1 = upper_coord_pair[0][0]
		y1 = upper_coord_pair[0][1]
		x2 = upper_coord_pair[1][0]
		y2 = upper_coord_pair[1][1]
		height1 = y1 - b
		height2 = (y2 - y1) * (a - x1) / (x2 - x1)
		return height1 + height2

	def get_four_points(self, x_val):
		coordinate_array = self.coords
		x_last = coordinate_array[-1][0]
		points = []
		for i in range(0, len(coordinate_array)):
			x = coordinate_array[i][0]
			if (((x > x_val) and (x_last < x_val)) or ((x < x_val) and (x_last > x_val))):
				points.append(coordinate_array[i-1])
				points.append(coordinate_array[i])
			x_last = x
		return np.asarray(points)

	def get_Xs(self, width, min_x):
		increment = width / (1 + self.num_rows)
		Xs = []
		for i in range (1, num_rows - 1):
			Xs.append(i * increment)
		return np.asarray(Xs)




# with open('Track_example.txt', newline = '') as data: 
# 	coordinates = csv.reader(data, delimiter='\t')

#data.close()
coordinates = np.loadtxt('Track_example.txt', delimiter = '\t')
#coordinates = np.array([[50.854457, 4.377184],[52.518172,13.407759],[50.072651,14.435935],[48.853033,2.349553]])
field = field(coordinates,30,7)
plt.plot(coordinates)
plt.show()



x_val = field.get_width(coordinates)/2 + np.amin(coordinates[:,0])

print(field.get_four_points(x_val))

upper_coord_pair = np.array([[1,3],[4, 8]])
row_node = np.array([2, 1])

print(field.get_height(upper_coord_pair, row_node))