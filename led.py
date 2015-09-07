#!/bin/python

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
range = 10
x = 0
while (x < range):
	x += 1
	GPIO.output(11, True)
	time.sleep(.5)
	GPIO.output(11, False)
	time.sleep(.5)
GPIO.cleanup()
