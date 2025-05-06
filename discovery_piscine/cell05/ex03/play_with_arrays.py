#!/usr/bin/python3
array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 6, 7, 8, 13]
result =[]
for x in array:
    if x > 5 and x not in result:
        result.append(x)
print("Original Array: ", array)    
print("New Array: ", result)