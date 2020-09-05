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

	def Net_Force(self, Load, Pressure):
		#TODO calculate overall reduction
		reduction = 0.69
		pull = Pressure * reduction 

		if net_force <= 0:
			done = True

		if not done:
			return pull - Load
		else: 
			sys.exit("it is complete")

	def Velocity(self, net_force, prev_net_force, prev_velocity):
		velocity = (prev_velocity * prev_net_force) / net_force #conservation of momentum
		velocities[time] = velocity
		return velocity

	def Load(self, Distance):
		return Distance * 10 # TODO rate of change in load / unit of measurement (meters)

	def Pressure(self, Net_Force):
		pressure = Net_Force / 0.69 #TODO this is the inverse of the reduction 
		return random.triangular(pressure - VARIATION, pressure + VARIATION, pressure) # (min, max, mode) prob distribution

	def Displacement(self, Pressure):
		pid = PID(self.P, self.I, self.D)
		control = pid(Pressure)
		displacement = controlled_system.update(control)
		return displacement #this needs to get converted to new pressure



#pull = Pull(#TODO implement command line args)

print("still needs implementing")
print(P, I, D)

pull = Pull(P,I,D)

time = 0
prev_velocity = 0
distance = 0
prev_net_force = 0
net_force = 5000 #max pressure * loss and reduction (max force)
done = False
velocities = []
while not done:
	time +=1
	velocity = pull.Velocity(net_force, prev_net_force, prev_velocity)
	distance = pull.Distance(velocities, time)
	print(distance)
	if time >= 100:
		break

print("distance travelled is %d", distance)










