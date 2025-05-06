import sys

class downcase:
    def downcase_it(self):
        n = len(sys.argv)

        if n == 1:
            print("None")
        else:
            i = 1
            while i < n:
                print(sys.argv[i].lower())
                i += 1


object = downcase()
object.downcase_it()