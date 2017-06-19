import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(3,GPIO.OUT)     #Define pin 3 as an output pin
GPIO.setup(3,GPIO.OUT)
GPIO.setup(3,GPIO.OUT)

while True:
        GPIO.output(3,1)   #Outputs digital HIGH signal (5V) on pin 3
        time.sleep(3)      #Time delay of 1 second

        GPIO.output(3,0)   #Outputs digital LOW signal (0V) on pin 3
        time.sleep(3)      #Time delay of 1 second