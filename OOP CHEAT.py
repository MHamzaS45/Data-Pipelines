#construction_example.py


class Car:
    weels = 4 # same for all cars as a default

'''
These attributes live on the class, not the object

Use constructor (__init__) for instance-specific data. They are unique per object

Examples:
- Car color
- max speed
- current car
- registration number 
'''

class Car:
    weels = 4 

    def __init__(self, color, max_speed):
        self.color = color 
        self.max_speed = max_speed
        self.current_speed = 0

'''
Every time you create a new object, constructor (__init__) runs and gives the specific object and its attributes

Why not put the object-specific attributes in the root? Because attributes in the root are shared unless overwritten

For example: 
'''

class Person:
    hobbies = [] # shared list

p1 = Person()
p2 = Person()

p1.hobbies.append("Football")
p1.hobbies.append("Reading")
p2.hobbies.append("Making music")
print(p2.hobbies)
 
'''
If the list was inside __init__, each would have its own list

The following is a correct example:
'''

class Student:
    hobbies2 = [] # shared list

    def __init__(self):
        self.hobbies2 = [] #  list will be unique per object

s1 = Student()
s2 = Student()

s1.hobbies2.append("Football")
s1.hobbies2.append("Reading")
s2.hobbies2.append("Making music")
s2.hobbies2.append("Cooking")
print(s1.hobbies2) # s1 has its own list
print(s2.hobbies2) # now s2 has its own list