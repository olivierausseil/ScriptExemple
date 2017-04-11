#!/usr/bin/python2

import RPi.GPIO as GPIO
import time

ledPin = 27

GPIO.setmode(GPIO.BCM)

GPIO.setup(ledPin, GPIO.IN)

while(1):
    time.sleep(1)
    if GPIO.input(ledPin):
        print 'detection'
    else:
        print 'no detection'

GPIO.cleanup() # cleanup all GPIO
