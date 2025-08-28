def removeKeyInPlace(arr, key):
    if not arr:
        return 0

    curr, next_insertion_idx = 0, 0

    while curr != len(arr):
        if arr[curr] != key:
            arr[next_insertion_idx] = arr[curr]
            next_insertion_idx += 1

        curr += 1

    return next_insertion_idx


def main():
    print("Array new length: " + str(removeKeyInPlace([3, 2, 3, 6, 3, 10, 9, 3], 3)))
    print("Array new length: " + str(removeKeyInPlace([2, 11, 2, 2, 1], 2)))


main()
