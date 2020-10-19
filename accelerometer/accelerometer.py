import time
import board
import busio
import adafruit_adxl34x

i2c = busio.I2C(board.SCL, board.SDA)
accelerometer = adafruit_adxl34x.ADXL345(i2c)
for j in range (0,30):
	for i in range(0,150):
		print("%d,"%j,"%f,%f,%f,"%accelerometer.acceleration)
		#time.sleep(0.1)

