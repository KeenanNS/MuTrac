#include <stdio.h>
#include <wiringPiI2C.h>
#include <stdint.h>
#include <time.h> 

#define DEVICE_ID 0x53
#define REG_POWER_CTL   0x2D
#define REG_DATA_X_LOW  0x32
#define REG_DATA_X_HIGH 0x33
#define REG_DATA_Y_LOW  0x34
#define REG_DATA_Y_HIGH 0x35
#define REG_DATA_Z_LOW  0x36
#define REG_DATA_Z_HIGH 0x37

int main (int argc, char **argv)
{
int i;
    // Setup I2C communication
    int fd = wiringPiI2CSetup(DEVICE_ID);
    if (fd == -1) {
        printf("you fucked up");
        return -1;
    }
    printf("setup of i2c successful");
    // Switch device to measurement mode
    wiringPiI2CWriteReg8(fd, REG_POWER_CTL, 0b00001000);
    while (1) {
        int dataX = wiringPiI2CReadReg16(fd, REG_DATA_X_LOW);
        dataX = ((uint16_t)dataX) /25;
        int dataY = wiringPiI2CReadReg16(fd, REG_DATA_Y_LOW);
        dataY = ((uint16_t)dataY) /25;
        int dataZ = wiringPiI2CReadReg16(fd, REG_DATA_Z_LOW);
        dataZ = ((uint16_t)dataZ) /25;
        printf("X: %d  --  Y: %d  --  Z: %d\n", dataX, dataY, dataZ);
i = 0;	
while(i++ < 50);
    }
    return 0;
}
