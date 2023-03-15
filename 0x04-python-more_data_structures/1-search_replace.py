#!/usr/bin/python3
def search_replace(my_list, search, replacer):
    new_list = []
    for itm in my_list:
        if itm == search:
            new_list.append(replacer)
        else:
            new_list.append(itm)
    return new_list
