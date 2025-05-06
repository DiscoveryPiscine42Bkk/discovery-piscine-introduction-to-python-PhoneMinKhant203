#!/usr/bin/python3
number = int(input("Enter a number: "))
if number <= 25:
    while number < 26:
        print("Inside the loop, my variable is " + str(number))
        number += 1
else:
    print("Error")
