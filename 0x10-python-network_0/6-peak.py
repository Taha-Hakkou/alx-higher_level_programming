#!/usr/bin/python3
"""
6-peak.py
"""

def find_peak(list_of_integers):
    """ finds a peak in a list of unsorted integers """
    lint = list_of_integers
    if lint is None or lint == []:
        return (None)
    begin, end = 0, len(lint) - 1
    while begin < end:
        mid = begin + (end - begin) // 2
        if lint[mid] > lint[mid - 1] and lint[mid] > lint[mid + 1]:
            return (lint[mid])
        else:
            if lint[mid + 1] >= lint[mid - 1]:
                begin = mid + 1
            else:
                end = mid
    return (lint[begin])
