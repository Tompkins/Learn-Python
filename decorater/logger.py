# -*- coding:utf-8 -*-
# 利用装饰器获得函数运行信息
import time
from functools import wraps

def logger(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        ts = time.time()
        result = fn(*args, **kwargs)
        te = time.time()
        print("function      = {0}".format(fn.__name__))
        print("    arguments = {0}{1}".format(args, kwargs))
        print("    return    = {0}".format(result))
        print("    time      = %.6f sec" % (te-ts))
        return result
    return wrapper

if __name__ == '__main__':
    @logger
    def multipy(x, y):
        return x * y

    @logger
    def sum_num(n):
        s = 0
        for i in range(n+1):
            s += i
        return s

    print(multipy(50000, 500000))
    print(sum_num(100000))
    print(sum_num(1000000))
