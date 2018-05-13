# Raspsaber basic algorithm
# Based on: strandtest.py by Tony DiCola (tony@tonydicola.com)
#
# Attempt: Mathlpaca
# Using the rpi_ws281x library 
#
# Disclamer: If it's ugly and rough, well, that must be my part...


import time

from neopixel import *

import argparse
import signal
import sys
from array import *
import adxl345

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

GPIO.setup(17,GPIO.IN)

def signal_handler(signal, frame):
        colorWipe(strip, Color(0,0,0))
        sys.exit(0)

def opt_parse():
        parser = argparse.ArgumentParser()
        parser.add_argument('-c', action='store_true', help='clear the display on exit')
        args = parser.parse_args()
        if args.c:
                signal.signal(signal.SIGINT, signal_handler)


# LED strip configuration:
LED_COUNT      = 60      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 100     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53
LED_STRIP      = ws.WS2811_STRIP_RGB   # Strip type and colour ordering


#create ADXL345 object 
accel = adxl345.ADXL345()
#get axes as g 
#axes = accel.getAxes(True) 

# Define functions which animate LEDs in various ways.
def colorWipe(strip, color, wait_ms=45):
	"""Wipe color across display a pixel at a time."""
	for i in range(strip.numPixels()):
		strip.setPixelColor(i, color)
		strip.show()
		time.sleep(wait_ms/1000.0)

def rainbow(strip, wait_ms=40, iterations=1):
	"""Draw rainbow that fades across all pixels at once."""
	for j in range(256*iterations):
		for i in range(strip.numPixels()):
			strip.setPixelColor(i, wheel((i+j) & 255))
		strip.show()
		time.sleep(wait_ms/1000.0)

def flash(strip, color, wait_ms=50, iterations=30):
	"""Flashes all LEDs for a short period of time"""
	for j in range(iterations):
		for q in range(2):
			for i in range(0, strip.numPixels(), 2):
				strip.setPixelColor(i+q, color)
			strip.show()
			time.sleep(wait_ms/1000.0)
                        for i in range(0, strip.numPixels(), 2):
                                strip.setPixelColor(i+q, 0)

def colorChange(strip, color):
        """Wipe color across display a pixel at a time."""
        for i in range(strip.numPixels()):
                strip.setPixelColor(i, color)
        strip.show()
                
	
def colorOff(strip, color, wait_ms=45):
        """Wipe color across display a pixel at a time."""
  	i=strip.numPixels()
        while i >= 0:
                strip.setPixelColor(i, 0)
                strip.show()
                time.sleep(wait_ms/1000.0)
		i = i-1

def accelTest(level=2):
	axes = accel.getAxes(True)
        x = axes['x'] 
        y = axes['y'] 
        z = axes['z']
        if x > level or y > level or z > level:
		print x
		return True
	return False       

G=[255, 0, 0, 255, 255, 0, 50] 
R=[0, 255, 0, 0, 255, 255, 150] 
B=[0, 0, 255, 255, 0, 255, 100] 

#listColor
#CurrentColor

wait_ms = 45

 


# Main program logic follows:
if __name__ == '__main__':
        # Process arguments
        opt_parse()

	# Create NeoPixel object with appropriate configuration.
	strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
	# Intialize the library (must be called once before other functions).
	strip.begin()

	#initialise a previous input variable to 0 (assume button not pressed last)
	#initialise variable icolor to select color
        icolor = 0
	input = 1
	impact = 0

	while True:
  		#take a reading
  		input = GPIO.input(17)
		
		if accelTest:
                        flash(strip, Color(200, 200, 200))                 

  		#if the last reading was low and this one high, print
  		if (not input):
    			print("Button pressed")
			icolor = 1
  			#update previous input
  			prev_input = input
  			#slight pause to debounce
  			time.sleep(0.5)
 			
			
			#strip.setPixelColor(0,Color(255,0,0))
			#strip.show()
 			#strip.setPixelColor(1,Color(255,0,0))
			#strip.show()
			 
			if icolor == 1: 
				colorWipe(strip, Color(R[0], G[0], B[0]))
				icolor = icolor +  1
             	
			if icolor == 2:
				time.sleep(wait_ms/1000.0)
				colorChange(strip, Color(R[5], G[5], B[5]))
				icolor = icolor + 1
			
			if icolor == 3:
				time.sleep(wait_ms/1000.0)
				colorOff(strip, Color(0, 0, 0))
				icolor = icolor + 1
			if icolor > 3:
				icolor = 1
