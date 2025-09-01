import math


class Solution:
    def findStringAnagrams(self, str1, pattern):
        result_indices = []

        pattern_chars = self.construct_freq_map_from_string(pattern)

        chars = {}
        windowStart = 0
        for windowEnd in range(len(str1)):
            windowSize = windowEnd - windowStart + 1

            if str1[windowEnd] not in chars:
                chars[str1[windowEnd]] = 0
            chars[str1[windowEnd]] += 1

            while windowSize > len(pattern):
                chars[str1[windowStart]] -= 1
                if chars[str1[windowStart]] == 0:
                    del chars[str1[windowStart]]

                windowStart += 1
                windowSize = windowEnd - windowStart + 1

            if windowSize == len(pattern) and chars == pattern_chars:
                result_indices.append(windowStart)

        return result_indices

    def construct_freq_map_from_string(self, s):
        chars = {}
        for char in s:
            if char not in chars:
                chars[char] = 0
            chars[char] += 1

        return chars


if __name__ == "__main__":
    sol = Solution()

    assert sol.findStringAnagrams("ppqp", "pq") == [1, 2]
    assert sol.findStringAnagrams("abbcabc", "abc") == [2, 3, 4]

    print("All test cases passed.")
