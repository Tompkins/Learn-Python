class Iters:
    def __init__(self, value):
        self.data = value
    def __getitem__(self, i):               # Fallback for iteration
        print('get[%s]:' % i, end='')       # Also for index, slice
        return self.data[i]
    def __iter__(self):                     # Preferred for iteration
        print('iter=> ', end='')            # Allows noly active iterator
        self.ix = 0
        return self
    def __next__(self):
        print('next:', end='')
        if self.ix == len(self.data): raise StopIteration
        item = self.data[self.ix]
        self.ix += 1
        return item
    def __contains__(self, x):               # Preferred for 'in'
        print('contain: ', end='')
        return x in self.data

if __name__ == '__main__':
    x = Iters([1, 2, 3, 4, 5])              # Make instance
    print(3 in x)                           # Membership
    for i in x:                             # For loops
        print(i, end=' | ')

    print()
    print([i ** 2 for i in x])              # other iteration context
    print(list(map(bin, x)))

    I = iter(x)
    while True:
        try:
            print(next(I), end=' * ')
        except StopIteration:
            break
