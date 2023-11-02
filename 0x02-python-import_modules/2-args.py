#!/usr/bin/python3
if __name__ == "__main__":
    """print number & list of arguments"""
    import sys

    n = len(sys.argv) - 1
    print("{:d} argument{}".format(n, "" if n == 1 else "s"), end="")
    if n != 0:
        print(":")
        for i in range(1,n+1):
            print("{:d}: {}".format(i, sys.argv[i]))
    else:
        print(".")
