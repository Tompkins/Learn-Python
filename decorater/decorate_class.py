def tracer(func):
    calls = 0
    def onCall(*args, **kwargs):
        nonlocal calls
        calls += 1
        print('call %s to %s' % (calls, func.__name__))
        return func(*args, **kwargs)
    return onCall

# applied to simple function
@tracer
def spam(a, b , c):
    print(a + b + c)

spam(1, 2, 3)
spam(a=4, b=5, c=6)

# applied to class method function too!

class Person:
    def __init__(self, name, pay):
        self.name = name
        self.pay = pay

    @tracer
    def giveRaise(self, percent):       # giveRaise = tracer(giveRaise)
        self.pay *= (1.0 + percent)

    @tracer
    def lastName(self):             # lastName = tracer(lastName)
        return self.name.split()[-1]

if __name__ == '__main__':
    print('methods...')
    bob = Person('Bob Smith', 50000)
    sue = Person('Sue Jones', 100000)
    print(bob.name, sue.name)
    sue.giveRaise(.10)
    print(sue.pay)
    print(bob.lastName(), sue.lastName())   
