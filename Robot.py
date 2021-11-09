import time
from Motor import *
from servo import *
from Ultrasonic import *
from PCA9685 import PCA9685
from Buzzer import *
PWM = Motor()
pwm_S = Servo()
Ultrasonic = Ultrasonic()

# Variables
defaultMoveDistance = .3
defaultMoveSpeed = 1000
defaultTurnDistance = 1
choiceStack = []
debugMode = True

# A fixed motor function with proper wheel direction

def setMotor(front_left, back_left, front_right, back_right):
    PWM.setMotorModel(-ront_left, back_left, front_right, back_right)

# Movement Functions

def moveForward(distance):
    #PWM.setMotorModel(-speed, speed, speed, -speed)
    setMotor(600,600,600,600)
    time.sleep(distance)

def moveBackward(distance):
    # PWM.setMotorModel(speed, -speed, -speed, speed)
    setMotor(-600,-600,-600,-600)
    time.sleep(distance)
    # choiceStack.append(Choice(BACKWARD, distance, speed))
    # PWM.setMotorModel(0, 0, 0, 0)

def turnLeft(distance):
    setMotor(-1500, -1500, 1500, 1500)
    time.sleep(distance)

def turnRight(distance):
    setMotor(1500, 1500,-1500,-1500)
    time.sleep(distance)

def stopBot():  # Stops the bot
    PWM.setMotorModel(0, 0, 0, 0)
    time.sleep(.5)

def killBot():
    PWM.setMotorModel(0, 0, 0, 0)
    pwm_S.setServoPwm('0', 90)
    buzzer.run('0')

# Servo Functions

def get_distance():
    dist = Ultrasonic.get_distance()
    time.sleep(.25)
    return dist

def lookForward():
    pwm_S.setServoPwm('0', 60)
    time.sleep(.25)

def lookRight():
    pwm_S.setServoPwm('0', 120)
    #pwm_S.setServoPwm('1',40)
    time.sleep(.25)

def lookLeft():
    pwm_S.setServoPwm('0', 0)
    time.sleep(.25)

buzzer = Buzzer()
def test_Buzzer():
    try:
        buzzer.run('1')
        time.sleep(1)
        buzzer.run('0')
    except KeyboardInterrupt:
        buzzer.run('0')

