#!/usr/bin/python2

import logging
import time
from smbus2 import SMBus
bus = SMBus(1)
import RPi.GPIO as GPIO
ledPin = 27
GPIO.setmode(GPIO.BCM)
GPIO.setup(ledPin, GPIO.IN)

logging.basicConfig(level = logging.INFO,
                    format= '%(asctime)s %(message)s',
                    datefmt='%a %d %b %Y %H:%M:%S')
logging.Formatter.converter = time.localtime
logging.info('A message.')
detection = GPIO.input(ledPin)
while (1):
    if detection == detection:
        logging.info('A message.')
        time.sleep(1)
