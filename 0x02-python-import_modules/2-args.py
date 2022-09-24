#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = len(sys.argv) - 1
    if (argv == 0):
        print("0 argument.")
    else:
        print("{} argument:".format(argv))
        for n in range(1, argv + 1):
            print("{}: {}".format(n, sys.argv[n]))
