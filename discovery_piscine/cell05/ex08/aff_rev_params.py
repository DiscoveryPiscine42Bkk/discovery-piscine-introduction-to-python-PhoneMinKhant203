#!/usr/bin/python3
import sys

n = len(sys.argv)
while n != 1:
    print(sys.argv[n-1])
    n -= 1