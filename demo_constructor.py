'''
 Demo Constructor in Python!
 Every time you create an object - it will take space from the heap memory.
 Size depends on var and number of var in the object.
'''


class Computer:

    def __init__(self):
        self.cpu = 'Core i5'
        self.memory = '32GB'


c1 = Computer()
c2 = Computer()
# print(id(c1)) # address of heap memory
# print(id(c2))
c1.cpu = 'Skylake i7'  # Override the cpu for c1 object
c1.memory = '128GB'  # Override the memory for c1 object

print(f'CPU is : {c1.cpu} and RAM is : {c1.memory}')
print(f'CPU is : {c2.cpu} and RAM is : {c2.memory}')

print(id(c1)) # address of heap memory
print(id(c2))
