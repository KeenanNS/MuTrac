# MuTrac
all scripted code

# Setting up your environment

you should just google "python hello world from command line - windows/mac/linux". Otherwise you can follow this guide.

Mac and Linux

open your terminal

Windows

download anaconda terminal, and then use that

run :
$python

If this works, you can start coding. 
Make a folder and create a file called hello_world.py
write the line : print('hello world')
save the file
go back to your terminal and cd into the right folder. (google how to cd in unix)
run:
$python hello_world.py
it should print : hello world

You can use the same methods to run all the other programs.

At the top of the python files, there are lines like " import <some library> ". You will get errors if you try to run one of these without the libraries installed. To install libraries, you need pip. Google "how to install pip on mac/linux/anaconda". Once you have pip, run the program. The error will be something like "could not find module called <some library>". Run the commmand $pip install <some library>. keep trying until you don't get errors anymore. Otherwise, you can look at the top of the file, and pip install all of the libraries that get imported at the top.
  
You should be able to make changes and run the programs now.

# GitHub

If you learned how to use Git from the command line, that's great. Checkout the branch you are assigned, work on it, stage, commit, push and then make a pull request. 

If you did not learn how to use Git, go to the repository page. Click branch, select the branch you were assigned, then "add new file", with your new code. Then google "how to make a pull request" and make one.


# RaspberryPi

As a dev you will write mostly applications for the raspberry pi to run. You can write them in whatever language you want, but python is probably the easiest. C is also a good option, especially if you are interested in doing embedded software, but if you are beginning, then I would avoid this as there are many ways to screw up. The Raspberry pi runs a light linux distribution made specifically for it. If you do not have a pi board you can download an emulator https://azeria-labs.com/emulate-raspberry-pi-with-qemu/. This simulates the functionality of the raspberry pi so you can test code on your desktop or laptop.

The hardware architechture of the board itself is not important to you, but if you want to learn about it you can find ample information about the componants on google. One important addition is the CAN bus processor hat that we have. This allows CAN communication with our other controller, which will still be responsible for all locomotion.

Software architechture: You'll write applications or programs to accomplish specific tasks. Once you become more comfortable with that stuff you can start messing with the lower level code. The lower level code will handle the distribution of hardware resources to the applications. Either the application will do it's own interrupt handling or the main.c script will handle interrupts and call the python scripts from there. Depending on how much speed we need, we will make these decisions later.

The main script will live in some directory and be called using systemd at boot time. Either it will run once and start up all applications to run in parrrallel, or it will live forever and handle calls to other applications. It will likely be a combination of the two.

