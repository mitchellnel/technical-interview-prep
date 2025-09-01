class Solution:
    def findLength(self, str1, k):
        max_length = 0

        window_start = 0
        majority_letter_freq = 0
        chars = {}
        for window_end in range(len(str1)):
            window_size = window_end - window_start + 1

            if str1[window_end] not in chars:
                chars[str1[window_end]] = 0
            chars[str1[window_end]] += 1

            majority_letter_freq = max(majority_letter_freq, chars[str1[window_end]])

            if window_size - majority_letter_freq <= k:
                max_length = max(max_length, window_size)

            while window_size - majority_letter_freq > k:
                chars[str1[window_start]] -= 1
                if chars[str1[window_start]] == 0:
                    del chars[str1[window_start]]

                window_start += 1
                window_size = window_end - window_start + 1

        return max_length


if __name__ == "__main__":
    sol = Solution()
    assert sol.findLength("aabccbb", 2) == 5
    assert sol.findLength("abbcb", 1) == 4
    assert sol.findLength("abccde", 1) == 3

    print("All test cases passed.")
