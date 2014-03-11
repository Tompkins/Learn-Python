class Adder:
    def __init__(self, data):
        self.data = data
    def add(self, y):
        print('Not implemented')
    def __add__(self, y):
        return self.add(y)

class ListAdder(Adder):
    def add(self, y):
        for i in y:
            self.data.append(i)
        print(self.data)

class DictAdder(Adder):
    def add(self, y):
        for keys in y:
            if keys in self.data:
                pass
            else:
                self.data[keys] = y[keys]
        print(self.data)
        
if __name__ == '__main__':
    A = ListAdder([1, 2, 3])
    A.add([4, 5, 6, 7, 8])
    A + [9]
    B = DictAdder({1:'2'})
    B.add({1:'3', 2:'4'})
    B + {3:'3'}
        
