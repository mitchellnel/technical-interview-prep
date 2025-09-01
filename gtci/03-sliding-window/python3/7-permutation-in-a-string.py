class Solution:
    def findPermutation(self, str1, pattern):
        pattern_chars = self.construct_freq_map_from_string(pattern)

        chars = {}
        max_window_size = len(pattern)

        window_start = 0
        for window_end in range(len(str1)):
            window_size = window_end - window_start + 1

            if str1[window_end] not in chars:
                chars[str1[window_end]] = 0
            chars[str1[window_end]] += 1

            if window_size > max_window_size:
                chars[str1[window_start]] -= 1
                if chars[str1[window_start]] == 0:
                    del chars[str1[window_start]]

                window_start += 1
                window_size = window_end - window_start + 1

            if chars == pattern_chars:
                return True

        return False

    def construct_freq_map_from_string(self, s):
        chars = {}

        for char in s:
            if char not in chars:
                chars[char] = 0
            chars[char] += 1

        return chars


if __name__ == "__main__":
    sol = Solution()

    assert sol.findPermutation("oidbcaf", "abc") == True
    assert sol.findPermutation("odicf", "dc") == False
    assert sol.findPermutation("bcdxabcdy", "bcdyabcdx") == True
    assert sol.findPermutation("aaacb", "abc") == True

    print("All test cases passed.")
