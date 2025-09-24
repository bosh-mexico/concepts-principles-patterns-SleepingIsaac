from typing import Iterable, TypeVar

T = TypeVar("T", str, Iterable)

def stringFilter(letter: str, items: Iterable[T]) -> list:
    return [item for item in items if isinstance(item, str) and item.lower().startswith(letter.lower())]

# Example usage
stringList = ["Bosch", "Mexico", "Mango", "Mark", "Blr", "Clean code"]
result = stringFilter('M', stringList)
print(result)
