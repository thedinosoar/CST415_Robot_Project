import time
from Motor import *
import RPI.GPIO as GPIO
from servo import *
from Utrasonic import *
from PCA9685 import PCA9685

def moveForward(): 
    dist = get_distance(self)   #gets current distance
    minDist = 30                #minimum distance robot can be
    autonomous = 1              #Bool to run autonomous mode. Will be used later as a safeguard to shut off autonomous mode
    
    while autonomous:
        if dist <= minDist:
            self.PWM.setMotorModel(0,0,0,0)
            time.sleep(3)
            pwm.setServoPwm('0',90) #checks right
            time.sleep(3)
            dist = get_distance(self)
        else if: 


    