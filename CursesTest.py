#!/usr/bin/python2

import curses
import time
import RPi.GPIO as GPIO



ledPin = 27

GPIO.setmode(GPIO.BCM)

GPIO.setup(27, GPIO.OUT)
#high = GPIO.output(ledPin, GPIO.HIGH)
#low = GPIO.output(ledPin, GPIO.LOW)

x = 0

#def execute_cmd(cmd_string):

#     a = system(cmd_string)
#     print ""
#     if a == 0:
#          print "Command executed correctly"
#     else:
#          print "Command terminated with error"
#     raw_input("Press enter")
#     print ""
screen = curses.initscr()
while x != ord('3'):
     #screen = curses.initscr()

     screen.clear()
     screen.border(1)
     screen.addstr(2, 2, "Please enter a number...")
     screen.addstr(4, 4, "1 - Switch on the LED")
     screen.addstr(5, 4, "2 - Switch of the LED")
     screen.addstr(9, 8, "3 - Exit")
     screen.refresh()

     x = screen.getch()

     if x == ord('1'):

          curses.endwin()
          GPIO.output(ledPin, GPIO.HIGH)
          #time.sleep(1)


     if x == ord('2'):
          curses.endwin()
          GPIO.output(ledPin, GPIO.LOW)


curses.endwin() # quit the graphic interface
GPIO.cleanup() # the GPIO come back to origin
