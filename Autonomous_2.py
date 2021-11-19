from MoveNode import *  
from Buzzer import *
from Robot import *
# buzzer=Buzzer()       
# PWM = Motor() 
# servoPWM = Servo()
# ultrasonic = Ultrasonic()   

distanceTolerance = 25

def test():
    moveHistory = MoveStack()
    moveHistory.push(MoveNode(1, "F"))
    moveHistory.push(MoveNode(1, "R"))

    moveHistory.pop().reverse().print()
    moveHistory.pop().reverse().print()
    
    lookRight() #Right
    time.sleep(1)
    lookCenter() # Roughly center
    time.sleep(1)
    servoPWM.setServoPwm('0', 40)

def drive(): 
    moveHistory = MoveStack()
    try:
        while True:
            lookForward()
            forwardDistance = sweepThisView()  
            if forwardDistance > distanceTolerance:
                moveForward(.1)
                #moveHistory.push(MoveNode(1, "F"))
                continue

            rightDistance = 0
            lookForward()
            startBuzzer()
            moveBackward(.2)
            while rightDistance < distanceTolerance:
                print(str(rightDistance) + " CM")
                turnRight(1.27)
                stopBot()
                rightDistance = get_distance()
                time.sleep(.1)

            stopBuzzer()
            #rightDistance = get_distance()  
            #if rightDistance > distanceTolerance:
                #turnRight()
                #moveHistory.push(MoveNode(1, "R"))
                #continue

            #leftDistance = get_distance()
            #if leftDistance > distanceTolerance:
                #turnLeft()
                #moveHistory.push(MoveNode(1, "L"))
                #continue

            #reverseMove = moveHistory.pop().reverse()

            #if reverseMove.direction == "F":
                #moveForward(1)
                #moveHistory.push(MoveNode(1, "F"))
            #elif reverseMove.direction == "B":
                #moveBackward(1)
                #moveHistory.push(MoveNode(1, "B"))
            #elif reverseMove.direction == "R":
                #turnRight(1)
                #moveHistory.push(MoveNode(1, "R"))
            #elif reverseMove.direction == "L":
                #turnLeft(1)
                #moveHistory.push(MoveNode(1, "L"))


            
            

    except KeyboardInterrupt:
        PWM.setMotorModel(0,0,0,0)
        print ("\nEnd of program")

#40 because distance thing, lazy for now
#5 to fail distance test

def sweepThisView():
    lookLeft()
    leftDistance = get_distance()
    time.sleep(.25)
    lookForward()
    centerDistance = get_distance()
    time.sleep(.25)
    lookRight()
    rightDistance = get_distance()
    if rightDistance > distanceTolerance and leftDistance > distanceTolerance and centerDistance > distanceTolerance:
        return distanceTolerance + 1
    
    return 5

# def moveForward(distance):
#     PWM.setMotorModel(500,500,500,500)
#     time.sleep(distance)

# def moveBackward(distance):
#     PWM.setMotorModel(-500,-500,-500,-500)
#     time.sleep(distance)

# def turnLeft():
#     PWM.setMotorModel(-1500,-1500,2000,2000)
#     time.sleep(.2)

# def turnRight():
#     PWM.setMotorModel(2000,2000,-1500,-1500)
#     time.sleep(.2)

# def stopMotor():
#     PWM.setMotorModel(0,0,0,0)
#     time.sleep(.5)

# def lookStraight():
#     print("WARNING NOT YET IMPLEMENTED")

# def lookRight():
#     print("WARNING NOT YET IMPLEMENTED")

# def lookLeft():
#     print("WARNING NOT YET IMPLEMENTED")
        
def startBuzzer():
    buzzer.run('1')

def stopBuzzer():
    buzzer.run('0')

#test()
drive()
