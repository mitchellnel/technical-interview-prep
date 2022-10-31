# O(n) time | O(1) space
def findThreeLargestNumbers(array):
    largest_three = [None for _ in list(range(0, 3))]

    for num in array:
        if largest_three[0] is None or num > largest_three[0]:
            findThreeLargestHelper(largest_three, num)

    return largest_three


def findThreeLargestHelper(largest_three, new_largest):
    i = 2

    elem_to_insert = new_largest

    while i >= 0:
        if largest_three[i] is None:
            largest_three[i] = elem_to_insert
            break

        elif elem_to_insert > largest_three[i]:
            temp = largest_three[i]
            largest_three[i] = elem_to_insert
            elem_to_insert = temp

        i -= 1
