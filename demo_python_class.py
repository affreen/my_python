'''
 Create a simple class.
 Create 2 objects and call the function inside the class.
'''


class Computer(object):
    def config(self, cpu, memory):
        self.cpu = cpu
        self.memory = memory
        self.display_config()
        return None

    def display_config(self):
        print(f'CPU is {self.cpu} and memory is {self.memory}')
        return None


c1 = Computer()
c2 = Computer()
c1.config('i7', '64GB')
c2.config('i5', '32GB')