def longest_substring_with_replacement(string, k):
    max_length = 0

    char_freqs = {}
    max_repeat_letter_count = 0

    window_start = 0
    for window_end in range(len(string)):
        rightmost_char = string[window_end]
        if rightmost_char not in char_freqs:
            char_freqs[rightmost_char] = 0
        char_freqs[rightmost_char] += 1

        max_repeat_letter_count = max(
            max_repeat_letter_count, char_freqs[rightmost_char]
        )

        # current window size if from window_start to window_end
        # overall, we have a letter that is repeating max_repeat_letter_count times
        # this means that we can have a window that has one letter repeating
        #   max_repeat_letter_count times, and the remaining letters we should replace
        # if the remaining letters are more than k, it is time to shrink the window as we are not
        #   allowed to replace more than k letters
        if window_end - window_start + 1 - max_repeat_letter_count > k:
            leftmost_char = string[window_start]
            char_freqs[leftmost_char] -= 1
            window_start += 1

        curr_substring_length = window_end - window_start + 1
        max_length = max(max_length, curr_substring_length)

    return max_length


def main():
    print(longest_substring_with_replacement("aabccbb", 2))
    print(longest_substring_with_replacement("abbcb", 1))
    print(longest_substring_with_replacement("abccde", 1))


main()
