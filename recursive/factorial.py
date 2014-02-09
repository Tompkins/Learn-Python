# -*- coding:utf-8 -*-

def factorial(n):
    """Recursive factorial."""
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

if __name__ == '__main__':
    a = factorial(4)
    print a
