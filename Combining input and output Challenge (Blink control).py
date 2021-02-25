#4)Combining input and output
#led connected to pin 15
#button connected to pin 14

#c)Press the button for x seconds and the LED will blink at a frequency of 10x Hz (Desired Action)
#Code’’’

from machine import Pin
from utime import sleep
led_e = Pin(15, Pin.OUT)
button = Pin(14, Pin.IN, Pin.PULL_DOWN)
x = 0
while True:
	if button.value() == 1:
		x = x+1
		sleep(1)
	elif x == 1:
		break

x = 10*x
while True:
	led_e.toggle()
	sleep(1/x)

#The above code has a single error, one that will not show up as an error when you Run it, but it wont work.
#It's a challenge for you to figure out the single error and resolve it to get the desired action as output
#Happy tinkering!