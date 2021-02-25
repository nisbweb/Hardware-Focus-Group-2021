#3) Input from button
#button connected to pin 14

#Code
from machine import Pin #Attaches Pin class of functions to the file that can be called as required
from utime import sleep #Attaches sleep class of functions to the file that can be called as required
button = Pin(14, Pin.IN, Pin.PULL_DOWN) #Declares Pin 14 as the component button(button connected to GPIO 14) , Sets it as an INPUT pin , calls for a pull down resistor at that pin
while True: # sets an infinite loop
	if button.value() == 1: #checcks for if the value of button (Pin 14) is 1 or high
		print("I’m High!")
	sleep(0.2) #sets the pico to rest for 0.2 seconds
