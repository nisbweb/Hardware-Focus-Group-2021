#2) Blinking external LED
# led connected to pin 15

# Code

from machine import Pin #Attaches Pin class of functions to the file that can be called as required
from utime import sleep #Attaches sleep class of functions to the file that can be called as required
led_e = Pin(15, Pin.OUT) #Declares avariable/component LED and tells that it's attached to Pin 25
while True: # sets an infinite loop
	led_e(1) #sets Pin named LED (Pin 25) to High or 1 , led_e(1) same as led_e.value(1) 
	sleep(0.5)
	led_e(0)
	sleep(0.5)
	
#Using toggle function Alternate code
#from machine import Pin
#from utime import sleep
#led_e = Pin(15, Pin.OUT)
#while True:
#	led_e.toggle() #Toggles the state of LED between on and off(if on then off and vice versa)
#	sleep(0.2)

