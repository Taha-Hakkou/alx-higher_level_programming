#!/usr/bin/python3
if __name__ == "__main__":
    """print sum of infinite number of args"""
    import sys

    sum = 0
    for i in range(1,len(sys.argv)):
        sum += int(sys.argv[i])
    print("{:d}".format(sum))
