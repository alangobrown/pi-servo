# Don't try to run this as a script or it will all be over very quickly  
# it won't do any harm though.  
# these are all the elements you need to control PWM on 'normal' GPIO ports  
# with RPi.GPIO - requires RPi.GPIO 0.5.2a or higher  
  
import RPi.GPIO as GPIO # always needed with RPi.GPIO  
  
import time

GPIO.setmode(GPIO.BCM)  # choose BCM or BOARD numbering schemes. I use BCM  
  
GPIO.setup(4, GPIO.OUT)# set GPIO 25 as an output. You can use any GPIO port  
  
p = GPIO.PWM(4, 50)    # create an object p for PWM on port 25 at 50 Hertz  
                        # you can have more than one of these, but they need  
                        # different names for each port   
                        # e.g. p1, p2, motor, servo1 etc.  
print("Starting PWM")  
p.start(5)             # start the PWM on 50 percent duty cycle  
                        # duty cycle value can be 0.0 to 100.0%, floats are OK  

time.sleep(1)  
p.ChangeDutyCycle(6)  

time.sleep(1)  
p.ChangeDutyCycle(7)  

time.sleep(1)  
p.ChangeDutyCycle(8)  

time.sleep(1)  
p.ChangeDutyCycle(9)  

time.sleep(1)  
p.ChangeDutyCycle(10)  

time.sleep(1)  
p.ChangeDutyCycle(11)  

time.sleep(5)  
p.ChangeDutyCycle(10)  

time.sleep(1)  
p.ChangeDutyCycle(9)  

time.sleep(1)  
p.ChangeDutyCycle(8)  

time.sleep(1)  
p.ChangeDutyCycle(7)  

time.sleep(1)  
p.ChangeDutyCycle(6)  

time.sleep(1)  
p.ChangeDutyCycle(5)  

time.sleep(1)  
p.ChangeDutyCycle(4)  

time.sleep(1)  
p.ChangeDutyCycle(3)  

time.sleep(1)  
p.ChangeDutyCycle(2)  

time.sleep(1)  
p.ChangeDutyCycle(1)  

time.sleep(2)  
print("Stopping the script")
p.stop()                # stop the PWM output  
  
GPIO.cleanup()          # when your program exits, tidy up after yourself 