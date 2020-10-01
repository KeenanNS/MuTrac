import pandas as pd 
import matplotlib.pyplot as plt
data = pd.read_csv("full_displacement.csv",sep=';') 
# Preview the first 5 lines of the loaded data 
data = data.iloc[110:460]

data['pressure'] = ( data['0,2 - CP_pressureB'] - data['0,2 - CP_pressureA'] ) * 8571
data['rpms'] = data['0,2 - CP_rpms'] / 10
data['flow'] = data['rpms'] * 0.000326 / 60
data['power'] = data['flow'] * data['pressure']
data['horse power'] = data['power'] / 746
plt.scatter(data['rpms'], data['horse power'])
plt.show()
plt.savefig('motor_rpm_vs_HP.png')


