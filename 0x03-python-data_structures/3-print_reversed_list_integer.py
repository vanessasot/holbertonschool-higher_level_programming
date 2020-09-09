#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    my_list2 = my_list.copy()
    my_list2.reverse()
    for i in my_list2:
        print("{:d}".format(i))
