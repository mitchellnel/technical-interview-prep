class Solution:
    def findLength(self, str1, k):
        max_length = 0

        window_start = 0
        chars = {}

        for window_end in range(len(str1)):
            if str1[window_end] not in chars:
                chars[str1[window_end]] = 0
            chars[str1[window_end]] += 1

            if len(chars) == k:
                max_length = max(max_length, window_end - window_start + 1)

            # if too many chars, shrink window until len(chars) <= k
            while len(chars) > k:
                chars[str1[window_start]] -= 1

                if chars[str1[window_start]] == 0:
                    del chars[str1[window_start]]

                window_start += 1

        return max_length


if __name__ == "__main__":
    sol = Solution()
    assert sol.findLength("araaci", 2) == 4
    assert sol.findLength("araaci", 1) == 2
    assert sol.findLength("cbbebi", 3) == 5
    print("All test cases passed.")
