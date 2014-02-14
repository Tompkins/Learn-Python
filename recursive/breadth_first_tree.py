# -*- coding:utf-8 -*-

# Breadth-first tree

from turtle import *

def branch(length, level):
    if level <= 0:          
        return
    forward(length)
    left(45)
    branch(0.6*length, level-1)
    right(90)
    branch(0.6*length, level-1)
    left(45)
    backward(length)
    return

if __name__ == '__main__':
    left(90)
    branch(100, 5)
    
