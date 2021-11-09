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
    PWM.setMotorModel(front_left, back_left, front_right, back_right)

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

def sweepView():
    lookLeft()
    leftDistance = ultrasonic.get_distance()
    print(leftDistance)
    time.sleep(.25)
    lookForward()
    centerDistance = ultrasonic.get_distance()
    print(centerDistance)
    time.sleep(.25)
    lookRight()
    rightDistance = ultrasonic.get_distance()
    print(rightDistance)
    # if rightDistance > distanceTolerance and leftDistance > distanceTolerance and centerDistance > distanceTolerance:
    #     return distanceTolerance + 1
    if (rightDistance < leftDistance and rightDistance < centerDistance):
        return 1 #right
    if (leftDistance < rightDistance and leftDistance < centerDistance):
        return 2 #left
    else:
        return 3 #center

buzzer = Buzzer()
def test_Buzzer():
    try:
        buzzer.run('1')
        time.sleep(1)
        buzzer.run('0')
    except KeyboardInterrupt:
        buzzer.run('0')

