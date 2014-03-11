class Adder:
    def add(self, x, y):
        print('Not implemented')

class ListAdder(Adder):
    def add(self, x, y):
        for i in y:
            x.append(i)
        print(x)

class DictAdder(Adder):
    def add(self, x, y):
        for keys in y:
            if keys in x:
                pass
            else:
                x[keys] = y[keys]
        print(x)
        
if __name__ == '__main__':
    A = ListAdder()
    A.add([1, 2, 3], [4, 5, 6, 7, 8])
    B = DictAdder()
    B.add({1:'2'}, {1:'3', 2:'4'})
        
