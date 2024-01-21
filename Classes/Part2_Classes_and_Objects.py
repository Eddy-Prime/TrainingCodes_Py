
# 1. Classes and Objects

    #this is for the file Classes_and_Objects.py importing the class Robot
from Classes_and_Objects import Robot

class Person:
    def __init__(self, name, personality, is_sitting ,r):
        self.name = name
        self.personality = personality
        self.is_sitting = is_sitting
        self.robot_owned = r

    def sit_down(self):
        self.is_sitting = True

    def stand_up(self):
        self.is_sitting = False    

p1 = Person("Alice", "aggressive", False)
p2 = Person("Becky", "talkative", True)

p1.robot_owned  = "Jerry"
p2.robot_owned = "Tom"

p1.robot_owned = Robot("Jerry", "blue", 40)
p2.robot_owned = Robot("Tom", "green", 30)