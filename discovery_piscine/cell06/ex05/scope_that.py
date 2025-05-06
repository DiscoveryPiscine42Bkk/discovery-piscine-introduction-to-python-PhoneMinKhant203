#!/usr/bin/python3

class scope:
    def add_one(self, number):
        number += 1
        print ("After Adding one", number)


number = 21
print("Original Number is", number)

object = scope()
object.add_one(number)

print("Before Adding one", number)
