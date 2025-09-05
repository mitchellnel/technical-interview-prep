class Solution:
    def firstUniqueChar(self, s: str) -> int:
        freq_map = {}

        for idx, char in enumerate(s):
            if char not in freq_map:
                freq_map[char] = 0
            freq_map[char] += 1

        for idx, char in enumerate(s):
            if freq_map[char] == 1:
                return idx

        return -1


if __name__ == "__main__":
    sol = Solution()

    assert sol.firstUniqueChar("leetcode") == 0
    assert sol.firstUniqueChar("abcab") == 2
    assert sol.firstUniqueChar("abab") == -1

    print("All test cases passed.")
