# O(n^2) time | O(1) space
def bubbleSort(array):
    swap_made = True

    while swap_made:
        swap_made = False
        for i in range(len(array)):
            if i == len(array) - 1:
                continue
            elif array[i] > array[i + 1]:
                temp = array[i]
                array[i] = array[i + 1]
                array[i + 1] = temp

                swap_made = True
    return array
