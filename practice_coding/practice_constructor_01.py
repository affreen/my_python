"""
   Practice Python Constructors. Exe-01.
"""

class People(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.display() # the method gets automatically called while the object is created due to python constructor.
        return None

    def display(self):
        print(f"my name is {self.name} and my age is {self.age}")
        return None

p1 = People("Affreen", 38)

