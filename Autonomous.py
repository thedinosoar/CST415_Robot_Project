from enum import Enum
from Robot import *

min_dist_before_stop = 30  # minimum distance robot can be

def autonomous():

    # autonomous = 1 # Bool to run autonomous mode. Will be used later as a safeguard to shut off autonomous mode
    try:
        while True:
            stopBot()

            # Checks if Robot can move forward
            if getDistance() > min_dist_before_stop:
                moveForward()
            else:
                if not changeDirection():
                    backTrack()

    except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
        killBot()

def furthestChoice(left_path, right_path):  # Returns which path is furthest

    # Checks if the left path is far enough from the min distance
    if left_path < min_dist_before_stop:
        if right_path < min_dist_before_stop:
            return 0
        return RIGHT

    # Checks if the right path is far enough from the min distance
    if right_path < min_dist_before_stop:
        if left_path < min_dist_before_stop:
            return STOP
        return LEFT

    # Checks which path is further
    if left_path < right_path:
        return LEFT
    if right_path < left_path:
        return RIGHT
    if left_path == right_path:
        print("Path options are equal")
        return False

def closestChoice(left_path, right_path):  # Returns which path is furthest

    # Checks if the left path is far enough from the min distance
    if left_path < min_dist_before_stop:
        if right_path < min_dist_before_stop:
            return 0
        return RIGHT

    # Checks if the right path is far enough from the min distance
    if right_path < min_dist_before_stop:
        if left_path < min_dist_before_stop:
            return STOP
        return LEFT

    # Checks which path is further
    if left_path > right_path:
        return LEFT
    if right_path > left_path:
        return RIGHT
    if left_path == right_path:
        print("Path options are equal")
        return 0

def changeDirection():
    look(70) # looks to the left
    time.sleep(0.2)
    left_path = getDistance()

    look(110) # looks to the right
    time.sleep(0.2)
    right_path = getDistance()

    lookForward()

    next_direction = furthestChoice(left_path, right_path)
    turn(next_direction)

    # returns whether or not the robot could change directions
    if not next_direction:
        return False
    else:
        return True

# This is not finished yet,  but it will backtrack the robots history
def backTrack():
    return 0


    if choiceStack.__sizeof__() == 0:
        print("Stack Empty, cam't backtrack")
        return False

    new_path_found = False

    while(not new_path_found):

        if(choiceStack[choiceStack.__sizeof__()-1].move_direction == (LEFT or RIGHT)):
            turn(-choiceStack[choiceStack.__sizeof__()-1].move_direction,choiceStack.__sizeof__()-1].move_distance, choiceStack.__sizeof__()-1].move_speed)
            choiceStack.pop()




def test():
    try:
        # PWM.setMotorModel(0,0,0,-1000)
        # time.sleep(2)
        for i in range(70,110,5):
            pwm_S.setServoPwm('0', i)
            time.sleep(0.2)
    except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
        killBot()


autonomous()
