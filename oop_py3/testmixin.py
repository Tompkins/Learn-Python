# -*- coding:utf-8 -*-
# File testmixin.py

from lister import *                # Get lister tool classes

class Super:
    def __init__(self):             # Superclass.__init__
        self.data1 = 'spam'         # Creat instance attrs
    def ham(self):
        pass

class Sub(Super, ListInherited):     # Mix in ham and s __str__
    def __init__(self):             # listers have access to self
        Super.__init__(self)
        self.data2 = 'eggs'         # More instance attrs
        self.data3 = 42
    def spam(self):                 # Define another method here
        pass

if __name__ == '__main__':
    X = Sub()
    print(X)                        # Run mixed-in __str__
