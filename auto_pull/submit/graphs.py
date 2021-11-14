import pandas as pd 
import matplotlib.pyplot as plt
data = pd.read_csv("for_demo.csv",sep=';') 
# Preview the first 5 lines of the loaded data 
#data = data.iloc[200:775]

data['pressure'] = data['0,2 - CP_pressure']
data['rpms'] = data['0,2 - CP_rpms'] 
data['pwm'] = data['0,2 - CP_output_pwm']
data
#plt.scatter(data['rpms'], data['pressure'])
plt.scatter(data['pressure'], data['pwm'])
plt.scatter(data['pressure'], data['rpms'])
plt.xlabel('Pressure in Pascals')
plt.ylabel('PWM output signal (blue) -- RPM (orange)')
plt.title('PWM vs Pressure -- AutoPull Test')
plt.show()
plt.savefig('PWM_vs_Pressure.png')


