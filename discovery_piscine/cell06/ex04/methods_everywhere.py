#!/usr/bin/python3

import sys

class methods:
    def shrink(self, word):
        show_word = word[:8]
        print(show_word)

    def enlarge(slef, word):
        x = len(word)
        y = 8 - x
        Z = 'Z'
        z = word+Z*y
        print(z)

    
object = methods()
n = len(sys.argv)
if n == 1:
    print("None")
else:
    i = 1
    while i < n:
        word = sys.argv[i]
        if len(word) > 8:
            object.shrink(word)
            
        elif len(word) < 8:
            object.enlarge(word)
            
        else:
            print(sys.argv[i])
        i += 1
         


    
            
