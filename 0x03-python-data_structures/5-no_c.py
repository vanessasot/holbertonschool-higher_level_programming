#!/usr/bin/env python3
def no_c(my_string):
    my_string2 = my_string.translate({ord('c'): None})
    my_string2 = my_string.translate({ord('C'): None})
    return my_string2