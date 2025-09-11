class Solution:
    def findPermutations(self, nums):
        permutations = []

        n = len(nums)

        def backtrack(start):
            if start == n:
                permutations.append(nums[:])
                return

            for i in range(start, n):
                nums[start], nums[i] = nums[i], nums[start]
                backtrack(start + 1)
                nums[start], nums[i] = nums[i], nums[start]

        backtrack(0)
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
