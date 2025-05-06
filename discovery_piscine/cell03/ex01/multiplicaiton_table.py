#!/usr/bin/python3
number = int(input("Enter a number: "))
if number > 0:
    x = 0
    while x < 10:
        print(str(x) + " x " + str(number) + " = " + str(x*number))
        x += 1
else:
    print("Error")

