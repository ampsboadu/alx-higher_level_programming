#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary == None:
        return None
    else:
        #get first key
        key1 = next(iter(a_dictionary))
        max = 0
        for key, value in a_dictionary.items():
            if value > max:
                max = value
                key1 = key
        return key1
