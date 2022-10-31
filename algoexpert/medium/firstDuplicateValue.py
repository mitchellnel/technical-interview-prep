# O(n) time | O(1) space
def firstDuplicateValue(array):
    appearances = {}

    for num in array:
        if num in appearances:
            return num
        else:
            appearances[num] = 1

    return -1
