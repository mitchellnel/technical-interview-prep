def longest_substring_with_k_distinct_characters(string, k):
    max_substring_length = 0

    char_frequency = {}

    window_start = 0
    for window_end in range(len(string)):
        # add the rightmost char of the substring
        rightmost_char = string[window_end]
        if rightmost_char not in char_frequency:
            char_frequency[rightmost_char] = 0
        char_frequency[rightmost_char] += 1

        # shrink the sliding window, until we are left with k distinct characters
        while len(char_frequency) > k:
            leftmost_char = string[window_start]
            char_frequency[leftmost_char] -= 1
            if char_frequency[leftmost_char] == 0:
                del char_frequency[leftmost_char]
            window_start += 1

        curr_substring_length = window_end - window_start + 1
        max_substring_length = max(max_substring_length, curr_substring_length)

    return max_substring_length


def main():
    print(
        "Length of the longest substring: "
        + str(longest_substring_with_k_distinct_characters("araaci", 2))
    )
    print(
        "Length of the longest substring: "
        + str(longest_substring_with_k_distinct_characters("araaci", 1))
    )
    print(
        "Length of the longest substring: "
        + str(longest_substring_with_k_distinct_characters("cbbebi", 3))
    )


main()
