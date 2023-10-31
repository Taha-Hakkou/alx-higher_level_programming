#!/usr/bin/python3
def uppercase(str):
    for char in str:
        if ord(char) in range(ord('a'),ord('z')+1):
            char = chr(ord(char) + ord('A') - ord('a'))
        print(f"{char}",end="")
    print()

