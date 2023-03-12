#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    new_list = []
    if idx < 0:
        return my_list
    else:
        i = 0
        while i < len(my_list):
            if not i == idx:
                new_list.append(my_list[i])
            i += 1

    return new_list
