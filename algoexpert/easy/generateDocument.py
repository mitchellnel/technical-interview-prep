# O(n+m) time | O(c) space
def generateDocument(characters, document):
    available_chars = {}

    for char in characters:
        if char in available_chars:
            available_chars[char] += 1
        else:
            available_chars[char] = 1

    for char in document:
        if char not in available_chars:
            return False
        elif available_chars[char] == 0:
            return False
        else:
            available_chars[char] -= 1
    return True
