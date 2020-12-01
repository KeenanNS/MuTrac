import pandas as pd 
import os
import subprocess
import matplotlib.pyplot as plt
import scipy
data = pd.read_csv("goodgood.csv",sep=';') 
# Preview the first 5 lines of the loaded data 
data = data.iloc[200:775]
del data['Info']
del data['Date']
del data['Time']
del data['TimeStamp']
data['pressure'] = data['0,2 - CP_pressure']
data['rpms'] = data['0,2 - CP_rpms'] 
data['pwm'] = data['0,2 - CP_output_pwm']
del data['0,2 - CP_pressure']
del data['0,2 - CP_rpms'] 
del data['0,2 - CP_output_pwm']
del data['0,2 - CP_last_pwm']


def episode():#tweak, tweak2):
	x = 10000
	arr = []
	press = []
	for i,row in data.iterrows():
		pressure = int(row['pressure'])
		rpm = int(row['rpms'])

		command1 = str(row['pressure'])# + ' ' + str(row['rpms']) #{}'.format(row['pressure'], row['rpms'])
		command2 = str(row['rpms'])
		command3 = str(x)
		command = './pull {} {} {}'.format(command3, command1, command2)#, tweak, tweak2)
		command = command.split()
		#print(command)
		#os.system('./pull {} {} {}'.format(command3, command1, command2))
		x = subprocess.check_output(command, stderr=subprocess.STDOUT).decode('utf-8')
		#print(x.decode("utf-8"))
		arr.append(int(x))
		press.append(pressure)
		#powers.append(pressure * rpm/60 * x / 10000 * 0.0003/11.7)
		#return sum(powers)/len(powers)
		# TODO extract average power and return it. ( you have pressure, pwm and rpm)
	return press, arr



def func (X, tweak, tweak2):
	power = episode(tweak, tweak2)
	return 1 / power

#pars  = scipy.optimize.minimize(func, [1,1])
press, arr = episode()
plt.scatter(press, arr)
plt.xlabel('Pressure in Pa')
plt.ylabel('PWM (0:10000, mapped to 12V)')
plt.show()