import time
from Motor import *
import RPI.GPIO as GPIO
from servo import *
from Utrasonic import *
from PCA9685 import PCA9685
PWM = Motor()
pwm_S = Servo()
ultrasonic = Ultrasonic()

def autonomous(self): 
    minDist = 30                #minimum distance robot can be
    autonomous = 1              #Bool to run autonomous mode. Will be used later as a safeguard to shut off autonomous mode
    while autonomous:
        stopBot()
        dist = get_distance(self)  #checks in front of itself first before moving
        if dist <= minDist:
            stopBot()
            for i in range(30,151,120):
                self.pwm_S.setServoPwm('0',i)
                time.sleep(0.2)
                if i==30:
                    L = self.get_distance()
                elif i==150:
                    R = self.get_distance()
            path = self.decidePath(L,R)
            if (path == 1):
                moveRight()
            elif (path == 2):
                moveLeft() 
            elif (path == 3):
                stopBot()
                print("haven't implemented stack yet. Don't know where to go.")
        else:
            moveForward()

def decidePath(self,left,right):
    L = left
    R = right
    if L < R:
        return 1
    if R < L:
        return 2
    if L == R:
        return 3

def moveForward():
    self.PWM.setMotorModel(1000,1000,1000,1000)
    time.sleep(2)

def moveLeft():
    self.PWM.setMotorModel(-500,-500,1500,1500)
    time.sleep(2)

def moveRight():
    self.PWM.setMotorModel(1500,1500,-500,-500)
    time.sleep(2)

def stopBot():
    self.PWM.setMotorModel(0,0,0,0)
    time.sleep(2)

def main():
    autonomous = autonomous()
    try:
        autonomous.run()
    except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
        PWM.setMotorModel(0,0,0,0)
        pwm_S.setServoPwm('0',90)

main()