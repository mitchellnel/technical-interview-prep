def minimumWindowSort(arr):
    low = 0
    high = len(arr) - 1

    # find the first number out of sorting order from the beginning of the
    #   array
    while low < len(arr) - 1 and arr[low] <= arr[low + 1]:
        low += 1

    if low == len(arr) - 1:
        # the array is already sorted
        return 0

    # find the first nubmer out of sorting order from the end of the
    #   array
    while high > 0 and arr[high] >= arr[high - 1]:
        high -= 1

    # find the maximum and minimum of the subarray
    subarray_max = float("-inf")
    subarray_min = float("inf")
    for k in range(low, high + 1):
        subarray_max = max(subarray_max, arr[k])
        subarray_min = min(subarray_min, arr[k])

    # extend the subarray to include any number bigger than the
    #   subarray min
    while low > 0 and arr[low - 1] > subarray_min:
        low -= 1

    # extend the subarray to include any number smaller than the
    #   subarray max
    while high < len(arr) - 1 and arr[high + 1] < subarray_max:
        high += 1

    return high - low + 1


def main():
    print(minimumWindowSort([1, 2, 5, 3, 7, 10, 9, 12]))
    print(minimumWindowSort([1, 3, 2, 0, -1, 7, 10]))
    print(minimumWindowSort([1, 2, 3]))
    print(minimumWindowSort([3, 2, 1]))


main()
