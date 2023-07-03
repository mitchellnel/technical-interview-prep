class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_length = 0
        seen = {}

        window_start = 0
        for window_end in range(len(s)):
            char = s[window_end]
            if char not in seen:
                longest_length = max(longest_length, window_end - window_start + 1)
            else:
                if seen[char] < window_start:
                    longest_length = max(longest_length, window_end - window_start + 1)
                else:
                    window_start = seen[char] + 1

            seen[char] = window_end

        return longest_length


def main():
    soln = Solution()

    print(
        f'Longest substring without repeating characters in "abcabcbb" is {soln.lengthOfLongestSubstring("abcabcbb")}'
    )
    print(
        f'Longest substring without repeating characters in "bbbbb" is {soln.lengthOfLongestSubstring("bbbbb")}'
    )
    print(
        f'Longest substring without repeating characters in "pwwkew" is {soln.lengthOfLongestSubstring("pwwkew")}'
    )


main()
