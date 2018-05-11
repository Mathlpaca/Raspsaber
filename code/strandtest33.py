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
LED_COUNT      = 24      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 150     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53
LED_STRIP      = ws.WS2811_STRIP_GRB   # Strip type and colour ordering


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

def flash(strip, color, wait_ms=50, iterations=10):
	"""Flashes all LEDs for a short period of time"""
	for j in range(iterations):
		for q in range(3):
			for i in range(0, strip.numPixels(), 3):
				strip.setPixelColor(i+q, color)
			strip.show()
			time.sleep(wait_ms/1000.0)
                       # for i in range(0, strip.numPixels(), 3):
                               # strip.setPixelColor(i+q, 0)

list1=[255, 0, 0] #Red
list2=[0, 255, 0] #Green
list3=[0, 0, 255] #Blue

array_color = array('i', [list1[0:3], list2[0:3], list3[0:3]])




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
        icolor=1
	input=1
	while True:
  		#take a reading
  		input = GPIO.input(17)
  		#if the last reading was low and this one high, print
  		if (not input):
    			print("Button pressed")
  			#update previous input
  			prev_input = input
  			#slight pause to debounce
  			time.sleep(0.05)
	
		
			

			print ('Shall the force be with you')
			if icolor==1: 
				colorWipe(strip, Color(array_color[0]))  # Red wipe
			if icolor==2:
				colorWipe(strip, Color(array_color[1]))  # Green wipe
			if icolor==3:
				colorWipe(strip, Color(array_color[2]))  # Blue wipe
			if icolor==4:
				colorWipe(strip, Color(127, 127, 0))
			if icolor==5:
				colorWipe(strip, Color(127, 0, 127))
			if icolor==6:
				colorWipe(strip, Color(70, 50, 120))
			if icolor==7:	
				colorWipe(strip, Color(127, 200, 60))
			if icolor==8:
				colorWipe(strip, Color(127, 34, 70))
			if icolor==9:	
				colorWipe(strip, Color(89, 127, 60))
			if icolor==10:
				colorWipe(strip, Color(140, 67, 45))
			if icolor==11:
				flash(strip, Color(200, 200, 200))
			icolor=icolor+1
			if icolor>11:
				icolor=1
		
			#rainbow(strip)
			
			

