# O(n^2) time | O(1) space
def insertionSort(array):
    for i in range(1, len(array)):
        j = i
        while j > 0 and array[j] < array[j - 1]:
            temp = array[j]
            array[j] = array[j - 1]
            array[j - 1] = temp

            j -= 1

    return array
