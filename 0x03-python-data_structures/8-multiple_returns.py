#!/usr/bin/python3
def multiple_returns(sentence):
    """returns a tuple with length of string & its first character"""
    n = len(sentence)
    if n == 0:
        return (0, None)
    return (n, sentence[0])
