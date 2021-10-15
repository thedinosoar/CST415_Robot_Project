from Robot import *

def turnTest():

    # Front Left
    print("(1000, 0, 0, 0")
    PWM.setMotorModel(1000, 0, 0, 0)
    time.sleep(1)
    PWM.setMotorModel(0, 0, 0, 0)

    # Back Left
    print("(0, -1000, 0, 0")
    PWM.setMotorModel(0, -1000, 0, 0)
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
    PWM.setMotorModel(-500, 500, 2000, -2000)
    time.sleep(2)
    PWM.setMotorModel(0, 0, 0, 0)

    print("turning Right")
    PWM.setMotorModel(-2000, 2000, -500, 500)
    time.sleep(2)
    PWM.setMotorModel(0, 0, 0, 0)

turnTest()