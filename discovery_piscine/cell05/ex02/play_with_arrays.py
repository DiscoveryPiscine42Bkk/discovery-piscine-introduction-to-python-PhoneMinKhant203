#!/usr/bin/python3
array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result =[]
for x in array:
    if x > 5:
        result.append(x)
print("Original Array: ", array)    
print("New Array: ", result)