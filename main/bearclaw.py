#! /usr/bin/env python3.3
# Author: bcolb
# Version March 13, 2014
# Written for Python 3.3

''' bearclaw.py: maps user input to wild thumper commands.'''

# We're dependent on the pySerial module, link below
# http://pyserial.sourceforge.net/

# import serial
import wildthumper
import time
import sys, termios, tty

def getChar():
    files = sys.stdin.fileno()
    old = termios.tcgetattr(files)
    try:
        tty.setraw(sys.stdin.fileno())
        chin = sys.stdin.read(1)
    finally:
        termios.tcsetattr(files, termios.TCSADRAIN, old)
    return chin

if __name__=='__main__':
    # w = forward
    wt = wildthumper.WildThumper()
    time.sleep(3)
    going = True
    while(going):
        ch = getChar()
        if ch == 'q':
            going = False
        elif ch == 'w':
            wt.driveForward()
        elif ch == 'a':
            wt.turnLeft()
        elif ch == 's':
            wt.driveBackwards()
        elif ch == 'd':
            wt.turnRight()
        elif ch == 'e':
            wt.fullBrake()
    time.sleep(1)
    wt.fullBrake()
    time.sleep(1)
