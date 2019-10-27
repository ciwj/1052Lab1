import RPi.GPIO as GPIO #Library for the GPIO Pins
import time #Library for time-related tasks

GPIO.setmode(GPIO.BCM) #Sets the way we reference the GPIO Pins
GPIO.setup(25,GPIO.OUT) #Sets GPIO Pin 25 to an output pin

for x in range(5): #iterates through the loop 5 times

    print ("LED on") #Prints when the LED turns on in the console below
    GPIO.output(25,GPIO.HIGH) #Sets the voltage of Pin 25 'HIGH' or 3.3V
    time.sleep(1) #Pauses the program for 1 second
    print ("LED off") #Prints when the LED turns off in the console below
    GPIO.output(25,GPIO.LOW) #Sets the voltage of Pin 25 'LOW' or 0V
    time.sleep(1) #Pauses the program for 1 second
    
GPIO.cleanup()#Resets the GPIO Pins that we used
