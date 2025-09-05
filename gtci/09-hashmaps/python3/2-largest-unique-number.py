from typing import List


class Solution:
    def largestUniqueNumber(self, A: List[int]) -> int:
        freq_map = {}

        for num in A:
            if num not in freq_map:
                freq_map[num] = 0
            freq_map[num] += 1

        max_unique = -1
        for num in A:
            if freq_map[num] == 1:
                max_unique = max(max_unique, num)

        return max_unique


if __name__ == "__main__":
    sol = Solution()

    assert sol.largestUniqueNumber([5, 7, 3, 9, 4, 9, 8, 3, 2, 5]) == 8
    assert sol.largestUniqueNumber([1, 2, 3, 4, 5]) == 5
    assert sol.largestUniqueNumber([1, 1, 1, 1]) == -1

    print("All test cases passed.")
