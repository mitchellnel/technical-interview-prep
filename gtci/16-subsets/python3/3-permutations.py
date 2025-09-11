class Solution:
    def findPermutations(self, nums):
        """
        Time: O(n * n!) -- building each permutation takes O(n) for the recursive calls, then we do this O(n!) times
        Space: O(n) -- recursive stack
        """
        permutations = []

        n = len(nums)
        used = [False] * n

        def backtrack(path):
            if len(path) == n:
                permutations.append(path[:])
                return

            for i in range(len(nums)):
                if used[i]:
                    continue

                path.append(nums[i])
                used[i] = True
                backtrack(path)
                used[i] = False
                path.pop()

        backtrack([])
        return permutations


if __name__ == "__main__":
    sol = Solution()

    assert sol.findPermutations([1, 3]) == [[1, 3], [3, 1]]
    assert set(map(tuple, sol.findPermutations([1, 5, 3]))) == set(
        [
            (1, 5, 3),
            (1, 3, 5),
            (5, 1, 3),
            (5, 3, 1),
            (3, 5, 1),
            (3, 1, 5),
        ]
    )

    print("All test cases passed.")
