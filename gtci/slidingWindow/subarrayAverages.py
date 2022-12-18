def subarray_averages(k, array):
    soln = []

    window_start = 0
    window_sum = 0

    for window_end in range(len(array)):
        # add the next element
        window_sum += array[window_end]

        # if the window is of size 5, we need to slide the window
        if window_end - window_start + 1 == k:
            # get the average of the window
            soln.append(window_sum / k)

            # remove first element of the subarray
            window_sum -= array[window_start]

            # move the start of the window, thereby "sliding" it
            window_start += 1

    return soln


def main():
    result = subarray_averages(5, [1, 3, 2, 6, -1, 4, 1, 8, 2])
    print("Averages of subarrays of size K: " + str(result))


main()
