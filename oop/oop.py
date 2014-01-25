# -*- coding:utf-8 -*-
class Island():
    """Island
    n X n grid where zero value indicates an unoccupied cell."""
    def __init__(self, n, prey_cnt=0, predator_cnt=0):
        """Initialize cell to all 0's, then fill with animals
        """
        print n, prey_cnt, predator_cnt
        self.grid_size = n
        self.grid = []
        for i in range(n):
            row = [0]*n         # row is a list of n zeros
            self.grid.append(row)
        # self.init_animals(prey_cnt, predator_cnt)

    def size(self):
        """Return size of the island: one dimension.
        """
        return self.grid_size
    
    def register(self, animal):
        """Register animal with island, i.e. put it at the 
        animal's coordinates
        """
        x = animal.x
        y = animal.y
        
        self.grid[x][y] = animal

    def __str__(self):
        '''String representation for printing.
        (0,0) will be in the lower-left corner.
        '''
        s = ''
        for j in range(self.grid_size-1, -1, -1):   # print row size-1 first
            for i in range(self.grid_size):         # each row starts at 0
                if not self.grid[i][j]:
                    # print a '.' for an empty space
                    s += "%-2s" % '.' + " "
                else:
                    s += "%-2s" % (str(self.grid[i][j])) + " "
            s += "\n"
        return s

class Animal(object):
    def __init__(self, island, x = 0, y = 0, s="A"):
        """Initialize the animal's and their positions
        """
        self.island = island
        self.name = s
        self.x = x
        self.y = y

    def position(self):
        """Return coordinate of current position"""
        return self.x, self.y

    def __str__(self):
        return self.name
