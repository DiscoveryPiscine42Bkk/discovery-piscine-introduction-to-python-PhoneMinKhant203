string = input("Enter a word: ")

result = ''.join([char.lower() if char.isupper() else char.upper() for char in string])
print(result)

