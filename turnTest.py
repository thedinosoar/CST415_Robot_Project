from Robot import *

def turnTest():

    print("(500, 0, 0, 0")
    PWM.setMotorModel(500, 0, 0, 0)
    time.sleep(1)
    PWM.setMotorModel(0, 0, 0, 0)

    print("(0, -500, 0, 0")
    PWM.setMotorModel(0, -500, 0, 0)
    time.sleep(1)
    PWM.setMotorModel(0, 0, 0, 0)

    print("(0, 0, 500, 0")
    PWM.setMotorModel(0, 0, 500, 0)
    time.sleep(1)
    PWM.setMotorModel(0, 0, 0, 0)

    print("(0, 0, 0, -500")
    PWM.setMotorModel(0, 0, 0, -500)
    time.sleep(1)
    PWM.setMotorModel(0, 0, 0, 0)

    print("turning Left")
    PWM.setMotorModel(0, -500, 0, -2000)
    time.sleep(2)
    PWM.setMotorModel(0, 0, 0, 0)

    print("turning Right")
    PWM.setMotorModel(-2000, 2000, -500, 500)
    time.sleep(2)
    PWM.setMotorModel(0, 0, 0, 0)

turnTest()