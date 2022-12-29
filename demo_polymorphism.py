'''
 Python script to demo polymorphism in OOPs.
'''

class Birds(object):
    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.display()

    def display(self):
        print('Bird name is : {0} ; Color of the bird is : {1}'.format(self.name, self.color))

    def location(self):
        print('Found mostly in Arctic Circle !!')

class Insects(object):
    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.display()

    def display(self):
        print('Insect name is : {0} ; Color of the insect is {1}'.format(self.name, self.color))

    def location(self):
        print('Found mostly in soil !!')

bird_1 = Birds('Blue Robin', 'blue')
bird_1.location()

insect_1 = Insects('Ant', 'black')
insect_1.location()
