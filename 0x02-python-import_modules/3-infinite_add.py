#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    if len(sys.argv) == 1:
        print(int(0))
    numbers = len(sys.argv)
    add = 0
    for i in range(1, numbers):
        add = add + int(sys.argv[i])
    print(add)
