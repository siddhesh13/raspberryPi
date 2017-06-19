from time import sleep  # Library will let us put in delays
import RPi.GPIO as GPIO # Import the RPi Library for GPIO pin control
GPIO.setmode(GPIO.BOARD)# We want to use the physical pin number scheme
GPIO.setwarnings(False)
LED1=22
LED2=18
LED3=12
GPIO.setup(LED1,GPIO.OUT) # LED1 will be an output pin
GPIO.setup(LED2,GPIO.OUT) # LED2 will be an output pin
GPIO.setup(LED3,GPIO.OUT)
pwm1=GPIO.PWM(LED1,1000)  # We need to activate PWM on LED1 so we can dim, use 1000 Hz
pwm2=GPIO.PWM(LED2,1000)  # We need to activate PWM on LED2 so we can dim, use 1000 Hz
pwm3=GPIO.PWM(LED3,1000)
pwm1.start(0)              # Start PWM at 0% duty cycle (off)            
pwm2.start(0)              # Start PWM at 0% duty cycle (off)
pwm3.start(0)
bright=1                   # Set initial brightness to 1%

while(1):                  # Loop Forever
 #Red led  
    for bright in range (0,100,4):
     
        pwm1.ChangeDutyCycle(bright)   # Apply new brightness
       
        sleep(.10)                     # Briefly Pause
        print "New Green Brightness is: ",bright # Notify User of Brightness



    for bright in range (100,0,-4):
       
        if bright==100:                 # Keep Brightness at or below 100%
           print "You are at Full Bright"
        
        pwm1.ChangeDutyCycle(bright)  # Apply new brightness
      
        sleep(.10)                    # Pause
        print "New Green Brightness is: ",bright #Notify User of Brightness
      



#green Led
    for bright in range (0,100,4):
       
        pwm2.ChangeDutyCycle(bright)   # Apply new brightness
        sleep(.10)                     # Briefly Pause
        print "New Blue Brightness is: ",bright # Notify User of Brightness


    for bright in range (100,0,-4):
      
        if bright==100:                 # Keep Brightness at or below 100%
           print "You are at Full Bright"
        
     
        pwm2.ChangeDutyCycle(bright)  # Apply new brightness
        sleep(.10)                    # Pause
        print "New Blue Brightness is: ",bright #Notify User of Brightness
     



  #blue Led
    for bright in range (0,100,4):
        
        pwm3.ChangeDutyCycle(bright)   # Apply new brightness
     
        sleep(.10)                     # Briefly Pause
        print "New Red Brightness is: ",bright # Notify User of Brightness



    for bright in range (100,0,-4):
    
        if bright==100:                 # Keep Brightness at or below 100%
           print "You are at Full Bright"
        
        pwm3.ChangeDutyCycle(bright)  # Apply new brightness
       
        sleep(.10)                    # Pause
        print "New Red Brightness is: ",bright #Notify User of Brightness
 
