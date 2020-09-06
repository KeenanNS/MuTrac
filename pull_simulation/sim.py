#Simulation of autopull

import random
import sys
from simple_pid import PID

print('MH3 Autopull PID learning simulation')

#this should output a distance travelled. I think it will be easier if we try to out put velocity/

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

WEIGHT = 1000 * 4.44822#TODO weight of tractor
VARIATION = 5 #TODO this is the amount that we thing the pressure will vary, (how much it could jump / time step)
MAX_PRESSURE = 4000 #psi or some other value

class Pull:
	def __init__(self, P, I, D):
		self.P = P
		self.I = I
		self.D = D

	def Distance(self, velocities, time):
		avg_velocity = sum(velocities)/len(velocities)
		return avg_velocity * time

	def Net_Force(self, Load, Pressure_in, done):
		#TODO calculate overall reduction
		reduction = 0.69
		pull = Pressure_in * reduction 

		if pull <= 0:
			done = True

		if not done:
			return pull - Load
		else: 
			sys.exit("it is complete")

	def Velocity(self, net_force, prev_net_force, prev_velocity, time):
		velocity = (prev_velocity * prev_net_force) / net_force #conservation of momentum
		print("velocity: " ,velocity)
		velocities.append(velocity)
		return velocity

	def Load(self, Distance):
		return (Distance * 10) + 1000 # TODO rate of change in load / unit of measurement (meters). 1000 represents inertia of sled on wheels

	def Measured_Pressure(self, Net_Force):
		pressure = Net_Force / 0.69 #TODO this is the inverse of the reduction 
		return random.triangular(pressure - VARIATION, pressure + VARIATION, pressure) # (min, max, mode) prob distribution

	def Presure_in(self, Pressure): #controlled by displacement, equivalent of applied force
		pid = PID(self.P, self.I, self.D)
		control = pid(Pressure)
		#v = controlled_system.update(0)
		#displacement = controlled_system.update(control)
		return control #this needs to get converted to new pressure



#pull = Pull(#TODO implement command line args)

print("still needs implementing")
print(P, I, D)

pull = Pull(P,I,D)

time = 0
prev_velocity = 1
distance = 0
prev_net_force = 1
done = False
pressure_in = 4000
Measured_Pressure = 3000
velocities = []
while not done:
	load = pull.Load(distance)
	print(load)
	pressure_in = pull.Presure_in(Measured_Pressure)
	print(pressure_in)
	net_force = pull.Net_Force(pressure_in, load, done)
	print(net_force)

	velocity = pull.Velocity(net_force, prev_net_force, prev_velocity, time)
	distance = pull.Distance(velocities, time)
	Measured_Pressure = pull.Measured_Pressure(net_force)
	print(distance)
	time +=1
	if time >= 100:
		break

print("distance travelled is ", distance)










