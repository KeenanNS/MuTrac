#This is a Simulation of a tractor pull and is the property of the McGill University Trcator Pulling Team. Contact keenan.simpson1999@gmail.com if you wish to use this software.

# Everything is in metric base units so g M s N
import numpy

GRAVITY = 10 # lol

class Tractor:
	def __init__(self, length, mass):
		self.length = length #meters
		self.mass = mass #grams
		self.exampleConstantProperty = 69 # this one is constant and is not taken as an argument
		# etc just add stuff you need

	def get_weight(self):
		return self.mass * GRAVITY