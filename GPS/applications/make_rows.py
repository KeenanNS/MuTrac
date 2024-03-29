import numpy as np
import csv
import matplotlib.pyplot as plt
import utm

class field():
	def __init__(self, coordinate_array, theta, num_rows):
		self.coords = coordinate_array
		self.theta = theta
		self.num_rows = num_rows

	def to_xy(self):
		vals = []
		for i in range(0,len(self.coords)):
			val = utm.from_latlon(self.coords[i][0], self.coords[i][1])
			vals.append(val[:2])	
		self.coords = np.asarray(vals)	
		self.min_x = np.amin(self.coords[:,0])
		self.min_y = np.amin(self.coords[:,1])

		self.coords[:,0] = self.coords[:,0] - self.min_x
		self.coords[:,1] = self.coords[:,1] - self.min_y
		return np.amin(self.coords[:,0])

	def normal_to_tilted(self):
		new_coords = []
		transform = np.array([[np.cos(self.theta), -np.sin(self.theta)], [np.sin(self.theta), np.cos(self.theta)]])
		for i in range(0, len(self.coords)):
			new_coords.append(np.matmul(transform , self.coords[i]))
		self.coords = np.asarray(new_coords)
		self.shift_right = np.amin(self.coords[:,0])
		self.shift_left = np.amin(self.coords[:,1])
		self.coords[:,0] = self.coords[:,0] - np.amin(self.coords[:,0])
		self.coords[:,1] = self.coords[:,1] - np.amin(self.coords[:,1])
		

	def tilted_to_normal(self, nodes):
		new_coords = []
		new_nodes = []
		transform = np.array([[np.cos(-self.theta), -np.sin(-self.theta)], [np.sin(-self.theta), np.cos(-self.theta)]])
		self.coords[:,0] = self.coords[:,0] + self.shift_right
		self.coords[:,1] = self.coords[:,1] + self.shift_left
		nodes[:,0] = nodes[:,0] + self.shift_right
		nodes[:,1] = nodes[:,1] + self.shift_left

		for i in range(0, len(self.coords)):
			new_coords.append(np.matmul(transform , self.coords[i]))
		self.coords = np.asarray(new_coords)

		for j in range(0, len(nodes)):
			new_nodes.append(np.matmul(transform , nodes[j]))

		return np.asarray(new_nodes)

	def get_width (self):
		Xs = self.coords[:,0]
		left = np.amin(Xs)
		right = np.amax(Xs)
		return abs(left-right)

	def get_nodes(self, n_four_points, Xs):
		nodes = []
		for i in range(0,len(Xs)):
			point1 = n_four_points[i][0]
			point2 = n_four_points[i][1]
			point3 = n_four_points[i][2]
			point4 = n_four_points[i][3]
			X1 = Xs[i]
			X2 = Xs[i]
			Y1 = point2[1] + ((Xs[i] - point2[0]) * abs(point1[0] - point2[1] / point1[0] - point2[0]))
			Y2 = point4[1] + ((Xs[i] - point4[0]) * abs(point3[0] - point4[0] / point3[0] - point4[0]))
			nodes.append([X1, Y1])
			nodes.append([X2, Y2])
			ret = np.asarray(nodes)
		return ret

	def get_four_points(self, Xs):
		coordinate_array = self.coords
		n_four_points = []
		for j in range(len(Xs)):
			x_last = coordinate_array[-1][0]
			points = []
			for i in range(0, len(coordinate_array)):
				x = coordinate_array[i][0]
				if (((x > Xs[j]) and (x_last < Xs[j])) or ((x < Xs[j]) and (x_last > Xs[j]))):
					points.append(coordinate_array[i-1])
					points.append(coordinate_array[i])
				x_last = x
			points = np.asarray(points)
			n_four_points.append(points) 			
		return np.asarray(n_four_points)

	def get_Xs(self, width, min_x):
		Xs = np.array([])
		increment = width / (1 + self.num_rows)
		for i in range (1, self.num_rows +1):
			Xs = np.concatenate((Xs, [increment *i]))
		return np.asarray(Xs)

	def gradient(self):
		from skspatial.objects import Plane
		from skspatial.objects import Points
		from skspatial.plotting import plot_3d
		# do fit
		tmp_A = []
		tmp_b = []
		for i in range(len(self.coords)):
		    tmp_A.append([self.coords[i, 0], self.coords[i, 1], 1])
		    tmp_b.append(self.coords[i, 2])
		b = np.matrix(tmp_b).T
		A = np.matrix(tmp_A)

		# Manual solution
		fit = (A.T * A).I * A.T * b
		print(fit)
		angle = np.arctan(fit[0]/fit[1])
		print(np.degrees(angle))
		errors = b - A * fit
		residual = np.linalg.norm(errors)
		points = Points(self.coords)

		plane_fit = Plane.best_fit(points)
		print(plane_fit)
		print(np.degrees(np.arctan(plane_fit.vector[0]/plane_fit.vector[1])))
		

coordinates = np.loadtxt('F22_Elevation.txt', delimiter = '\t', skiprows=1, usecols=(0,1,3))
print(coordinates)
#coordinates = np.array([[50.854457, 4.377184],[52.518172,13.407759],[50.072651,14.435935],[48.853033,2.349553]])
field = field(coordinates,np.radians(0),5)
field.gradient()
exit()
#field = field(coordinates,0,7)
min_x = field.to_xy()
plt.plot(field.coords[:,0], field.coords[:,1])
tilted = field.normal_to_tilted()



w = field.get_width()
Xs = field.get_Xs(w, min_x)
n4 = field.get_four_points(Xs)
nodes = field.get_nodes(n4, Xs)
nodes = field.tilted_to_normal(nodes)

i = 0
while i < len(nodes):
	cpl_x = []
	cpl_y = []
	cpl_x.append(nodes[i][0])
	cpl_x.append(nodes[i+1][0])
	cpl_y.append(nodes[i][1])
	cpl_y.append(nodes[i+1][1])
	plt.plot(cpl_x, cpl_y)
	i += 2

plt.show()
