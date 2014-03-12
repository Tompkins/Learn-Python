class Adder:
    def __init__(self, data = []):
        self.data = data
    def add(self, other):
        print('Not implemented')
    def __add__(self, other):
        return self.add(other)
    
class ListAdder(Adder):
    def add(self, y):
        return self.data + y
    
class DictAdder(Adder):
    def add(self, other):
        new = {}
        for k in self.data.keys(): new[k] = self.data[k]
        for k in other.keys(): new[k] = other[k]
        return new
        

    
    
        
