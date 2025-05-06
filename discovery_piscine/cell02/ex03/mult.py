#!/usr/bin/python3
fn = input("Enter the first number: ")
x = int(fn)
sn = input("Enter the second number: ")
y = int(sn)

result = x*y

print(fn + " x " + sn + " = " + str(result))
if result > 0:
    print("The result is positive")
elif result < 0:
    print("The result is negative")
else:
    print("The result is zero")
