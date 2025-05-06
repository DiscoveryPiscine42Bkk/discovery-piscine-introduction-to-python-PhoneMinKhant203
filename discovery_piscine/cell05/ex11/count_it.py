#!/usr/bin/python3
import sys

n = len(sys.argv)
if n == 1:
    print("None")
else:
    i = 1
    while i < n:
        print(sys.argv[i],":", len(sys.argv[i]))
        i += 1