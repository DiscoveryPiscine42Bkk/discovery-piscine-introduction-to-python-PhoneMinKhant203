#!/usr/bin/python3

class note:
    def find_the_redheads(self, family):
        for x,y in family.items():
            if y == "red":
                final_list.append(x)
            else:
                continue
        print(final_list)

final_list = []

dupont_family = {
    "florian": "red",
    "marie": "blond",
    "virginie": "brunette",
    "david": "red",
    "franck": "red"
}

object = note()
object.find_the_redheads(dupont_family)




