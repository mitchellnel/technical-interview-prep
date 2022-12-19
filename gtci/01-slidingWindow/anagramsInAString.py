def anagrams_in_string(string, pattern):
    anagram_start_indices = []

    char_freqs = {}

    # get the frequency of chars in our pattern
    for char in pattern:
        if char not in char_freqs:
            char_freqs[char] = 0
        char_freqs[char] += 1

    n_matched_chars = 0

    # our goal is to match all the characters in char_freqs with the current window
    window_start = 0
    for window_end in range(len(string)):
        rightmost_char = string[window_end]

        if rightmost_char in char_freqs:
            # decrement its frequency
            char_freqs[rightmost_char] -= 1

            # if the frequency is now 0, we've matched 1 of the chars in the pattern
            if char_freqs[rightmost_char] == 0:
                n_matched_chars += 1

        # if we've matched all the characters our frequency map, append start of anagram to our list
        if n_matched_chars == len(char_freqs):
            anagram_start_indices.append(window_start)

        # if our window size is greater or equal to the length of the pattern, we need to shrink it
        if window_end >= len(pattern) - 1:
            leftmost_char = string[window_start]

            if leftmost_char in char_freqs:
                # if the frequency is currently 0, we're unmatching 1 of the chars in the pattern
                if char_freqs[leftmost_char] == 0:
                    n_matched_chars -= 1
                char_freqs[leftmost_char] += 1

            window_start += 1

    return anagram_start_indices


def main():
    print(anagrams_in_string("ppqp", "pq"))
    print(anagrams_in_string("abbcabc", "abc"))


main()
