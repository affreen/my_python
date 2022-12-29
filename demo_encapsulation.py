'''
 Python script to demo encapsulation in OOPs.
'''

class Person(object):
    def assigning_name_and_age(self, name, age, location):
        self.name = name
        self.age = age
        self.__location = location
        return None
    def display(self):
        print('Name of the person is {0} and age is {1} and current city residing is {2}'.format(self.name, self.age,
        self.__location))
        return None
    def __display_location(self):
        print('Location of the person is {0}'.format(self.__location))
        return None

new_person = Person()
new_person.assigning_name_and_age('Affreen', 37, 'Raleigh')
new_person.display()
print('Print individual variable value of person object ....')
print(new_person.name)
print(new_person.age)
#print(new_person.__location) # this will generate no attribute found exception due to encapulation
#new_person.__display_location() # this will generate no attribute found exception due to encapulation