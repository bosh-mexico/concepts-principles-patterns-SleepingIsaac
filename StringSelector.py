def stringFilter(*strings):
    return [string for string in strings if string.lower().startswith('m')]

stringList = stringFilter("Bosch", "Mexico", "Mango", "Mark", "Blr", "Clean code")
print(stringList)
