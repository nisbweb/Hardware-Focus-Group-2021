#4)Combining input and output
#led connected to pin 15
#button connected to pin 14

#b)LED keeps blinking as long as you keep the button pressed, release thebutton and LED stops blinking
#Code
from machine import Pin #Attaches Pin class of functions to the file that can be called as required
from utime import sleep #Attaches sleep class of functions to the file that can be called as required
led_e = Pin(15, Pin.OUT) #Declares avariable/component LED and tells that it's attached to Pin 25
button = Pin(14, Pin.IN, Pin.PULL_DOWN) #Declares Pin 14 as the component button(button connected to GPIO 14) , Sets it as an INPUT pin , calls for a pull down resistor at that pin
while True: # sets an infinite loop
	if button.value() == 1: #checcks for if the value of button (Pin 14) is 1 or high
		while True:
			led_e.toggle() #Toggles the state of LED between on and off(if on then off and vice versa)
			sleep(0.5) #sets the pico to rest for 0.2 seconds
			if button.value() == 0:
				break #breaks out of or exits the current loop
	sleep(0.1)