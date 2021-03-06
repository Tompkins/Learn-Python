# -*- coding:utf-8 -*-
# Filename: person.py

class Person:
    """
    Create and process person records
    """
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay
        
    def lastName(self):
        return self.name.split()[-1]

    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))

    def __str__(self):
        return '[Person: job = %s, name = %s, pay = %s]' % \
               (self.job,self.name, self.pay)

class Manager(Person):
    """
    A customized Person with special requirements
    """
    def __init__(self, name, pay):
        Person.__init__(self, name, 'mgr', pay)
        
    def giveRaise(self, percent, bonus=0.1):
        Person.giveRaise(self, percent + bonus)     # good: argument original

    
if __name__ == '__main__':
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job='dev', pay=10000)
    print(bob)
    print(sue)
    print(bob.lastName(), sue.lastName())
    sue.giveRaise(.10)
    print(sue)
    tom = Manager('Tom Jones', 50000)
    tom.giveRaise(0.1)
    print(tom.lastName())
    print(tom)
    # print('--All three--')
    # for object in (bob, sue, tom):
    #     object.giveRaise(0.1)
    #     print(object)
    # Aggregate embedded objects into a computer
    """
    class Department:
        def __init__(self, *args):
            self.members = list(args)

        def addMember(self, person):
            self.members.append(person)

        def giveRaise(self, percent):
            for person in self.members:
                person.giveRaise(percent)

        def showAll(self):
            for person in self.members:
                print(person)

    development = Department(bob, sue)       # Embed object in a composite
    development.addMember(tom)
    development.giveRaise(.10)               # run embedded objects' giveRaise
    development.showAll()                    # Runs embedded objects' __str__
    """
