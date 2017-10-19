import time
import RPi.GPIO as GPIO
from random import randint
import threading

class LED:
    
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(11,GPIO.OUT)
    GPIO.setwarnings(False)
    p = GPIO.PWM(11,60)
    feedback = True

    def blink(self):
        self.feedback = True
        try:
            while self.feedback == True:
                self.p.start(50)
                i = randint(1,100)
                if i > 50:
                    self.p.ChangeDutyCycle(50)
                else:
                    self.p.ChangeDutyCycle(i)
                    time.sleep(0.12)
            self.p.stop()


        except KeyboardInterrupt:
            print("Terminated by user")
            self.p.stop()
            GPIO.cleanup()
            print("Cleanup complete")