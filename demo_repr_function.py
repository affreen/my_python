'''
 Demo repr function.
'''


class Car(object):
    def __init__(self, name, mileage):
        self.name = name
        self.mileage = mileage
    def __repr__(self):
        return "name: {}, mileage: {}".format(self.name, self.mileage)

c = Car("Tesla", 270)
print(c)