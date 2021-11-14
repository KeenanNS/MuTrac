#This is a Simulation of a tractor pull and is the property of the McGill University Trcator Pulling Team. Contact keenan.simpson1999@gmail.com if you wish to use this software.


import numpy as np
import math

GRAVITY = 10 # lol
BASE_RATIO = 11.7 # engine rpm to motor rpm
MAX_DISPLACEMENT = 0.009 # flow rate of oil in m^3 
TIRE_DIAMETER = 1 # meter this is also wrong


class Tractor:
	def __init__(self, length, mass, hitch_height):
		self.length = length #meters
		self.mass = mass #grams
		self.tire_diameter = 4 # example
		self.exampleConstantProperty = 69 # this one is constant and is not taken as an argument
		self.displacement = None
		# etc just add stuff you need

	def get_displacement(self, theta):
		self.displacement = theta * MAX_DISPLACEMENT
		return theta * MAX_DISPLACEMENT

	def get_weight(self):
		return self.mass * GRAVITY

	def get_rpms(self):
		#TODO this should be a function of load etc
		return 3600.0
		#this is new work, idk how to do this. You probably need to look at documents or run an experiment

	def max_available_power(self, theta):
		peak_power = 61591000 - 49681800 / theta - 4866 * math.log(theta) 
		peak_power = peak_power * 4.86 - 2184 / self.get_rpms() - 0.440 * math.log(self.get_rpms())
		return peak_power # in watts

		# this is where autopull comes into play. theta is a fraction we adjust to compensate for load. as of now it is always 1
	def get_requested_power(self, theta, load):
		return self.get_rpms() * self.get_displacement(theta) * load

	def get_distance_from_displacement(self): # this is wheere you'll determine your time base 
		return self.displacement * BASE_RATIO * TIRE_DIAMETER


class PullingSurface:
	def __init__(self, hydration, temperature): # idk what we'll need and this is more advanced. probably just use one default surface
		pass

	def get_tire_friction(self):
		return 1 # coefficient of friction for now just google what it is for tractors on dirt

	def get_sled_friction(self):
		return 0.4 # same as above but for the sled plate

class Sled:
	def __init__(self, rate_of_increase, starting_weight):
		self.rate_of_increase = rate_of_increase
		self.starting_weight = starting_weight

	def get_current_load(self, current_position):
		return self.starting_weight + self.rate_of_increase * current_position # load increases per meter this is wrong it should be based on friction

## this is the dynamics part and is where it gets actually complicated with momentum and such. That, I'll leave to you

def get_net_force():
	pass

# at each time step you need to determine the load of the sled 

MH2 = Tractor(1,1,1) # this is where the __init__ method gets called
sled = Sled(100, 10000)

current_position = 0

# for now, have this run and output a reasonable number ~ 100 meters, but talk to shamus and john about it. Find the all the constants you need (max displacement etc. )
while(1):
	sled_load = sled.get_current_load(current_position)
	#rint(MH2.get_requested_power(1, sled_load),MH2.max_available_power(1))
	if(MH2.get_requested_power(1, sled_load) < MH2.max_available_power(1)):
		current_position += MH2.get_distance_from_displacement()
	else:
		break

print(current_position)




