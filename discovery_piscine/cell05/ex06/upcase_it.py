#!/usr/bin/python3
import sys

n = len(sys.argv)

if n > 1 and n < 3:
    print(sys.argv[1].upper())
elif n == 1:
    print("None")
else:
    print("None")