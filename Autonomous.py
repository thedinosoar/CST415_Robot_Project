from Robot import *
from Buzzer import *

min_dist_before_stop = 20  # minimum distance robot can be
max_fails = 6

def autonomous():
    current_fails = 0
    try:
        while True:
            if len(choiceStack) > 0:
                print("Last direction [", len(choiceStack), "]: ", dirToStr(choiceStack[-1].move_direction), ", ", choiceStack[-1].move_distance, ", ", choiceStack[-1].move_speed)

            # Checks if Robot is too close
            print("Forward Distance:", get_Distance())
            if get_Distance() >= min_dist_before_stop:
                moveForward(defaultMoveDistance, 1000)
                current_fails = 0

            else:
                stopBot()
                # Tries to change direction
                while not changeDirection():
                    # Checks if max number of fails has been reached
                    if current_fails >= max_fails:
                        killBot()
                        test_Buzzer()
                        print("Max fails have been reached, I'm stuck frfr")
                        return False
                    current_fails += 1
                    test_Buzzer()
                    #moveBackward(.2, defaultMoveSpeed)

            time.sleep(.1)

    except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
        killBot()


def furthestChoice(left_path_dist, right_path_dist):  # Returns which path is furthest
    return LEFT if left_path_dist > right_path_dist else RIGHT

def changeDirection():

    print("*Changing Direction*")

    # Get left distance
    look(70)  # looks to the left
    time.sleep(1) # Sleeps for 1 second
    print("Left Distance:", get_Distance())
    left_path = get_Distance()  # Gets distance
    print("left_path = ", left_path)

    # Get right distance
    look(110)  # looks to the right
    time.sleep(1)
    print("Right Distance:", get_Distance())
    right_path = get_Distance()  # Gets distance
    print("right_path = ", left_path)
    lookForward()

    next_direction = furthestChoice(left_path, right_path)
    print("next_direction = ", dirToStr(next_direction))

    if (left_path >= min_dist_before_stop) or (right_path >= min_dist_before_stop):
        turn(next_direction, 1.27, defaultMoveSpeed)
        return True

    print("left and right are too close")
    return False

# This is not finished yet,  but it will backtrack the robots history
def backtrack(enabled):
    if enabled:
        try:
            if len(choiceStack) == 0:
                print("Stack Empty, can't backtrack")
                return False

            new_path_found = False

            while not new_path_found:

                # If the last thing the robot did was turn, turn the other direction
                last_direction = choiceStack[-1].move_direction
                if debugMode:
                    print("last_direction = ", dirToStr(last_direction))
                if last_direction in [LEFT, RIGHT]:
                    # Reverse turn
                    turn(-last_direction, choiceStack[-1].move_distance, choiceStack[-1].move_speed)
                    choiceStack.pop()
                    if debugMode:
                        print("Turning opposite direction: ", dirToStr(-last_direction))
                else:
                    if last_direction in {FORWARD, BACKWARD}:
                        if debugMode:
                            print("Moving last direction = ", dirToStr(-last_direction))
                        turn(-last_direction, 1.27, defaultMoveSpeed)
                        stopBot()
                        return True
            return True
        except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program killBot() will be  executed.
            killBot()

def turn(direction, distance):
    if (direction == LEFT):
        turnLeft(distance)
    if (direction == RIGHT):
        turnRight(distance)

if __name__ == '__main__':

    print('Program is starting ... ')

    # Input commands for the terminal
    import sys
    if len(sys.argv) > 3:
        if sys.argv[1] == '-d':
            if 0 < float(sys.argv[2]) < 30:
                min_dist_before_stop = sys.argv[2]
            else:
                print("Error, proper syntax is: python Autonomous.py -d <min_dist_before_stop>")

    # if sys.argv[1] == 'look':
    #     dir = input("What direction do you want to look?: ")
    #     look(dir)
    #     time.sleep(1)
    #     dist = getDistance()
    #     print(dist)

    autonomous()


autonomous()
killBot()
