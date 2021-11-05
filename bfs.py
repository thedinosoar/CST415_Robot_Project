from MoveNode import *
from Robot import *

def drive(): 
    moveHistory = MoveStack()
    
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
                continue
            elif currentNode.get_current_direction() == "R":
                lookRight()
                if get_distance() > 25:
                    turnRight()
                    moveForward(.2, 1000)
                    moveHistory.push(currentNode)
                    moveHistory.push(MoveNode(1, "R"))
                    moveHistory.push(MoveNode(.2, "F"))
                else:
                    moveHistory.push(currentNode)
            elif currentNode.get_current_direction() == "F":
                lookForward()
                if get_distance() > 15:
                    moveForward(.2, 1000)
                    moveHistory.push(currentNode)
                    moveHistory.push(MoveNode(.2, "F"))
                else:
                    moveHistory.push(currentNode)
            elif currentNode.get_current_direction()== "L":
                lookLeft()
                if get_distance() > 25:
                    turnLeft()
                    moveForward(.2, 1000)
                    moveHistory.push(currentNode)
                    moveHistory.push(MoveNode(1, "L"))
                    moveHistory.push(MoveNode(.2, "F"))
                else:
                    moveHistory.push(currentNode)
                

    except KeyboardInterrupt:
        PWM.setMotorModel(0,0,0,0)
        print ("\nEnd of program")

