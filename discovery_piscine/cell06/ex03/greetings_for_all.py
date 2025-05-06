import sys
import math

class greeting:
    def greeting(self, name = None , name2="Nobel Stranger"):
        if name == None:
            print("Hello, ", name2)
        elif name != None:
            try:
                x = float(name)
                print("Error! It was not a name")
            except ValueError:
                print("Hello, ", name)
        else:
            print("Error")

        


object = greeting()
object.greeting()
object.greeting("Phone")
object.greeting("Phone Min")
object.greeting(42)