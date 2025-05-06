#!/usr/bin/python3

class note:
    def array_of_names(self, first_name, second_name):
        full_name = first_name.capitalize() + " " + second_name.capitalize()
        persons_list.append(full_name)
            

persons_list=[]

persons = {
    "jean": "valjean",
    "grace": "hopper",
    "xavier": "niel",
    "fifi": "bridancier"
}

object = note()
for x,y in persons.items():
    object.array_of_names(x,y)

print(persons_list)



