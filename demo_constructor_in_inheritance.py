'''
 Python script to demo constructor and super keyword in inheritance in OOPs.
'''

class A:

    def __init__(self):
        print('Executing the init method from class A .....')
    def feature1(self):
        print('Feature 1 is working....')
    def feature2(self):
        print('Feature 2 is working....')

# class B is inheriting all the methods in class A - single level inheritance
class B(A):
    def __init__(self):
        print('Executing the init method from class B .....')
        super().__init__() # access the init method from class A
    def feature3(self):
        print('Feature 3 is working....')
    def feature4(self):
        print('Feature 4 is working....')

class P():
    def __init__(self):
        print('Executing the init method from class P .....')
    def feature11(self):
        print('Feature 11 is working....')

class Q():
    def __init__(self):
        print('Executing the init method from class Q .....')
    def feature12(self):
        print('Feature 12 is working....')

# class R is inheriting the methods from two separate super classes P and Q - due to MRO init method from P will also get executed
class R(P, Q):
    def __init__(self):
        print('Executing the init method from class R .....')
        super(R, self).__init__()
    def feature13(self):
        print('Feature 13 is working....')


b = B()
r = R()