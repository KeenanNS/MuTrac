import pandas as pd 
import matplotlib.pyplot as plt
data = pd.read_csv("goodgood.csv",sep=';') 
# Preview the first 5 lines of the loaded data 
data = data.iloc[200:775]

data['pressure'] = data['0,2 - CP_pressure']
data['rpms'] = data['0,2 - CP_rpms'] 
data['pwm'] = data['0,2 - CP_output_pwm']
data
#plt.scatter(data['rpms'], data['pressure'])
plt.scatter(data['pressure'], data['pwm'])
plt.show()
plt.savefig('motor_rpm_vs_HP.png')


