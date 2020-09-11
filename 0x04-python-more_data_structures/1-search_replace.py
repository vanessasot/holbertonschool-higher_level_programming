#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list.copy()
    j = 0
    for i in new_list:
        if i == search:
            new_list[j] = replace
        j += 1
    return new_list
