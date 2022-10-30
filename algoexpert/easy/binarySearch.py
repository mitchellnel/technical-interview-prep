# O(log(n)) time | O(1) space
def binarySearch(array, target):
    middle = int(len(array) / 2)

    if target < array[middle]:
        while middle != -1:
            if target == array[middle]:
                return middle

            middle -= 1
    elif target > array[middle]:
        while middle != len(array):
            if target == array[middle]:
                return middle

            middle += 1

    elif target == array[middle]:
        return middle

    return -1
