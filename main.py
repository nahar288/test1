
def reverse(text):
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    return text[::-1]


def vowels(text):
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    total = 0
    for char in text.lower():
        if char in "aeiou":
            total += 1
    return total


def words(text):
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    return len(text.split())

