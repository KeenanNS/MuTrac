import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

x = [4.3, 6.9, 9.5, 12.1, 14.7, 17.4, 20.0, 22.8, 25.4, 27.9]
y = [43, 60, 69, 75, 79, 81, 82, 83, 84, 85]

def func (x, a, b, c, d):	
	return (a * np.power(x, b) + c * x) 
pars, cov = curve_fit(f=func, xdata=x, ydata=y)

def func2 (x, a, b):	
	return a * (np.log(x) / np.log(b)) 
pars2, cov2 = curve_fit(f=func2, xdata=x, ydata=y)


print(pars)
#print(pars2)
Y = []
X_ = []
W = []
G = []

for Z in range(0, 30):
	W.append(Z)
	

for X in range(0, 30):
	X_.append(X)
	#G.append(func2(Z, pars[0], pars[1]))
	Y.append(func(X, pars[0], pars[1], pars[2], pars[3]))

plt.plot(x,y)
#plt.plot(X_, G)
plt.xlabel('displacement in cc')
plt.ylabel('efficiency in %')
plt.plot(X_,Y)
plt.show()