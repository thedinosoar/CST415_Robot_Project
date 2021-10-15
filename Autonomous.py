from Robot import *
from Buzzer import *

min_dist_before_stop = 30  # minimum distance robot can be

def CDV(value):
    defaultMoveDistance = value
    autonomous()

def autonomous():
    try:
        while True:
            # stopBot()

            # Checks if Robot can move forward
            if getDistance() > min_dist_before_stop:
                moveForward(defaultMoveDistance, 500)
            else:
                stopBot()
                moveBackward(defaultMoveDistance, defaultMoveSpeed)
                if not changeDirection():  # If the robot can't change direction
                    test_Buzzer()
                    if backtrack(False):
                        if debugMode:
                            print("Attempting backtracking")
                        print("=======================")
                        print("Cannot Backtrack")
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
    if debugMode:
        print("Changing Direction")
    look(70)  # looks to the left
    time.sleep(0.2)
    left_path = getDistance()
    if debugMode:
        print("left_path = ", left_path)
    look(110)  # looks to the right
    time.sleep(0.2)
    right_path = getDistance()
    if debugMode:
        print("right_path = ", left_path)
    lookForward()

    next_direction = furthestChoice(left_path, right_path)
    if debugMode:
        print("next_direction = ", dir(next_direction))
    if next_direction == LEFT:
        if left_path >= min_dist_before_stop:
            turn(next_direction, .5, defaultMoveSpeed)
            return True

    if next_direction == RIGHT:
        if right_path >= min_dist_before_stop:
            turn(next_direction, .5, defaultMoveSpeed)
            return True
    if debugMode:
        print("left and right are too close")
    return False

# This is not finished yet,  but it will backtrack the robots history
def backtrack(enabled):
    if enabled:
        try:
            if choiceStack.__sizeof__() == 0:
                print("Stack Empty, can't backtrack")
                return False

            new_path_found = False

            while not new_path_found:

                # If the last thing the robot did was turn, turn the other direction
                last_direction = choiceStack[-1].move_direction
                if debugMode:
                    print("last_direction = ", dir(last_direction))
                if last_direction is (LEFT or RIGHT):
                    # Reverse turn
                    turn(-last_direction, choiceStack[-1].move_distance, choiceStack[-1].move_speed)
                    choiceStack.pop()
                    if debugMode:
                        print("Turning opposite direction: ", dir(-last_direction))
                else:
                    if last_direction is (FORWARD or BACKWARD):
                        if debugMode:
                            print("Moving last direction = ", dir(-last_direction))
                        turn(-last_direction, 1, defaultMoveSpeed)
                        stopBot()
                        new_path_found = True
                        return True
            return True
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
killBot()
