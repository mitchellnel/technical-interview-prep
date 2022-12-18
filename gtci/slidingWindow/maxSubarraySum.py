def max_subarray_sum(k, array):
    max_sum = float("-inf")

    curr_sum = 0
    window_start = 0
    for window_end in range(len(array)):
        curr_sum += array[window_end]

        if window_end - window_start + 1 == k:
            # update max_sum if necessary
            max_sum = max(max_sum, curr_sum)

            # slide the window
            curr_sum -= array[window_start]
            window_start += 1

    return max_sum


def main():
    print(
        "Maximum sum of a subarray of size K: "
        + str(max_subarray_sum(3, [2, 1, 5, 1, 3, 2]))
    )
    print(
        "Maximum sum of a subarray of size K: "
        + str(max_subarray_sum(2, [2, 3, 4, 1, 5]))
    )


main()
