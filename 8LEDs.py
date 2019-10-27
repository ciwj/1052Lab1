import RPi.GPIO as GPIO #Library for the GPIO Pins
import time #Library for time-related tasks

GPIO.setmode(GPIO.BCM) #Sets the way we reference the GPIO Pins

pins1 = [25, 8, 7, 1, 12, 16, 20, 21] # Ordered pin numbers for turning on.
pins2 = [25, 7, 12, 20, 8, 1, 16, 21] # Ordered pin numbers for turning off.

# Set all relevant pins as outputs.
for pin in pins1:
    GPIO.setup(pin,GPIO.OUT)

for pin in pins1: # Turn on all pins.
    GPIO.output(pin,GPIO.HIGH)
    print("Pin", pin, "activated.")
    time.sleep(0.5)
for pin in pins2: # Turn off all pins.
    GPIO.output(pin,GPIO.LOW)
    print("Pin", pin, "de-activated.")
    time.sleep(0.5)