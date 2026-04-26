#!/usr/bin/python3

def uppercase(s):
    for char in s:
        if ord('a') <= ord(char) <= ord('z'):
            char = chr(ord(char) - ord('a') + ord('A'))
        print(char, end="")
    print()
