class Mylist:
    times = 0
    def __init__(self, wrapped):
        self.wrapped = []
        for i in wrapped:
            self.wrapped.append(i)
    def __getitem__(self, index):
        return self.wrapped[index]
    def __add__(self, other):
        return Mylist(self.wrapped + other)
    def __iter__(self):
        return self
    def __next__(self):
        if self.times == len(self.wrapped):
            raise StopIteration
        self.times += 1
        return self.wrapped[self.times - 1]
    def append(self, i):
        return self.wrapped.append(i)
    def sort(self):
        return sorted(self.wrapped)
        
