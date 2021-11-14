import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

x = [4.3, 6.9, 9.5, 12.1, 14.7, 17.4, 20.0, 22.8, 25.4, 27.9]
x = [(296.6*num + 1724.62) for num in x]
y = [.43, .60, .69, .75, .79, .81, .82, .83, .84, .85]
# y = [(num * 14019) for num in y]
y = [(num * 18.8) for num in y]

x = [1800, 2000, 2200, 2400, 2600, 2800, 3000, 3200, 3400, 3600]
y = [21, 23.7, 25, 26.8, 28, 29, 30, 30.5, 31, 31]
y = [num / 31 for num in y]
def func (x, a, b, c, d):	
	# return (a * np.power(x, b) + c * x) 
	# return a * np.sqrt(b * (x+c)) + d
	return a + b/(x) + c* np.log(x)
pars, cov = curve_fit(f=func, xdata=x, ydata=y)

print(pars)
#print(pars2)
Y = []
X_ = []
W = []
G = []
	
for X in range(1800, 3600):
	X_.append(X)
	#G.append(func2(Z, pars[0], pars[1]))
	Y.append(func(X, pars[0], pars[1], pars[2], pars[3]))


print(func(3028, pars[0], pars[1], pars[2], pars[3]))
print(pars[0], pars[1], pars[2], pars[3])
# x = [1800, 3600]
# y = [21,23]
plt.plot(x,y)
#plt.plot(X_, G)
plt.xlabel('displacement in cc')
plt.ylabel('power in watts')
plt.plot(X_,Y)
plt.show()