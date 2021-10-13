import time
from Motor import *
from servo import *
from Ultrasonic import *
from PCA9685 import PCA9685
from Buzzer import *
PWM = Motor()
pwm_S = Servo()
Ultrasonic = Ultrasonic()

# Enum for directions

LEFT = 256
RIGHT = -256
FORWARD = 257
BACKWARD = -257
STOP = 0

# Variables
defaultMoveDistance = 0.1
defaultMoveSpeed = 1000
choiceStack = []

class Choice:
    def __init__(self, move_direction, move_distance, move_speed):
        self.move_direction = move_direction
        self.move_distance = move_distance
        self.move_speed = move_speed


# Movement Functions
def moveForward():  # Moves the bot Forward default distance
    PWM.setMotorModel(-defaultMoveSpeed, defaultMoveSpeed, defaultMoveSpeed, -defaultMoveSpeed)
    time.sleep(defaultMoveDistance)
    choiceStack.append(Choice(FORWARD,defaultMoveDistance, defaultMoveSpeed))

def moveForwardSpecified(distance, speed):
    PWM.setMotorModel(-speed, speed, speed, -speed)
    time.sleep(distance)
    choiceStack.append(Choice(FORWARD,distance, speed))


def moveBackward(): # Moves the bot backward default distance
    PWM.setMotorModel(defaultMoveSpeed, -defaultMoveSpeed, -defaultMoveSpeed, defaultMoveSpeed)    # Front left and back right wheel inputs are reversed for some reason
    time.sleep(defaultMoveDistance)
    choiceStack.append(Choice(BACKWARD,defaultMoveDistance, defaultMoveSpeed))
def moveBackwardSpecified(distance, speed):
    PWM.setMotorModel(speed, -speed, -speed, speed)
    time.sleep(distance)
    choiceStack.append(Choice(BACKWARD,distance, speed))


def turnLeft(): # Turns the bot to the left
    PWM.setMotorModel(0.5*defaultMoveSpeed, -0.5*defaultMoveSpeed, 2*defaultMoveSpeed, -2*defaultMoveSpeed)
    time.sleep(defaultMoveDistance)
    choiceStack.append(Choice(LEFT,defaultMoveDistance, defaultMoveSpeed))
def turnLeftSpecified(distance, speed):
    PWM.setMotorModel(.5*speed, -.5*speed, 2*speed, -2*speed)
    time.sleep(distance)
    choiceStack.append(Choice(LEFT,distance, speed))


def turnRight(): # Turns the bot to the right
    PWM.setMotorModel(-2*defaultMoveSpeed, 2*defaultMoveSpeed, -.5*defaultMoveSpeed, .5*defaultMoveSpeed)
    time.sleep(defaultMoveDistance)
    choiceStack.append(Choice(RIGHT,defaultMoveDistance, defaultMoveSpeed))
def turnRightSpecified(distance, speed):
    PWM.setMotorModel(-2*speed, 2*speed, -.5*speed, .5*speed)
    time.sleep(distance)
    choiceStack.append(Choice(FORWARD,defaultMoveDistance, defaultMoveSpeed))

def turn(direction):
    if direction == LEFT:
        turnLeft()
    if direction == RIGHT:
        turnRight()
    if direction == STOP:
        stopBot()
    print("turn() ERROR: Input should be LEFT, RIGHT, or STOP")
def turnSpecified(direction, duration, speed):
    if direction == LEFT:
        turnLeft(duration, speed)
    if direction == RIGHT:
        turnRight(duration, speed)
    if direction == STOP:
        stopBot()
    print("turn() ERROR: Input should be LEFT, RIGHT, or STOP")

def stopBot(): # Stops the bot
    PWM.setMotorModel(0, 0, 0, 0)
    time.sleep(defaultMoveDistance)


def killBot():
    PWM.setMotorModel(0, 0, 0, 0)
    pwm_S.setServoPwm('0', 90)

# Servo Functions

def getDistance():
    return Ultrasonic.get_distance()

def lookForward():
    pwm_S.setServoPwm('0', 90)

def look(direction):
    pwm_S.setServoPwm('0', direction)

buzzer=Buzzer()
def test_Buzzer():
    try:
        buzzer.run('1')
        time.sleep(1)
        buzzer.run('0')
    except KeyboardInterrupt:
        buzzer.run('0')