def smallest_window_containing_substring(string, substring):
    substring_char_freqs = {}

    # go through the substring and get all the frequencies of chars
    for char in substring:
        if char not in substring_char_freqs:
            substring_char_freqs[char] = 0
        substring_char_freqs[char] += 1

    min_length = len(string) + 1
    substring_start = 0

    n_matched_chars = 0

    window_start = 0
    for window_end in range(len(string)):
        rightmost_char = string[window_end]

        if rightmost_char in substring_char_freqs:
            # decrement its frequency
            substring_char_freqs[rightmost_char] -= 1

            # we've now matched one of the chars in the substring
            # there could be redundant matching chars, so only increment n_matched_chars for
            #   non-redundant chars
            if substring_char_freqs[rightmost_char] >= 0:
                n_matched_chars += 1

        # while we have all the chars matched in our window, try to shrink the window
        while n_matched_chars == len(substring):
            # check if we need to update min_length
            curr_substring_length = window_end - window_start + 1
            if min_length > curr_substring_length:
                min_length = curr_substring_length
                substring_start = window_start

            leftmost_char = string[window_start]

            if leftmost_char in substring_char_freqs:
                # if we're removing a non-redundant matching char, decrement n_matched_chars
                if substring_char_freqs[leftmost_char] == 0:
                    n_matched_chars -= 1

                substring_char_freqs[leftmost_char] += 1

            window_start += 1

    return (
        ""
        if min_length > len(string)
        else string[substring_start : substring_start + min_length]
    )


def main():
    print(smallest_window_containing_substring("aabdec", "abc"))
    print(smallest_window_containing_substring("aabdec", "abac"))
    print(smallest_window_containing_substring("abdbca", "abc"))
    print(smallest_window_containing_substring("adcad", "abc"))


main()
