#!/usr/bin/python3

class student_mark:
    def average(self, class_name):
        result = 0
        for x in class_name.values():
            result += x
        final_result = result/len(class_name)
        return final_result

final_list = []

class_3B = {
    "marine": 18,
    "jean": 15,
    "coline": 8,
    "luc": 9
}

class_3C = {
    "quentine": 17,
    "julie": 15,
    "marc": 8,
    "stephanie": 13
}

object = student_mark()
print(f"Average for class #B: {object.average(class_3B)}.")
print(f"Average for class #B: {object.average(class_3C)}.")



