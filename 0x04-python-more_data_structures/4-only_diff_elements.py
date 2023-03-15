#!/usr/bin/python3
def only_diff_elements(set1, set2):
    found = []
    diff = []
    for itm in set1:
        if itm in set2:
            found.append(itm)
    all_elements = set1.union(set2)
    for itm in all_elements:
        if itm not in found:
            diff.append(itm)
    return diff
