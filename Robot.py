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
debugMode = True

class Choice:
    def __init__(self, move_direction, move_distance, move_speed):
        self.move_direction = move_direction
        self.move_distance = move_distance
        self.move_speed = move_speed


# Movement Functions

def moveForward(distance, speed):
    PWM.setMotorModel(-speed, speed, speed, -speed)
    # time.sleep(distance)
    choiceStack.append(Choice(FORWARD, distance, speed))
    # PWM.setMotorModel(0, 0, 0, 0)


def moveBackward(distance, speed):
    PWM.setMotorModel(speed, -speed, -speed, speed)
    time.sleep(distance)
    choiceStack.append(Choice(BACKWARD, distance, speed))
    PWM.setMotorModel(0, 0, 0, 0)

def turnLeft(duration, speed):
    # PWM.setMotorModel(speed, -smallSpeed, speed, -smallSpeed)
    PWM.setMotorModel(500, -500, 2000, -2000)
    time.sleep(2*duration)
    choiceStack.append(Choice(LEFT, duration, speed))
    PWM.setMotorModel(0, 0, 0, 0)

def turnRight(duration, speed):
    # PWM.setMotorModel(-speed, smallSpeed, -speed, smallSpeed)
    PWM.setMotorModel(-2000, 2000, -500, 500)
    time.sleep(2*duration)
    choiceStack.append(Choice(RIGHT, duration, speed))
    PWM.setMotorModel(0, 0, 0, 0)

def turn(direction, duration, speed):
    if direction == LEFT:
        turnLeft(duration, speed)
        return True
    if direction == RIGHT:
        turnRight(duration, speed)
        return True
    if direction == STOP:
        PWM.setMotorModel(0, 0, 0, 0)
        return True
    print("turn() ERROR: Input should be LEFT, RIGHT, or STOP")


def stopBot(): # Stops the bot
    PWM.setMotorModel(0, 0, 0, 0)


def killBot():
    PWM.setMotorModel(0, 0, 0, 0)
    pwm_S.setServoPwm('0', 90)
    buzzer.run('0')

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

def dir(input):
    if LEFT:
        return "LEFT"
    if RIGHT:
        return "RIGHT"
    if BACKWARD:
        return "BACKWARD"
    if FORWARD:
        return "FORWARD"
    if STOP:
        return "STOP"
    return "<Error: Bad input>"
