# O(n) time | O(1) space
def moveElementToEnd(array, toMove):
    insert_idx = len(array) - 1

    # put the insert_idx in the right location
    while insert_idx > 0 and array[insert_idx] == toMove:
        insert_idx -= 1

    for idx, num in enumerate(array):
        if num == toMove:
            temp = array[insert_idx]
            array[insert_idx] = num
            array[idx] = temp

            # put the insert_idx in the right location
            while insert_idx > 0 and array[insert_idx] == toMove:
                insert_idx -= 1

        # if they're the same, we've made all the swaps we had to make
        if idx == insert_idx:
            break

    return array
