class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq_map = {}
        for char in s:
            if char not in freq_map:
                freq_map[char] = 0
            freq_map[char] += 1

        length = 0
        at_least_one_odd_char = False
        for char, count in freq_map.items():
            if count % 2 == 0:
                length += count
            else:
                length += count - 1
                at_least_one_odd_char = True

        return length if not at_least_one_odd_char else length + 1


if __name__ == "__main__":
    sol = Solution()

    assert sol.longestPalindrome("abccccdd") == 7
    assert sol.longestPalindrome("a") == 1
    assert sol.longestPalindrome("bb") == 2
    assert sol.longestPalindrome("ccc") == 3
    assert sol.longestPalindrome("abcd") == 1

    print("All test cases passed.")
