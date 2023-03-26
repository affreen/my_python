"""
   Practice Python Constructors. Exe-01
"""

class Country(object):
    def __init__(self, country_name, population):
        self.country_name = country_name
        self.population = population
        self.display() # the method gets automatically called while the object is created due to python constructor.
        return None

    def display(self):
        print(f"Country name is: {self.country_name}\nPopulation is: {self.population}")
        return None

c1 = Country("India", 3330000)

