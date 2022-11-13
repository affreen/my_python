'''
 Demo init method of the class.
'''


class Computer(object):
    def __init__(self, cpu, memory):
        self.cpu = cpu
        self.memory = memory
        self.display_config()
        return None

    def display_config(self):
        print(f'CPU is {self.cpu} and memory is {self.memory}')
        return None


c1 = Computer('Core i7', '8GB')
c2 = Computer('Core i5', '32GB')
