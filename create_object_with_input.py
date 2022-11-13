'''
 Ask user to pass the CPU, memory and disk configs and print if the device is latest or out dated!
'''

class Computer(object):

    def __init__(self, cpu, memory, disk):
        self.cpu = cpu
        self.memory = memory
        self.disk = disk
        self.display_config()

    def display_config(self):
        if self.cpu >= 9 and self.memory >= 16 and self.disk >= 500:
            print(f'CPU found Core i{self.cpu}; memory found {self.memory}GB; disk found {self.disk}TB; This is an up to date device!')
        else:
            print(f'CPU found Core i{self.cpu} ; memory found {self.memory}GB; disk found {self.disk}TB; Upgrade your device !')


cpu_config = int(input('Enter cpu config here : '))
memory_config = int(input('Enter memory config here : '))
disk_config = int(input('Enter disk config here : '))

my_computer = Computer(cpu_config, memory_config, disk_config)
