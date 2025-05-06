#!/usr/bin/python3
import re
import sys


n = len(sys.argv)
if n == 1 or n > 3:
    print("None")
else:
    result = re.findall(sys.argv[1], sys.argv[2])
    print(len(result))