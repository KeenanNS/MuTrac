#Simulation of autopull

import random
import sys
from simple_pid import PID
import matplotlib.pyplot as plt
import numpy as np

print('MH3 Autopull PID learning simulation')

# our input is displacement. d = f(pressure) where the function is some PID control

#pressure is a function of the load on the wheels. We can say that the load on the wheels is going to be 
#a function of weight of the sled which is a function of distance. and that this load will have some noise.
#so the function load = f(distance) will give us a mean, and we can sample some probability distribution from that

#distance is a function of velocity and time. Velocity is a function of net force and time.
#so all of our functions add up to 

# Distance = function of (velocity and time)
# Velocity = function of (net force and time)
# Net_force = function of (load and pressure) Pressure will get translated to ground force with the reduction
# Load = function of (distance)
# Pressure = function of (Load)
# Displacement = function of (Pressure)

P = int(sys.argv[1])
I = int(sys.argv[2])
D = int(sys.argv[3])
PRINT = int(sys.argv[4])

WEIGHT = 1600 * 4.44822 #TODO weight of tractor
MASS = WEIGHT / 9.8
VARIATION = 5 #TODO this is the amount that we thing the pressure will vary, (how much it could jump / time step)
MAX_PRESSURE = 4000 #psi or some other value
REDUCTION = 1
AREA = 1
#PRINT = False

class Pull:
	def __init__(self, P, I, D):
		self.P = P
		self.I = I
		self.D = D

	def Distance(self, velocities, time):
		avg_velocity = sum(velocities) / len(velocities)
		if PRINT:
			print("distance ", avg_velocity * time)
		return avg_velocity * time

	def Net_Force(self, Load, Pressure_in): # should be net work
		#TODO calculate overall reduction
		pull = Pressure_in * REDUCTION * AREA 

		net_force = pull - Load

		if PRINT:
			print("net_force ", net_force)

		return net_force

	def Velocity(self, net_force, prev_velocity,done):
		# Work_tractor - Work_sled = (1/2) * (mass_tractor)(Velocity^2 - prev_velocity^2)
		if (2 * net_force / MASS + (prev_velocity**2)) <= 0:
			return 0, True

		velocity = np.sqrt(2 * net_force / MASS + (prev_velocity**2))

		if PRINT:
			print("velocity", velocity)

		if velocity <= 0:
			done = True

		return velocity, done

	def Load(self, Distance): # Work of sled because * 1 second
		if PRINT:
			print("load ", Distance * 10 +2000)
		load = Distance * 10 +2000
		return load # TODO rate of change in load / unit of measurement (meters). 1000 represents inertia of sled on wheels

	def Measured_Pressure(self, Net_Force):
		pressure = 3999 #TODO this is the inverse of the reduction 
		if PRINT:
			print("pressure ", pressure)
		return random.triangular(pressure - VARIATION, pressure + VARIATION, pressure) # (min, max, mode) prob distribution

	def Presure_in(self, Pressure): #controlled by displacement, equivalent of applied force
		pid = PID(self.P, self.I, self.D, setpoint = 4000, output_limits = (3900, 4000))
		control = pid(Pressure)
		if PRINT:
			print ("control ", control)
		
		return control #this needs to get converted to new pressure it should be force before reduction

pull = Pull(P,I,D)

time = 0
prev_velocity = 0
distance = 0
done = False
pressure_in = 4000
Measured_Pressure = 3000
velocities = []
loads = []
net_forces = []
prev_net_force = 1000

while not done:
	if PRINT:
		print("step ***********************")
	

	load = pull.Load(distance)
	loads.append(load)
	pressure_in = pull.Presure_in(Measured_Pressure)
	net_force= pull.Net_Force(load, pressure_in)
	net_forces.append(net_force)
	velocity, done = pull.Velocity(net_force, prev_velocity,done)
	velocities.append(velocity)
	distance = pull.Distance(velocities, time)
	Measured_Pressure = pull.Measured_Pressure(net_force)
	prev_net_force = net_force
	prev_velocity = velocity
	time += 1

	if time == 200:
		break
	if done:
		print("steps" , time)
		break

if not PRINT:
	print("distance travelled is ", distance, "time elapsed is ", time)
	Time = list(range(time))
	plt.plot(Time, loads)
	plt.ylabel('load')
	plt.show()
	plt.plot(Time, net_forces)
	plt.ylabel('net_force')
	plt.show()
	plt.plot(Time, velocities)
	plt.ylabel('velocity')
	plt.show()










