import time
import pyupm_grove as grove
import pyupm_ttp223 as ttp223

# Create the button object using GPIO pin 2
button = grove.GroveButton(2)
# Create the TTP223 touch sensor object using GPIO pin 3
touch = ttp223.TTP223(3)
# Create the light sensor object using AIO pin 0
light = grove.GroveLight(0)
# New knob on AIO pin 1
knob = grove.GroveRotary(1)
# Create the temperature sensor object using AIO pin 2
temp = grove.GroveTemp(2)


while 1:
	print 		' Button ------------------ ', button.value()
	if touch.isPressed():
		print 	' Touch ------------------- ', True
	else:
		print 	' Touch ------------------- ', False
	print		' Light ------------------- ',light.value()
	print 		' Celsius ----------------- ',temp.value()
	print 		' Pot --------------------- ',knob.abs_value()

	time.sleep(1)

# Delete the button object
del button
# Delete the touch sensor object
del touch
# Delete the light sensor object
del light
# Delete the temperature sensor object
del temp