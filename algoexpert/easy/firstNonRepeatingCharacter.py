# O(n) time | O(1) space
def firstNonRepeatingCharacter(string):
    char_counts = {}

    for char in string:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1

    for char in char_counts:
        if char_counts[char] == 1:
            return string.index(char)

    return -1
