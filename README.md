Bearclaw
========

A wheeled robotics project.

## Description

Bearclaw is a small robot being developed from widely available electronics. The project is still in early developmental stages. Some of the componenets being used or considered for use include:
1. Raspberry Pi
2. Raspberry Pi Camera Module
3. Arduino
4. Wild Thumper Chassis and Micrcontroller
5. TRex Microcontroller

The bulk of the programming is being done in Python and housed in the Raspberry Pi. Associated Arduino based micocontrollers are accessed via serial with their programming done in either Arduino's native language or avr-c.

## Dependencies
The main python library used by the Raspberry Pi relies on the [PySerial module](http://pyserial.sourceforge.net/) to communicated with additional microcontrollers.

## Development
As of March 11, 2014 Bearclaw is actively being developed on. The project is still in its early stages. While the code contained herein is functional it is still very much under development.