#!/usr/bin/python2

import logging

# sources
#http://deusyss.developpez.com/tutoriels/Python/Logger/
#http://sametmax.com/ecrire-des-logs-en-python/

# Desire format
formatter = logging.Formatter("%(asctime)s -- %(name)s -- %(levelname)s -- %(message)s")
#creation of handler who permit to separate the different log level
handler_critic = logging.FileHandler("critic.log", mode="a", encoding="utf-8")
handler_info = logging.FileHandler("info.log", mode="a", encoding="utf-8")
#set the format of message to handler
handler_critic.setFormatter(formatter)
handler_info.setFormatter(formatter)
#set level to handler
handler_info.setLevel(logging.INFO)
handler_critic.setLevel(logging.CRITICAL)
# We create an object with logger type, we assigns a minimum level (logging.INFO) and use with the handler created
logger = logging.getLogger()
logger.setLevel(logging.INFO) # ***
logger.addHandler(handler_critic)
logger.addHandler(handler_info)
#Permit to transmit log message
logger.debug('Debug error') # minimum level is INFO(see ***), so the debug log don't appear (see level of logging)
logger.info('INFO ERROR')
logger.critical('INFO ERROR2')

# creation of handler to display on terminal
steam_handler = logging.StreamHandler()
steam_handler.setLevel(logging.DEBUG)
logger.addHandler(steam_handler)

#!/usr/bin/python2
# ----------------- Initialization --------------------
#library import
import time
import sys
import argparse
import RPi.GPIO as GPIO

timeDetection = 0
endTimeDetection = 0
detection = 0
flagTime = 0
loopInfinite = True
maxbyte = 65535 #maximum value to 2 bytes

#GPIO initialization
ledPin = 27
GPIO.setmode(GPIO.BCM)
GPIO.setup(ledPin, GPIO.IN)

#Initilization of I2C bus
from smbus2 import SMBus
bus = SMBus(1)

#test on a bit who is interesting -> Method
def testBit(int_type, offset):
   mask = 1 << offset
   return(int_type & mask)

# -------------- End of initialization ----------------

# -----  parser ----- do arguments when we launch the script
parser = argparse.ArgumentParser()
parser.add_argument('-sT', action='store', dest='sensitivityTrigger')
parser.add_argument('-sG', action='store', dest='sensitivityGain')
parser.add_argument('-t', action='store', dest='triggerTime')

results = parser.parse_args()

#------- Sensitivity --------
# in case argument has not been provided
if None == results.sensitivityGain:
    sensitivityGain = int(16)
else:
    sensitivityGain = int(results.sensitivityGain)

# manage argument limits (0-31) because 5 bits allow (see datasheet_HT7Mx6 __ p12 _ 1. Sensor Config Register)
if sensitivityGain < 0:
    sensitivityGain = 0

if sensitivityGain > 31:
    sensitivityGain = 31

# from there, sensitivity takes a value between 0 and 31 in all cases
print ("sensitivity Gain is: " + str(sensitivityGain) )
logger.info('sensitivity Gain is: %d ' %sensitivityGain)


if None == results.sensitivityTrigger:
    sensitivityTrigger = int(0)
else:
    sensitivityTrigger = int(results.sensitivityTrigger)

# manage argument limits (0-7) because 3 bits allow (see datasheet_HT7Mx6 __ p12 _ 1. Sensor Config Register)
if sensitivityTrigger < 0:
    sensitivityTrigger = 0

if sensitivityTrigger > 7:
    sensitivityTrigger = 7

logger.info(sensitivityTrigger)
# from there, sensitivity takes a value between 0 and 7 in all cases
print ("sensitivity Trigger is: " + str(sensitivityTrigger) )

# sum of the two sensitivity
sensitivity = (sensitivityTrigger << 5) +  sensitivityGain

if sensitivityTrigger == 0 :
    sensitivity = sensitivityGain
if sensitivityGain == 0 :
    sensitivity = sensitivityTrigger
print sensitivity

logger.critical('sensitivity Gainnnnnnnnnnnnnn is: %d ' %sensitivity)


#-------------- end sensitivity ---------

#---------------TriggerTime -------------
if None == results.triggerTime:
    triggerTime = int(50)
else:
    triggerTime = int(results.triggerTime)

if triggerTime < 0:
    triggerTime = 0

if triggerTime > maxbyte:
    triggerTime = maxbyte

# cut in two the data
triggerTimeMSB = triggerTime >> 8 # MSB
triggerTimeLSB = triggerTime & 0xFF # LSB

#triggerTime = int(triggerTime) * 10
#----------------end TriggerTIme --------
# -------------- end parser  ------------
