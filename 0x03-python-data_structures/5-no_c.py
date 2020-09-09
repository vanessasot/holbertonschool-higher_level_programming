#!/usr/bin/env python3
def no_c(my_string):
    my_string1 = ""
    for i in my_string:
        if i != 'c' and i != 'C':
            my_string1 = my_string1 + i
    return my_string1
