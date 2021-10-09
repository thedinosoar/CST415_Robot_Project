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
            stopBot()   #stops bot each cycle to prevent any big collisions during testing
            dist = Ultrasonic.get_distance()  #checks in front of itself first before moving
            if dist > minDist:                #if there are no obstacles within minDistance than move forward
                moveForward()
            else:                             #runs if it senses obstacle within minDistance
                stopBot()                     #stops bot when it spotted an obstacle
                for i in range(70,111,40):    #for loop to cycle through left and right servo positions
                    pwm_S.setServoPwm('0',i)  #sets servo direction
                    time.sleep(0.2)
                    if i==70:                 #if servo is left grab that distance
                        L = Ultrasonic.get_distance()
                    elif i==110:              #if servo is right grab that distance
                        R = Ultrasonic.get_distance()
                path = decidePath(L,R)        #decides best path with left and right distances
                if (path == 1):               #means right path is better. Turn right
                    moveRight()
                elif (path == 2):             #means left path is better. Turn left
                    moveLeft() 
                elif (path == 3):             #both left and right options are blocked. Will be decided in future steps
                    stopBot()
                    print("haven't implemented stack yet. Don't know where to go.")
                
    except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
        PWM.setMotorModel(0,0,0,0)
        pwm_S.setServoPwm('0',90)

def decidePath(left,right):                 #function to decide which path is better
    Lf = left                               
    Rt = right
    if Lf < Rt:                             #if left distance is less than right, return 1
        return 1
    if Rt < Lf:                             #if right is less than left, return 2
        return 2
    if Lf == Rt:                            #if both are the same, return 3
        return 3

#Functions to move the bot
def moveForward():
    PWM.setMotorModel(-1000,1000,1000,-1000)    #Front left and back right wheel inputs are reversed for some reason
    time.sleep(0.1)

def moveLeft():
    PWM.setMotorModel(500,-500,2000,-2000)
    time.sleep(0.1)

def moveRight():
    PWM.setMotorModel(-2000,2000,-500,500)
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