
from MoveNode import *
from Motor import *  
from Ultrasonic import *
from servo import *
from Robot import *
from Buzzer import *
from Server import *
# buzzer = Buzzer()
# PWM = Motor()
# servoPWM = Servo()
# ultrasonic = Ultrasonic()

distanceTolerance = 25
camera = PiCamera()

def reverseNode(currentNode, moveHistory):
    rNode = currentNode.reverse()
    if rNode.get_direction() == "B":
        moveBackward(rNode.distance)
    elif rNode.get_direction() == "R":
        turnRight(1.27)
    elif rNode.get_direction() == "L":
        turnLeft(1.27)
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
            stopBot()
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
                    checks = sweepView()
                    if checks == 1:
                        print("RIGHT")
                        camera.start_preview()
                        sleep(5)
                        camera.capture('/home/right.jpg')
                        camera.stop_preview()
                        # moveForward(.8)
                        # stopBot()
                        # turnRight(1.27)
                        # moveForward(0.8)
                        # moveHistory.push(currentNode)
                        # moveHistory.push(MoveNode(.8, "F"))
                        # moveHistory.push(MoveNode(1, "R"))
                        # print("RIGHT TURN")
                        # moveHistory.push(MoveNode(.8, "F"))
                    elif checks == 2:
                        print("LEFT")
                    elif checks == 3:
                        print("CENTER")
                # if get_distance() > 35:
                #     moveForward(.8)
                #     stopBot()
                #     turnRight(1.27)
                #     moveForward(.8)
                #     moveHistory.push(currentNode)
                #     moveHistory.push(MoveNode(.8, "F"))
                #     moveHistory.push(MoveNode(1, "R"))
                #     print("RIGHT TURN")
                #     moveHistory.push(MoveNode(.8, "F"))
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
                    turnLeft(1.27)
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
drive(MoveStack())