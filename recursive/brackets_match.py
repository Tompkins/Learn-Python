# -*- coding:utf-8 -*-
# 匹配括号

def brackets_match(n):
    left_brackets = []
    for i in n:
        if i == '(':
            left_brackets.append(i)
        elif i == ')':
            left_brackets.pop()
    if len(left_brackets) == 0:
        return True
    else:
        return False
