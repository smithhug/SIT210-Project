# SIT210-Project

The program consists of two major files:
  - Project.ino
  - pi.py

Project.ino is the project file that needs to be flashed to the Particle Argon device in order to allow it to operate. Once opened on the Particle Web IDE, press the flash button to flash it to a paired device.

pi.py is a program that needs to be run on a Raspberry Pi that has a stable internet connection and a connected USB Webcam. If it is run within a terminal window the program will loop until the window is closed. This will mean it will constantly ping the thingspeak database unless interrupted by a severed internet connection, severed power supply or if the terminal is closed.

In order to ping a mobile device a service must be setup with IFTTT in order to read when "isopen" is published at 1 by the Argon device. The next function from there is to send a notification to the IFTTT app on receiving this response.


It is impoerant to note that this program was built with the intention of working with the systems they were develiped on. If you intend on using a different thingspeak service you may want to replace the API queries on both the major files. 
