import RPi.GPIO as GPIO  # Import the RPi Library for GPIO pin control
import time              # Library will let us put in delays

GPIO.setmode(GPIO.BOARD)  # We want to use the physical pin number scheme
GPIO.setwarnings(False)
GPIO.setup(11, GPIO.OUT)


p = GPIO.PWM(11, 50)

p.start(7.5)

try:
        while True:
		p.ChangeDutyCycle(7.5)  # turn towards 90 degree
		time.sleep(1) # sleep 1 second
		p.ChangeDutyCycle(2.5)  # turn towards 0 degree
		time.sleep(1) # sleep 1 second
		p.ChangeDutyCycle(12.5) # turn towards 180 degree
                time.sleep(1) # sleep 1 second 
except KeyboardInterrupt:
	p.stop()
        GPIO.cleanup() 
