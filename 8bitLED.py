import RPi.GPIO as GPIO #Library for the GPIO Pins
import time #Library for time-related tasks

GPIO.setmode(GPIO.BCM) #Sets the way we reference the GPIO Pins

pins = [25, 1, 7, 8, 12, 16, 20, 21] # define all pins

for pin in pins: # set all relevant pins as outputs.
    GPIO.setup(pin,GPIO.OUT)

for x in range(248): # lab leader last # is 8, therefore count to 247.
    for num in range(1,9): # go through all pins
        if x % 2 == 0: # if divisible by 2, set low, otherwise set high.
            GPIO.output(pins[-num],GPIO.LOW)
        else:
            GPIO.output(pins[-num],GPIO.HIGH)
        x = x // 2 # divide by two and round down
    time.sleep(0.5)
