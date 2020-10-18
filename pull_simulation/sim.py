#Simulation of autopull

import random
import sys
from simple_pid import PID
import matplotlib.pyplot as plt
#import numpy as np

print('MH3 Autopull PID learning simulation')


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
		self.Msled = 1120
		self.Pslip = 13790000

	def load_sled(self, last_velocity):
		print("distance ",distance)
		#M * V = m * V
		momentum_force = 0.01 * self.Msled * last_velocity / 1 #second
		print("momentum ",momentum_force)
		friction = tot_distance * 100  + 4000
		sled_load = friction - momentum_force
		print("sled load ", sled_load)
		return sled_load

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
	def velocity(self, displacement, pressure, done):
		if pressure > self.Pslip:
			done = True


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
		return avg

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
	sled_load = pull.load_sled(last_velocity)
	pressure, done = pull.pressure(sled_load, done)
	# rpm = pull.get_rpms(pull.get_max_power(pump_factor),get_requested_power(flow * pressure))
	

	rpm = pull.get_rpms(13423, pull.get_requested_power(last_displacement, pressure))
	displacement = pull.work_tractor(pressure, pump_factor, rpm)
	displacements.append(displacement)
	#net_work= pull.net_work(work_sled, work_tractor)
	
	print(type(displacement))
	# velocity, done = pull.velocity(last_velocity, net_work, distance, done, displacement)
	velocity, done = pull.velocity(displacement, pressure, done)
	velocities.append(velocity)
	time += 1
	last_velocity = velocity
	last_pressure = pressure
	last_distance = distance


	if time == 100:
		break
	if done:
		print("steps" , time)
		break
plt.plot(range(0,time), velocities)
plt.show()






