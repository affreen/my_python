'''
  Python script to demo different method types used in OOPs.
'''

class Student:

    school = 'Affreen School'
    def __init__(self, marks_bio, marks_math, marks_phys):
        self.marks_bio = marks_bio
        self.marks_math = marks_math
        self.marks_phys = marks_phys

    # get the average of all the marks obtained , instance method
    def average_marks_obtained(self):  # this is an instance method - since we are passing self as argument to this method
        return (self.marks_bio + self.marks_math + self.marks_phys)/3

    # Getters are setters in OOPs - this belongs to instance method type
    def get_marks_bio(self):
        return self.marks_bio
    def set_marks_bio(self, new_bio_marks):
        self.marks_bio = new_bio_marks

    # Class method demo
    @classmethod
    def get_school_name(cls):
        return cls.school # return static var

    # Static method demo
    @staticmethod
    def get_class_details():
        print('This is a class of grade V students !')
        return None



s1 = Student(98, 100, 65)
s2 = Student(75, 95, 98)

print(s1.average_marks_obtained())
print(s2.average_marks_obtained())

print('Calling getters and setters methods')

s1.get_marks_bio()
s1.set_marks_bio(100)

print(s1.marks_bio)
print('New average score: ',s1.average_marks_obtained())

print('Calling the class methods')
print(Student.get_school_name())

print('Calling the static methods')
print(Student.get_class_details())