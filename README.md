Bearclaw
========

A robotics project aimed at creating an easy to assemble and modify wheeled off road platform. The platform will be easily expanded and will support multiple sensor types once complete.

## Description

Bearclaw is a small robot being developed from widely available electronics. The project is still in its early developmental stages. Some of the componenets being used or considered for use include:
 1. [Raspberry Pi](http://www.raspberrypi.org/) (the brains)
 2. [Raspberry Pi Camera Module](http://www.raspberrypi.org/camera) (the eyes)
 3. [Arduino](http://www.arduino.cc/) (Various Boards)
 4. [Wild Thumper Chassis](http://www.dagurobot.com/goods.php?id=47) and [Microcontroller](https://www.sparkfun.com/products/retired/11057)
 5. [TRex Microcontroller](http://www.dagurobot.com/goods.php?id=135)

The bulk of the programming is being done in Python and run from the Raspberry Pi. Associated Arduino based micocontrollers are accessed via serial with their programming done in Arduino or avr-c. 

## Dependencies
The main python library used by the Raspberry Pi relies on the [PySerial module](http://pyserial.sourceforge.net/) to communicate with additional microcontrollers.

## Development
As of March 11, 2014 Bearclaw is actively being developed on. The project is still in its early stages. While the code contained herein is functional it is still very much under development.