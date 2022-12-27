'''
 Python script to demo inner class in OOPs.
'''

# this would become the outer class
class Student:

    def __init__(self, name, id):
        self.name = name
        self.id = id

    def show_student_details(self):
        print(self.name, self.id)


    # create an inner class with init method

    class Device:

        def __init__(self, model, cpu, ram):
            self.model = model
            self.cpu = cpu
            self.ram = ram

        def show_device_details(self):
            print(self.model, self.cpu, self.ram)



s1 = Student('Affreen', '10')
print('Calling the outer class object....')
s1.show_student_details()

d1 = s1.Device('HPE', 'i5', '32 GB')
print('Calling the inner class object....')
d1.show_device_details()

d2 = Student('Affreen', '10').Device('Dell', 'i7', '16 GB')
d2.show_device_details()