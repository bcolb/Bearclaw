#! /usr/bin/env python3.3
# Author: bcolb
# Version March 12, 2014
# Written for Python 3.3

''' WildThumper.py: Creates an API for the Wild Thumper Controller\n
    board based off of the Atmega 128P. Options include reading\n
    analog input, controlling servos, and controlling the H-bridge.\n
    Note that a slight delay after initializing of a Wild Thumper]n
    Object may be needed in order to ensure correct serial communications. '''

# We're dependent on the pySerial module, link below
# http://pyserial.sourceforge.net/

import serial
import time

class WildThumper:
    ''' WildThumper Class: corresponds to physical actions via the\n
        Wild Thumper controller and associated chassis. '''
    def __init__(self, location='/dev/ttyUSB0', baud=115200):
        ''' Initializes our WildThumper with a serial connection via\n
            parameters location (a string) and baud (an integer) '''
        self.ser = serial.Serial(location, baud)
        self.Leftmode = 1
        self.LeftPWM = 0
        self.Rigthmode = 1
        self.RightPWM = 0
        self.speed = 100
    def __fl__(self):
        ''' A private method that can be called to flush the serial\n
            buffer on the arduino remotely. '''
        self.ser.write(bytearray('FL', 'ascii'))
    def __an__(self):
        ''' A private method that reads and returns analog input.\n
            Implementation of analog input has been deferred.'''
        pass
    def __sv__(self):
        ''' A private method that allows for control of the server\n
            outputs on the Wild Thumper controller. Implementation\n
            has been deferred. '''
        pass
    def __hb__(self, Leftmode, LeftPWM, Rightmode, RightPWM):
        ''' A private method that allows for control of the H-Bridge\n
            via several parameters. '''
        self.ser.write(bytearray('HB', 'ascii'))
        command = bytearray()
        command.append(Leftmode)
        command.append(LeftPWM)
        command.append(Rightmode)
        command.append(RightPWM)
        self.ser.write(command)
    def flush(self):
        ''' Flushes the serial buffer on the Wild Thumper Board '''
        self.__fl__()
    def drive(self, **values):
        ''' Transmits the following values, Leftmode, LeftPWM, Rightmode\n
            and RightPWM, to the Wild Thumper Controller to move the\n
            chassis accordingly. Acceptable values are 0-reverse, 1-brake,\n
            2-forward for mode, and an int 0-256 for PWM. '''
        params = [0,0,0,0]
        if("Leftmode" in values):
            n = values["Leftmode"]
            if(n >= 0 and n <= 2):
                params[0] = n
                self.Leftmode = n
            else:
                params[0] = self.Leftmode 
        if("LeftPWM" in values):
            n = values["LeftPWM"]
            if(n >= 0 and n < 256):
                params[1] = n
                self.LeftPWM
            else:
                params[1] = self.LeftPWM
        if("Rightmode" in values):
            n = values["Rightmode"]
            if(n >= 0 and n <= 2):
                params[2] = n
                self.Rightmode = n
            else:
                params[2] = self.Rightmode
        if("RightPWM" in values):
            n = values["RightPWM"]
            if(n >= 0 and n < 256):
                params[3] = n
                self.RightPWM = n
            else:
                params[3] = self.RightPWM
        self.__hb__(params[0], params[1], params[2], params[3])
    def getSpeed(self):
        return self.speed
    def setSpeed(self, speed):
        self.speed = speed
    def driveForward(self):
        ''' Calls the drive method to drive forward at half speed '''
        self.drive(Leftmode=2, LeftPWM=self.speed, Rightmode=2, RightPWM=self.speed)
    def driveBackwards(self):
        ''' Calls the drive method to put both sides in reverse at\n
            half speed '''
        self.drive(Leftmode=0, LeftPWM=self.speed, Rightmode=0, RightPWM=self.speed)
    def turnLeft(self):
        ''' Calls the drive method to put the right side in forward\n
            and the left side in reverse, both at half speed. '''
        self.drive(Leftmode=2, LeftPWM=self.speed, Rightmode=0, RightPWM=self.speed)
    def turnRight(self):
        ''' Calls the drive method to put the left side in forward\n
            and the right side in reverse, both at half speed. '''
        self.drive(Leftmode=0, LeftPWM=self.speed, Rightmode=2, RightPWM=self.speed)
    def fullBrake(self):
        ''' Calls the drive method to put both sides in brake.'''
        self.drive(Leftmode=1, LeftPWM=0, Rightmode=1, RightPWM=0)

if __name__=='__main__':
    # Just a little test drive
    print("Creating Wild Thumper")
    wt = WildThumper()
    # A delay is necessary after the creation of a new Wild Thumper
    # object for serial commands to execute correctly
    print("Delaying a few seconds...")
    time.sleep(3)
    print("Driving forward")
    wt.driveForward()
    time.sleep(1)
    print("Braking...")
    wt.fullBrake()
    time.sleep(1)
    print("Driving backwards")
    wt.driveBackwards()
    time.sleep(1)
    print("Braking...")
    wt.fullBrake()
    time.sleep(1)
    print("Turning left")
    wt.turnLeft()
    time.sleep(1)
    print("Braking...")
    wt.fullBrake()
    time.sleep(1)
    print("Turning right")
    wt.turnRight()
    time.sleep(1)
    print("Braking")
    wt.fullBrake()
    print("Done")
