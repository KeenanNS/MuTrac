# MuTrac
all scripted code

# RaspberryPi

As a dev you will write mostly applications for the raspberry pi to run. You can write them in whatever language you want, but python is probably the easiest. C is also a good option, especially if you are interested in doing embedded software, but if you are beginning, then I would avoid this as there are many ways to screw up. The Raspberry pi runs a light linux distribution made specifically for it. If you do not have a pi board you can download an emulator https://azeria-labs.com/emulate-raspberry-pi-with-qemu/. This simulates the functionality of the raspberry pi so you can test code on your desktop or laptop.

The hardware architechture of the board itself is not important to you, but if you want to learn about it you can find ample information about the componants on google. One important addition is the CAN bus processor hat that we have. This allows CAN communication with our other controller, which will still be responsible for all locomotion.

Software architechture: You'll write applications or programs to accomplish specific tasks. Once you become more comfortable with that stuff you can start messing with the lower level code. The lower level code will handle the distribution of hardware resources to the applications. Either the application will do it's own interrupt handling or the main.c script will handle interrupts and call the python scripts from there. Depending on how much speed we need, we will make these decisions later.

The main script will live in some directory and be called using systemd at boot time. Either it will run once and start up all applications to run in parrrallel, or it will live forever and handle calls to other applications. It will likely be a combination of the two.

