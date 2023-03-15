#!/usr/bin/python3
def uniq_add(my_list=[]):
    buf = []
    sum = 0
    for i in my_list:
        if i not in buf:
            sum += i
            buf.append(i)
    return sum
