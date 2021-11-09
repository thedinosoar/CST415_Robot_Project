from Robot import *

def turnTest():

    # Front Left
    print("(-1000, 0, 0, 0")
    PWM.setMotorModel(-1000, 0, 0, 0)
    time.sleep(1)
    PWM.setMotorModel(0, 0, 0, 0)

    # Back Left
    print("(0, 1000, 0, 0")
    PWM.setMotorModel(0, 1000, 0, 0)
    time.sleep(1)
    PWM.setMotorModel(0, 0, 0, 0)

    # Front Right
    print("(0, 0, 1000, 0")
    PWM.setMotorModel(0, 0, 1000, 0)
    time.sleep(1)
    PWM.setMotorModel(0, 0, 0, 0)

    # Back right
    print("(0, 0, 0, -1000")
    PWM.setMotorModel(0, 0, 0, -1000)
    time.sleep(1)
    PWM.setMotorModel(0, 0, 0, 0)

    print("turning Left")
    PWM.setMotorModel(500, -500, 2000, -2000)
    time.sleep(2)
    PWM.setMotorModel(0, 0, 0, 0)

    print("turning Right")
    PWM.setMotorModel(-2000, 2000, -500, 500)
    time.sleep(2)
    PWM.setMotorModel(0, 0, 0, 0)



def newLeft(moveTime):
    PWM.setMotorModel(-1500,-1500,1500,1500)
    time.sleep(moveTime)

if __name__ == '__main__':

    print ('Program is starting ... ')

    # Input commands for the terminal
    import sys
    if len(sys.argv)==3:
        if sys.argv[1] == '-left':
            if sys.argv[2] > 0:
                newLeft(sys.argv[2])
        if sys.argv[1] == '-right':
            if sys.argv[2] > 0:
                turnRight(sys.argv[2],defaultMoveSpeed)
    if len(sys.argv) == 1:
        turnTest()
    if len(sys.argv) > 6:
        if sys.argv[1] == '-turn':
            try:
                setMotor(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])
                time.sleep(sys.argv[6])
                stopBot()
            except KeyboardInterrupt:
                killBot()
    killBot()



# turnTest()