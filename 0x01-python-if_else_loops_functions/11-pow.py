#!/usr/bin/python3
def pow(a, b):
    pow = 1
    if b >= 0:
        for i in range(b):
            pow = pow * a
    else:
        for i in range(-b):
            pow = pow / a
    return (pow)
