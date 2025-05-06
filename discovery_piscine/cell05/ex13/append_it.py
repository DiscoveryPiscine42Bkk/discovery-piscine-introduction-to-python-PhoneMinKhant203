#!/usr/bin/python3
import sys

n = len(sys.argv)
if n == 1:
    print("None")
else:
    i = 1
    while i < n:
        if sys.argv[i].endswith('ism'):
            print(sys.argv[i])
        else:
            print(sys.argv[i]+"ism")
        i += 1

