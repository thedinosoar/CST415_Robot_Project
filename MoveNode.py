# Created by Kevin Ahlstrom on Oct 6 2021
# A move node keeps track of a move by mentioning distance and local direction
class MoveNode: 
    def __init__(self, distance, direction):
        self.distance = distance
        self.direction = direction
        self.next = None
        self.current_direction = ""

    def reverse(self):
        newDirection = ""
        if self.direction == "F":
            newDirection = "B"
        elif self.direction == "B":
            newDirection = "B"
        elif self.direction == "R":
            newDirection = "L"
        elif self.direction == "L":
            newDirection = "R"

        return MoveNode(self.distance, newDirection)

    def incrementDirection(self):
        if self.current_direction == "":
            self.current_direction = "R"
        elif self.current_direction == "R":
            self.current_direction = "F"
        elif self.current_direction == "F":
            self.current_direction = "L"
        elif self.current_direction == "L":
            self.current_direction = "POP"

    def print(self):
        print(str(self.distance) + " " + self.direction)

    def get_direction(self):
        return self.direction

    def get_current_direction(self):
        return self.current_direction
    
    def get_distance(self):
        return self.distance

class MoveStack:
    head: MoveNode

    def __init__(self):
        self.size = 1
        self.head = None
        start = MoveNode(0, "F")
        self.push(start)
        

    def push(self, obj):
        self.size = self.size + 1
        if self.head == None:
            self.head = obj
        else:
            obj.next = self.head
            self.head = obj
    
    def pop(self):
        if self.size == 0:
            return MoveNode(1, "E")
        if self.size == 1:
            self.head = None
            return self.head
        temp = self.head
        self.head = self.head.next

        return temp

