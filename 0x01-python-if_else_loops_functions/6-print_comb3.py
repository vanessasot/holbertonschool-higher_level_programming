#!/usr/bin/python3
for i in range(9):
    for j in range(10):
        if i < j and i != 8:
            print("{:1d}{:1d}, ".format(i, j), end="")
        if i == 8 and j == 9:
            print("{:1d}{:1d}".format(i, j))
