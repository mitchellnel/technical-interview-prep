def longest_binary_string_with_k_replacements(array, k):
    max_length = 0

    char_freqs = {}
    max_ones_count = 0

    window_start = 0
    for window_end in range(len(array)):
        if array[window_end] == 1:
            max_ones_count += 1

        # current window size if from window_start to window_end
        # overall, we have 1 repeating max_ones_count times
        # this means that we can have a window that has 1 repeating max_ones_count times, and the
        #   remaining 0s we should replace
        # if the remaining number of 0s is more than k, it is time to shrink the window as we are
        #   not allowed to replace more than k 0s
        if window_end - window_start + 1 - max_ones_count > k:
            if array[window_start] == 1:
                max_ones_count -= 1
            window_start += 1

        curr_string_length = window_end - window_start + 1
        max_length = max(max_length, curr_string_length)

    return max_length


def main():
    print(
        longest_binary_string_with_k_replacements([0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], 2)
    )
    print(
        longest_binary_string_with_k_replacements(
            [0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], 3
        )
    )


main()
