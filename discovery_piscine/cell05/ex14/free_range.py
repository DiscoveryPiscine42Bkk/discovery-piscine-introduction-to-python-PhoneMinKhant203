import sys

n = len(sys.argv)
if n == 1:
    print("None")
else:
    i = 1
    result = []
    for x in range(int(sys.argv[i]),int(sys.argv[n-1])):
        result.append(x)
    result.append(int(sys.argv[n-1]))
    print(result)

