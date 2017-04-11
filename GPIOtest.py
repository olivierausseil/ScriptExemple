#!/usr/bin/python2

import RPi.GPIO as GPIO
import time

ledPin = 27

GPIO.setmode(GPIO.BCM)

GPIO.setup(ledPin, GPIO.OUT)

print("Here we go! Press CTRL+C to exit")
try:
    while 1:
        GPIO.output(ledPin, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(ledPin, GPIO.LOW)
        time.sleep(1)
except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
    GPIO.cleanup() # cleanup all GPIO
