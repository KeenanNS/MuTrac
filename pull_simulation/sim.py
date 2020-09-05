#Simulation of autopull
#http://users.iems.northwestern.edu/~nelsonb/IEMS435/PythonSim.pdf

import SimPy.Simulation as sim
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
P = sys.argv[0]
I = sys.argv[1]
D = sys.argv[2]

WEIGHT = 1000 * 4.44822#TODO weight of tractor
VARIATION = 5 #TODO this is the amount that we thing the pressure will vary, (how much it could jump / time step)

class Pull:
	def __init__(self, P, I, D):
		self.P = P
		self.I = I
		self.D = D
		self.velocities = []
		self.start_clock = count_time()

	def count_time:
		while not:
			i+=1
		else: sys.exit("You lost, if your pressure dropped and then it stopped you slid out")

	def Distance(velocities, time):
		avg_velocity = sum(velocities)/len(velocities)
		return avg_velocity * time

	def Net_Force(Load, Pressure):
		#TODO calculate overall reduction
		reduction = 0.69
		pull = Pressure * reduction 

		if not done:
			return pull - Load
		else: 
			sys.exit("it is complete")

	def Velocity(net_force, prev_net_force, prev_velocity):
		velocity = (prev_velocity * prev_net_force) / net_force #conservation of momentum
		self.velocities[time] = velocity
		return velocity

	def Load(Distance):
		return Distance * 10 # TODO rate of change in load / unit of measurement (meters)

	def Pressure(Net_Force):
		pressure = Net_Force / 0.69 #TODO this is the inverse of the reduction 
		return random.triangular(pressure - VARIATION, pressure + VARIATION, pressure) # (min, max, mode) prob distribution

	def Displacement(Pressure):
		return PID(self.P, self.I, self.D)

pull = Pull(#TODO implement command line args)



