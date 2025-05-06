#!/usr/bin/python3

class person:
    def date_of_birth(self,women_scientists):
        final_list = {}
        for x, info in women_scientists.items():
            final_list[info["name"]] = info["date_of_birth"]
        
        
        sorted_list = dict(sorted(final_list.items(), key=lambda item: item[1]))
        print(sorted_list)

        for y,z in sorted_list.items():
            print(f"{y} is a great scientist born in {z}")
            



women_scientists = {
    "ada": {"name": "Ada Lovelace", "date_of_birth": "1815"},
    "cecilia":{"name": "Cecila Payne", "date_of_birth": "1900"},
    "lise": {"name": "Lise Meitner", "date_of_birth": "1878"},
    "grace": {"name": "Grace Hopper", "date_of_birth": "1906"}
}

object = person()
object.date_of_birth(women_scientists)