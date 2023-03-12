#!/usr/bin/env python3
def no_c(my_string):
    i = len(my_string) - 1
    while i >= 0:
        if (my_string[i] == 'C') or (my_string[i] == 'c'):
            my_string = my_string[:i] + my_string[i + 1:]
        i -= 1
    return my_string
