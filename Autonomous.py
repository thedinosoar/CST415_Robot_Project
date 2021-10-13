from Robot import *
from Buzzer import *

min_dist_before_stop = 30  # minimum distance robot can be

def autonomous():

    try:
        while True:
            stopBot()

            # Checks if Robot can move forward
            if getDistance() > min_dist_before_stop:
                moveForward()
            else:
                if not changeDirection(): # If the robot can't change direction
                    test_Buzzer()
                    if not backtrack(False):
                        print("=======================")
                        print("Cannot Backtrack, stack empty")
                        print("Ending program...")
                        killBot()
                        return 0
            time.sleep(.1)

    except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
        killBot()


def furthestChoice(left_path_dist, right_path_dist):  # Returns which path is furthest
    if left_path_dist > right_path_dist:
        return LEFT
    return RIGHT

def changeDirection():
    look(70)  # looks to the left
    time.sleep(0.2)
    left_path = getDistance()
    look(110)  # looks to the right
    time.sleep(0.2)
    right_path = getDistance()
    lookForward()

    next_direction = furthestChoice(left_path, right_path)
    if next_direction is LEFT:
        if left_path >= min_dist_before_stop:
            turn(next_direction)
            return True

    if next_direction is RIGHT:
        if right_path >= min_dist_before_stop:
            turn(next_direction)
            return True

    return False

# This is not finished yet,  but it will backtrack the robots history
def backtrack(function_done):
    if not function_done:
        return not False

    try:
        if choiceStack.__sizeof__() == 0:
            print("Stack Empty, can't backtrack")
            return False

        new_path_found = False

        while not new_path_found:

            # If the last thing the robot did was turn, turn the other direction
            if choiceStack[-1].move_direction is (LEFT or RIGHT):
                turn(-choiceStack[-1].move_direction, choiceStack[-1].move_distance, choiceStack[-1].move_speed)
                choiceStack.pop()

    except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
        killBot()


def test():
    try:
        # PWM.setMotorModel(0,0,0,-1000)
        # time.sleep(2)
        for i in range(70, 110, 5):
            pwm_S.setServoPwm('0', i)
            time.sleep(0.2)
    except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
        killBot()





autonomous()
