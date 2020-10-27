
//wire colours correspond to load cell not soldered
//with robotshop facing you, on the back quad, from left to right
//black, white, green, red
#include <SD.h>
#include <WheatstoneBridge.h>
#include "shield.h"

// Initial calibration values
const int CST_STRAIN_IN_MIN = 365;       // Raw value calibration lower point
const int CST_STRAIN_IN_MAX = 30;       // Raw value calibration upper point
const int CST_STRAIN_OUT_MIN = 0;        // Weight calibration lower point
const int CST_STRAIN_OUT_MAX = 1000;     // Weight calibration upper point

const int CST_CAL_FORCE_MIN = 0;
const int CST_CAL_FORCE_MAX = 32000;
const int CST_CAL_FORCE_STEP = 50;
const int CST_CAL_FORCE_STEP_LARGE = 500;
float strain_force;
float strain_adc;
//int strain_adc;
//int strain_force;
int force_pos_offset;
float load;
float pounds;
float loads;
int i;
// Initialize the Wheatstone bridge object
WheatstoneBridge wsb(A1, CST_STRAIN_IN_MIN, CST_STRAIN_IN_MAX, CST_STRAIN_OUT_MIN, CST_STRAIN_OUT_MAX);

int loadcell = A1;
int dummy_pin = A2;
int dummy_drop;
void setup()
{
 Serial.begin(9600);
// Force measurement & display
}
// < Main code >
void loop()
{
// Make a force measurement and obtain the calibrated force value
// Obtain the raw ADC value from the last measurement
load = analogRead(loadcell);
dummy_drop = analogRead(dummy_pin);

// calibration primitive equation
load = load - dummy_drop;
pounds = ((369 - load) * 6.7); 

//determined by hanging weights on the cell to make y = mx + b
//Serial.println(strain_force);
delay(100);

//then there was code here to store on an SD module and process more later.
}