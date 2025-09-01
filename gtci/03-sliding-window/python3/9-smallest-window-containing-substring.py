class Solution:
    def findSubstring(self, str1, pattern):
        smallest_substring_size = float("inf")
        smallest_substring_indices = []

        pattern_chars = self.construct_freq_map_from_string(pattern)

        window_start = 0
        chars = {}
        for window_end in range(len(str1)):
            window_size = window_end - window_start + 1

            if str1[window_end] not in chars:
                chars[str1[window_end]] = 0
            chars[str1[window_end]] += 1

            while self.is_submap(pattern_chars, chars):
                if smallest_substring_size > window_size:
                    smallest_substring_size = window_size
                    smallest_substring_indices = [window_start, window_end]

                chars[str1[window_start]] -= 1

                window_start += 1
                window_size = window_end - window_start + 1

        return (
            str1[smallest_substring_indices[0] : smallest_substring_indices[1] + 1]
            if smallest_substring_indices != []
            else ""
        )

    def construct_freq_map_from_string(self, s):
        chars = {}
        for char in s:
            if char not in chars:
                chars[char] = 0
            chars[char] += 1

        return chars

    def is_submap(self, small, big):
        return all(key in big and big[key] >= val for key, val in small.items())


if __name__ == "__main__":
    sol = Solution()

    assert sol.findSubstring("aabdec", "abc") == "abdec"
    assert sol.findSubstring("aabdec", "abac") == "aabdec"
    assert sol.findSubstring("abdbca", "abc") == "bca"
    assert sol.findSubstring("adcad", "abc") == ""

    print("All test cases passed.")
