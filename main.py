
def reverse(text):
    

    return text[::-1]


def vowels(text):
    
    total = 0
    for char in text.lower():
        if char in "aeiou":
            total += 1
    return total


def words(text):
    
    return len(text.split())
