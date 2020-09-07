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

def pressure_to_force(pressure_sensor_reading):
	#TODO, this shoud return the inverse sum of all the frictional forces on the 4 tires. 
	# You'll need to know the reduction of the tractor, and do a little physics. Try to incorporate
	# some loss factors for different components like the motors.

	#return net pull force
	return 0

def PID_iteration(Pull):
	#TODO
	#using the class "Pull", and copying the loop at the bottom, write a function that runs the simulation a bunch of 
	#times to figure out the best P I D values.

	# return P, I, D
	return 0

def pump_displacement(pressure_sensor_reading, desired_pressure):
	#TODO
	#write a function that maps displacement of the pump, to pressure in the lines. Basically, normalized to the 
	#interval [0:1], map how much juice the pump needs to let through, to achieve a certain pressure, and how quickly this should be 
	#done. Think PID

	#return displacement fraction ( from 0:1)
	return 0

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

	def net_work(self, work_sled, Pressure_in): # should be net work
		#TODO calculate overall reduction
		#pressure_to_force() TODO
		work_tractor = Pressure_in * REDUCTION * AREA 

		net_work = work_tractor - work_sled # * 1 second

		if PRINT:
			print("net work ", net_work)

		return net_work

	def Velocity(self, net_work, prev_velocity,done):
		# Work_tractor - Work_sled = (1/2) * (mass_tractor)(Velocity^2 - prev_velocity^2)

		if (2 * net_work / MASS + (prev_velocity**2)) <= 0:
			return 0, True

		velocity = np.sqrt(2 * net_work / MASS + (prev_velocity**2))

		if PRINT:
			print("velocity", velocity)

		if velocity <= 0:
			done = True

		return velocity, done

	def work_sled(self, Distance): # Work of sled because * 1 second
		if PRINT:
			print("work sled ", Distance * 50 + 1000)
		work_sled = Distance * 10 +2000 # * 1 second
		return work_sled # TODO rate of change in load / unit of measurement (meters). 1000 represents inertia of sled on wheels

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
sled_works = []
net_works = []
distances = []

while not done:
	if PRINT:
		print("step ***********************")
	

	work_sled = pull.work_sled(distance)
	sled_works.append(work_sled)
	pressure_in = pull.Presure_in(Measured_Pressure)
	net_work = pull.net_work(work_sled, pressure_in)
	net_works.append(net_work)
	velocity, done = pull.Velocity(net_work, prev_velocity,done)
	velocities.append(velocity)
	distance = pull.Distance(velocities, time)
	distances.append(distance)
	Measured_Pressure = pull.Measured_Pressure(net_work)
	prev_net_work = net_work
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
	plt.plot(Time, sled_works)
	plt.ylabel('load')
	plt.show()
	plt.plot(Time, net_works)
	plt.ylabel('net_force')
	plt.show()
	plt.plot(Time, velocities)
	plt.ylabel('velocity')
	plt.show()
	plt.plot(Time, distances)










