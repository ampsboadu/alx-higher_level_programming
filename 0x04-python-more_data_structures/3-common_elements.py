#!/usr/bin/python3
def common_elements(set1, set2):
    found = []
    for itm in set1:
        if itm in set2:
            found.append(itm)
    return found
