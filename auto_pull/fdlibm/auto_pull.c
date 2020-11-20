/*
FileName: auto_pull.c
Date: 2020-Nov-16
Time: 2:03:37 AM
GUIDE version: 12.1.7.1470
*/

//#include "auto_pull.h"
//#include "fdlibm.h"
#include</home/keenan/code/MuTrac/auto_pull/fdlibm/fdlibm.h>
#include<stdio.h>
/* USER code section begin */

// int do_shit(double theta, double pressure, double rpm){
//   double max_power = 61591 - 49681800 / theta - 4866 * log(theta);
//   max_power = max_power * (4.86 - 2184 / rpm - 0.396 * log(rpm));
  
//   int wanted = (int)((max_power * 22222222222) / (pressure * rpm));
//   if (wanted < 3000){
//   return 3000;
//   }
//   else if (wanted > 10000){
//   return 10000;
//   }
//   return wanted;
// }

int main(void){
 //double theta[10] = {10000, 9000, 8000, 7000, 6000, 5000, 4000, 3000, 2000, 1000};
 int i;
 double rpm;
 for (i = 0; i<10;i++){
 rpm = 2000 + i * 115;
  printf("%f, %f\n",rpm, 4.86 - 2184 / rpm - 0.396 * log(rpm));
 }
}

/* USER code section end */



# ret = scipy.interpolate.griddata((data2['latitude'],data2['longitude']),\
#   data2['2in'],\
#   [coord for coord in zip(data1['latitude'],\
#     data1['longitude'])])

# records = data1['2in', '4in', '6in'].to_records(index = False)
# def func (X, a, b, c):  
#   return (a * X[0] + b * X[1] + c * X[2]) / sum(X)
# pars, cov = curve_fit(f=func, xdata=x, ydata=y)
# print(ret)