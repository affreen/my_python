'''
 Python script to demo static variables and instance variables.
'''

class Car:
    wheels = 4 # Static variable
    def __init__(self):
        self.mileage = 10 # Instance variable
        self.model = 'BMW' # Instance variable

c1 = Car()
c2 = Car()

print(c1.model, c1.mileage, c1.wheels)
print(c2.model, c2.mileage, c2.wheels)

print('Changing the value of the static variable wheels to 5 !')

Car.wheels = 5

print(c1.model, c1.mileage, c1.wheels)
print(c2.model, c2.mileage, c2.wheels)
