def smallest_subarray_with_greater_sum(sum, array):
    min_subarray_size = float("inf")

    window_sum = 0
    window_start = 0
    for window_end in range(len(array)):
        # add the next element
        window_sum += array[window_end]

        # shrink the window as small as possible until the window_sum is smaller than sum
        while window_sum >= sum:
            # update the smallest size if necessary
            curr_subarray_size = window_end - window_start + 1
            min_subarray_size = min(min_subarray_size, curr_subarray_size)

            # shrink the window
            window_sum -= array[window_start]
            window_start += 1

    return min_subarray_size if min_subarray_size != float("inf") else 0


def main():
    print(
        "Smallest subarray length: "
        + str(smallest_subarray_with_greater_sum(7, [2, 1, 5, 2, 3, 2]))
    )
    print(
        "Smallest subarray length: "
        + str(smallest_subarray_with_greater_sum(7, [2, 1, 5, 2, 8]))
    )
    print(
        "Smallest subarray length: "
        + str(smallest_subarray_with_greater_sum(8, [3, 4, 1, 1, 6]))
    )


main()
