#!/usr/bin/python3
x = int(input("Give me the first number: "))
y = int(input("Give me the second number: "))
print("Thank you!")


print(x, "+", y, "=", "{}".format(x + y))
print(x, "-", y, "=", "{}".format(x - y))
print(x, "*", y, "=", "{}".format(x * y))

if y == 0:
    print("Error")
else:
    print(x, "/", y, "=", "{:.2f}".format(x / y))
