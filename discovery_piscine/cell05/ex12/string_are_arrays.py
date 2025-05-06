import sys

n = len(sys.argv)
if n == 1:
    print("None")
else:
    i = 1
    x = 0
    while i < n:
        count = sys.argv[i].count('z')
        print('z' *count)
        if count == 0:
            print("none")
        i +=1     
