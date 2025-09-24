def stringFilter(letter, *strings):
    return [string for string in strings if string.lower().startswith(letter.lower)]

stringList = stringFilter("m","Bosch", "Mexico", "Mango", "Mark", "Blr", "Clean code")
print(stringList)
