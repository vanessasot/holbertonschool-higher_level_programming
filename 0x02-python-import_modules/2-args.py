#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    if len(sys.argv) == 1:
        print("0 arguments.")
    if len(sys.argv) == 2:
        print((len(sys.argv)-1), "argument:")
    if len(sys.argv) > 2:
        print((len(sys.argv)-1), "arguments:")
    args = len(sys.argv)
    for i in range(1, args):
        print("{}: {}".format(i, str(sys.argv[i])))
