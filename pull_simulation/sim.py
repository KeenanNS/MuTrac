#Simulation of autopull

import random
import sys
from simple_pid import PID
import matplotlib.pyplot as plt
#import numpy as np

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

# P = int(sys.argv[1])
# I = int(sys.argv[2])
# D = int(sys.argv[3])
# PRINT = int(sys.argv[4])

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
	# def __init__(self, P, I, D):
	def __init__(self):
		# self.P = P
		# self.I = I
		# self.D = D
		self.flowrate = 0.000655483 / 12 # m^3
		self.max_flow = self.flowrate * 3400 / 60
		self.max = 18
		self.weight = 7700
		self.Msled = 11120

	def work_sled(self, distance, tot_distance, last_velocity):
		print("distance ",distance)
		#M * V = m * V
		momentum_force = self.Msled * last_velocity / 1 #second
		friction = tot_distance * 100  + 200
		sled_load = friction - momentum_force
		print("sled load ", sled_load)
		return sled_load * distance, sled_load

	def work_tractor(self, pressure, pump_factor, rpm):
		rps = rpm / 60
		flow = self.flowrate * rps
		displacement = pump_factor * rps * self.flowrate
		print("dispalcement ", displacement)
		return displacement # , pressure * diosplacent

	def get_max_power(self, pump_factor):
		#return pump_factor * 18
		return 13423 #watts

	def get_requested_power(self, displacement, pressure):
		print("pressure inside requested ", pressure)
		print("displacement inside requested ", displacement)
		print("request ",displacement * pressure)
		return displacement * pressure

	def get_rpms(self, max_power, requested_power):
		if requested_power > max_power :
			rpm = 3400 + (max_power - requested_power) * 100
		else :rpm = 3400
		print("the rpms ",  rpm)
		return max(rpm, 0)

	def pump_factor(self, max_power, last_pressure):
		print("pump factor ", pump_factor)
		print("LAST PRESSURE ", last_pressure)
		# return max_power / ((last_pressure * flow) +1)
		desired_flow = max_power / last_pressure
		ratio = desired_flow / self.max_flow 
		print("ratio ", ratio)
		ratio = min(1, ratio)
		return max(ratio, 0.3)
		

	def net_work(self, work_sled, work_tractor):
		net_work = work_tractor - work_sled
		print("tractor work", work_tractor)
		print("sled work ", work_sled)
		print("net work ",net_work)
		return net_work

	# def velocity(self, last_velocity, net_work, distance, done, displacement):
	def velocity(self, displacement, done):

		# net_force = net_work / (distance +1)
		# acceleration = net_force / self.weight
		# V = last_velocity + acceleration
		V = displacement * 6740

		if V <= 0.1:
			done = True
		#return V, done # * 1 timestep
		print("velocity ", V)
		return V, done

	def tot_distance(self, velocities, time, displacements):
		try:
			avg = sum(velocities) / len(velocities)
		except:
			avg = 0
		# return avg * time
		print("tot_distance ", tot_distance)
		return sum(displacements) * 6740

		#this could just as easily be (sum(velocities)) but this is easier to follow

	def pressure(self, sled_load, done):
		P = sled_load / ((0.02 ** 2) * 3.14)
		if P > 27579000:
			done = True

		return P, done#, 27579000)


pull = Pull()
tot_distance = 0
last_distance = 0
last_pressure = 1
last_displacement = pull.flowrate
pump_factor = 1
velocity = 0
last_velocity = 0
velocities = []
displacements = []
time = 0
done = False
flow = 0


	

while not done:
	
	print("step ", time, "tot_distance ", tot_distance, "velocity ", velocity)
	
	tot_distance = pull.tot_distance(velocities, time, displacements)
	distance = tot_distance - last_distance
	pump_factor = pull.pump_factor(pull.get_max_power(pump_factor), last_pressure)
	work_sled, sled_load = pull.work_sled(distance, tot_distance, last_velocity)
	pressure, done = pull.pressure(sled_load, done)
	# rpm = pull.get_rpms(pull.get_max_power(pump_factor),get_requested_power(flow * pressure))
	

	rpm = pull.get_rpms(13423, pull.get_requested_power(last_displacement, pressure))
	displacement = pull.work_tractor(pressure, pump_factor, rpm)
	displacements.append(displacement)
	#net_work= pull.net_work(work_sled, work_tractor)
	
	print(type(displacement))
	# velocity, done = pull.velocity(last_velocity, net_work, distance, done, displacement)
	velocity, done = pull.velocity(displacement, done)
	velocities.append(velocity)
	time += 1
	last_velocity = velocity
	last_pressure = pressure
	last_distance = distance
	# work_sled = pull.work_sled(distance)
	# sled_works.append(work_sled)
	# pressure_in = pull.Presure_in(Measured_Pressure)
	# net_work = pull.net_work(work_sled, pressure_in)
	# net_works.append(net_work)
	# velocity, done = pull.Velocity(net_work, prev_velocity,done)
	# velocities.append(velocity)
	# distance = pull.Distance(velocities, time)
	# Last_distance = distance
	# distances.append(distance)
	# Measured_Pressure = pull.Measured_Pressure(net_work)
	# prev_net_work = net_work
	# prev_velocity = velocity
	# time += 1

	if time == 100:
		break
	if done:
		print("steps" , time)
		break
plt.plot(range(0,time), velocities)
plt.show()



	# def Distance(self, velocities, time):
	# 	avg_velocity = sum(velocities) / len(velocities)
	# 	if PRINT:
	# 		print("distance ", avg_velocity * time)
	# 	return avg_velocity * time

	# def net_work(self, work_sled, Pressure_in): # should be net work
	# 	#TODO calculate overall reduction
	# 	#pressure_to_force() TODO
	# 	work_tractor = Pressure_in * REDUCTION * AREA 

	# 	net_work = work_tractor - work_sled # * 1 second

	# 	if PRINT:
	# 		print("net work ", net_work)

	# 	return net_work

	# def Velocity(self, net_work, prev_velocity,done):
	# 	# we have net work over 1 timestep. so net work is equal to power in this case. power is force * velocity.
	# 	# the force is going to be related to the momentum of the system I think.

	# 	# F * v  = F * v

	# 	if (2 * net_work / MASS + (prev_velocity**2)) <= 0:
	# 		return 0, True

	# 	velocity = np.sqrt(2 * net_work / MASS + (prev_velocity**2))

	# 	if PRINT:
	# 		print("velocity", velocity)

	# 	if velocity <= 0:
	# 		done = True

	# 	return velocity, done

	# def work_sled(self, Distance, Last_distance): # Work of sled because * 1 second
	# 	if PRINT:
	# 		print("work sled ", Distance * 50 + 1000)
	# 	delta = Distance - Last_distance
	# 	work_sled = (Distance * 10 +2000 )* delta# * 1 second
	# 	return work_sled # TODO rate of change in load / unit of measurement (meters). 1000 represents inertia of sled on wheels

	# def Measured_Pressure(self, Net_Force):
	# 	pressure = 3999 #TODO this is the inverse of the reduction 
	# 	if PRINT:
	# 		print("pressure ", pressure)
	# 	return random.triangular(pressure - VARIATION, pressure + VARIATION, pressure) # (min, max, mode) prob distribution

	# def work_shaft(self, Pressure): #controlled by displacement, equivalent of applied force
	# 	pid = PID(self.P, self.I, self.D, setpoint = 4000, output_limits = (3900, 4000))
	# 	control = pid(Pressure)
	# 	if PRINT:
	# 		print ("control ", control)
	# 	flow_rate = 3400 / 12 * 19.9
	# 	work = control * flow_rate
	# 	return control #this needs to get converted to new pressure it should be force before reduction

# pull = Pull(P,I,D)

# time = 0
# prev_velocity = 0
# Last_distance = 0
# distance = 0
# done = False
# pressure_in = 4000
# Measured_Pressure = 3000
# velocities = []
# sled_works = []
# net_works = []
# distances = []

# while not done:
# 	if PRINT:
# 		print("step ***********************")
	

# 	# work_sled = pull.work_sled(distance)
# 	# sled_works.append(work_sled)
# 	# pressure_in = pull.Presure_in(Measured_Pressure)
# 	# net_work = pull.net_work(work_sled, pressure_in)
# 	# net_works.append(net_work)
# 	# velocity, done = pull.Velocity(net_work, prev_velocity,done)
# 	# velocities.append(velocity)
# 	# distance = pull.Distance(velocities, time)
# 	# Last_distance = distance
# 	# distances.append(distance)
# 	# Measured_Pressure = pull.Measured_Pressure(net_work)
# 	# prev_net_work = net_work
# 	# prev_velocity = velocity
# 	# time += 1

# 	if time == 200:
# 		break
# 	if done:
# 		print("steps" , time)
# 		break

# if not PRINT:
# 	print("distance travelled is ", distance, "time elapsed is ", time)
# 	Time = list(range(time))
# 	plt.plot(Time, sled_works)
# 	plt.ylabel('load')
# 	plt.show()
# 	plt.savefig('load.png')
# 	plt.plot(Time, net_works)
# 	plt.ylabel('net_force')
# 	plt.savefig('net_force.png')
# 	plt.show()
# 	plt.plot(Time, velocities)
# 	plt.ylabel('velocity')
# 	plt.savefig('velocity.png')
# 	plt.show()
# 	plt.plot(Time, distances)










