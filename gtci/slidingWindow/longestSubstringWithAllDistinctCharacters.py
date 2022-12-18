def longest_substring_with_all_distinct_characters(string):
    longest_substring_length = 0

    last_index_of_char = {}

    window_start = 0
    for window_end in range(len(string)):
        curr_char = string[window_end]

        if curr_char in last_index_of_char:
            # if we've already encountered one of the curr_char, we shrink the window from the
            #   beginning so that we only have 1 occurrence of curr_char
            # in the current window, we will not have any of curr_char after its previous index
            #   if window_start is already past the last index of curr_char
            # if this is already the case, we keep window_start
            # so take the max between the two possible new window_start values
            window_start = max(window_start, last_index_of_char[curr_char] + 1)

        # update (or insert) the last index occurrence of curr_char
        last_index_of_char[curr_char] = window_end

        # update maximum length if necessary
        curr_substring_length = window_end - window_start + 1
        longest_substring_length = max(longest_substring_length, curr_substring_length)

    return longest_substring_length


def main():
    print(
        "Length of the longest substring: "
        + str(longest_substring_with_all_distinct_characters("aabccbb"))
    )
    print(
        "Length of the longest substring: "
        + str(longest_substring_with_all_distinct_characters("abbbb"))
    )
    print(
        "Length of the longest substring: "
        + str(longest_substring_with_all_distinct_characters("abccde"))
    )


main()
