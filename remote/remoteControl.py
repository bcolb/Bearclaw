#! /usr/bin/env python3.3
# Author: bcolb
# Version: March 25th, 2014
# Written for Python3.3

''' remoteControl.py: uses an ssh call to remotely access\n
    a Raspberry Pi. '''

class RemotePi:
    ''' RemotePi Class: corresponds to a physical raspberry pi.\n
        All methods of the class are accessed via an SSH call.\n '''
    def __init__(self):
        ''' Initializes our remote pi's connection. '''
        self.name = "Remote Raspberry Pi"
    def start(self):
        ''' performs an SSH into our Raspberry Pi. '''
        pass

if __name__=='__main__':
    # Creates a new remotePi and calls commands
    remoteRasPi = RemotePi()
    remoteRasPi.start()
