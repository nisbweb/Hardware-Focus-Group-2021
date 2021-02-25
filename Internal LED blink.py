#1)Blinking internal LED
#Internal LED connected inteernally to pin 25

#Code
from machine import Pin #Attaches Pin class of functions to the file that can be called as required
from utime import sleep #Attaches sleep class of functions to the file that can be called as required
led = Pin(25, Pin.OUT) #Declares avariable/component LED and tells that it's attached to Pin 25
while True: # sets an infinite loop
	led.value(1) #sets Pin named LED (Pin 25) to High or 1
	sleep(0.5) #sets the pico to rest for 0.5 seconds
	led.value(0)
	sleep(0.5)
