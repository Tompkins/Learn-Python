class SkipIterator:
    def __init__(self, wrapped):
        self.wrapped = wrapped          # Iterator state information
        self.offset = 0
    def __next__(self):
        if self.offset >= len(self.wrapped):    # Terminates Iterations
            raise StopIteration
        else:
            item = self.wrapped[self.offset]    # else return and skip
            self.offset += 2
            return item

class SkipObject:
    def __init__(self, wrapped):        # save item to be used
        self.wrapped = wrapped
    def __iter__(self):
        return SkipIterator(self.wrapped)   # New Iterator each time

if __name__ == '__main__':
    alpha = 'abcdef'
    skipper = SkipObject(alpha)         # Make container object
    I = iter(skipper)                   # Make an iterator on it
    print(next(I), next(I), next(I))    # Visit offset 0.2.3

    for x in skipper:                   # for calls __iter__ automatically
        for y in skipper:               # nested fors call __iter__ again each time
            print(x+y, end=' ')         # Each iterator has its own state. offset
