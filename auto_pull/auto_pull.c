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
#include<stdlib.h>
/* USER code section begin */

int do_shit(double theta, double pressure, double rpm){//, double tweak, double tweak2){
  double max_power = 61591 - 49681800 / theta - 4866 * log(theta);
  //printf("maxpower1 : %f\n", max_power);
  max_power = max_power * (4.86 - 2184 / rpm - 0.440 * log(rpm));
  //printf("maxpower2 : %f\n", max_power);
  max_power = max_power; // * tweak; 

  int wanted = (int)((max_power * 22222222222) / (pressure * rpm));
  if (wanted < 3000){
  return 3000;
  }
  else if (wanted > 10000){
  return 10000;
  }
  return wanted;
}

int main(int argc, char * argv[]){
  char * dummy;
  double pressure = strtod(argv[1], &dummy);
  double rpm = strtod(argv[2], &dummy);
  double pwm = strtod(argv[3], &dummy);
  //double tweak = strtod(argv[4], &dummy);
 // double tweak2 = strtod(argv[5], &dummy);
  int ret = do_shit(pressure, rpm, pwm);//, tweak, tweak2); 
  printf("%d\n", ret);

}

/* USER code section end */
//0.432