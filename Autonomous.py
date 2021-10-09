import time
from Motor import *
from servo import *
from Ultrasonic import *
from PCA9685 import PCA9685
PWM = Motor()
pwm_S = Servo()
Ultrasonic = Ultrasonic()

def autonomous(): 
    minDist = 30                #minimum distance robot can be
    #autonomous = 1              #Bool to run autonomous mode. Will be used later as a safeguard to shut off autonomous mode
    try:
        while True:
            stopBot()
            L,R
            dist = Ultrasonic.get_distance()  #checks in front of itself first before moving
            if dist > minDist:
                moveForward()
            else:
                stopBot()
                for i in range(70,110,40):
                    pwm_S.setServoPwm('0',i)
                    time.sleep(0.2)
                    if i==70:
                        L = Ultrasonic.get_distance()
                    elif i==110:
                        R = Ultrasonic.get_distance()
                path = decidePath(L,R)
                if (path == 1):
                    moveRight()
                elif (path == 2):
                    moveLeft() 
                elif (path == 3):
                    stopBot()
                    print("haven't implemented stack yet. Don't know where to go.")
                
    except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
        PWM.setMotorModel(0,0,0,0)
        pwm_S.setServoPwm('0',90)

def decidePath(left,right):
    Lf = left
    Rt = right
    if Lf < Rt:
        return 1
    if Rt < Lf:
        return 2
    if Lf == Rt:
        return 3

def moveForward():
    PWM.setMotorModel(-1000,1000,1000,-1000)
    time.sleep(0.1)

def moveLeft():
    PWM.setMotorModel(500,-500,1500,-1500)
    time.sleep(0.1)

def moveRight():
    PWM.setMotorModel(-1500,1500,-500,500)
    time.sleep(0.1)

def stopBot():
    PWM.setMotorModel(0,0,0,0)
    time.sleep(0.1)

def test():
    try:
        # PWM.setMotorModel(0,0,0,-1000)
        # time.sleep(2)
        for i in range(70,110,5):
            pwm_S.setServoPwm('0',i)
            time.sleep(0.2)
    except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
        PWM.setMotorModel(0,0,0,0)
        pwm_S.setServoPwm('0',90)

autonomous()
#test()