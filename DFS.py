
from MoveNode import *
from Motor import *  
from Ultrasonic import *
from servo import *
from Robot import *
from Buzzer import *
buzzer=Buzzer()       
PWM = Motor() 
servoPWM = Servo()
ultrasonic = Ultrasonic()

distanceTolerance = 25

def reverseNode(currentNode, moveHistory):
    rNode = currentNode.reverse()
    if rNode.get_direction() == "B":
        moveBackward(rNode.distance)
    elif rNode.get_direction() == "R":
        turnRight()
    elif rNode.get_direction() == "L":
        turnLeft()
        lookStraight()
        if get_distance() > 25:
            moveForward(1)
            moveHistory.push(MoveNode(1, "F"))

    if moveHistory.peek().get_direction() == "R" or moveHistory.peek().get_direction() == "L":
        reverseNode(moveHistory.pop(), moveHistory)


def drive(moveHistory):  
    
    try:
        end_found = False

        while end_found == False:
            stopMotor()
            lookForward()
            currentNode = moveHistory.pop()
            currentNode.print()
            if currentNode == None:
                break
            currentNode.incrementDirection()
            if currentNode.get_current_direction() == "POP":
                print("POP")
                reverseNode(currentNode,moveHistory)
                continue
            elif currentNode.get_current_direction() == "R":
                lookRight()
                if get_distance() > 35:
                    moveForward(.8)
                    stopMotor()
                    turnRight(.8)
                    moveForward(.8)
                    moveHistory.push(currentNode)
                    moveHistory.push(MoveNode(.8, "F"))
                    moveHistory.push(MoveNode(1, "R"))
                    print("RIGHT TURN")
                    moveHistory.push(MoveNode(.8, "F"))
                else:
                    moveHistory.push(currentNode)
            elif currentNode.get_current_direction() == "F":
                lookForward()
                if get_distance() > 15:
                    moveForward(.5)
                    moveHistory.push(currentNode)
                    moveHistory.push(MoveNode(.5, "F"))
                else:
                    moveHistory.push(currentNode)
            elif currentNode.get_current_direction()== "L":
                lookLeft()
                if get_distance() > 35:
                    turnLeft(.8)
                    moveForward(.8)
                    
                    moveHistory.push(currentNode)
                    moveHistory.push(MoveNode(1, "L"))
                    print("LEFT TURN")
                    moveHistory.push(MoveNode(.2, "F"))
                else:
                    moveHistory.push(currentNode)
                

    except KeyboardInterrupt:
        PWM.setMotorModel(0,0,0,0)
        print ("\nEnd of program")

#40 because distance thing, lazy for now
#5 to fail distance test

# def get_distance():
#     dist = ultrasonic.get_distance()
#     time.sleep(.25)
#     return dist
#
# def sweepView():
#     servoPWM.setServoPwm('0', -30)
#     leftDistance = ultrasonic.get_distance()
#     time.sleep(.25)
#     servoPWM.setServoPwm('0', 60)
#     centerDistance = ultrasonic.get_distance()
#     time.sleep(.25)
#     servoPWM.setServoPwm('0', 160)
#     rightDistance = ultrasonic.get_distance()
#     if rightDistance > distanceTolerance and leftDistance > distanceTolerance and centerDistance > distanceTolerance:
#         return distanceTolerance + 1
#
#     return 5
#
# def moveForward(distance):
#     PWM.setMotorModel(500,500,500,500)
#     time.sleep(distance)
#
# def moveBackward(distance):
#     PWM.setMotorModel(-500,-500,-500,-500)
#     time.sleep(distance)
#
# def turnLeft():
#     PWM.setMotorModel(-1500,-1500,2000,2000)
#     time.sleep(.8)
#
# def turnRight():
#     PWM.setMotorModel(2000,2000,-1500,-1500)
#     time.sleep(.8)
#
# def stopMotor():
#     PWM.setMotorModel(0,0,0,0)
#     time.sleep(.5)
#
# def lookStraight():
#     servoPWM.setServoPwm('0', 60)
#     time.sleep(.25)
#
# def lookRight():
#     servoPWM.setServoPwm('0', 120)
#     servoPWM.setServoPwm('1', 40)
#     time.sleep(.25)
#
# def lookLeft():
#     servoPWM.setServoPwm('0', 0)
#     time.sleep(.25)
#
# def startBuzzer():
#     buzzer.run('1')
#
# def stopBuzzer():
#     buzzer.run('0')

#test()
drive(MoveStack())


