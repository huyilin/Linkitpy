__author__ = 'Yilin'


class A:
    def __init__(self):
        self.h = 'hello'
        print self.h
        h = 5
        self.test = h
        h = 6
        print self.test


b = A()


