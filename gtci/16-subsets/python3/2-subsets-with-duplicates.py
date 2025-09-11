class Solution:
    def findSubsets(self, nums):
        nums.sort()

        subsets = [[]]
        start_idx = 0

        for i, num in enumerate(nums):
            if i > 0 and nums[i - 1] == nums[i]:
                s = start_idx
            else:
                s = 0

            n_subsets = len(subsets)
            while s < n_subsets:
                new_subset = subsets[s] + [num]
                subsets.append(new_subset)

                s += 1

            start_idx = s

        return subsets


if __name__ == "__main__":
    sol = Solution()

    assert sol.findSubsets([1, 3]) == [[], [1], [3], [1, 3]]
    assert sol.findSubsets([1, 5, 3]) == [
        [],
        [1],
        [3],
        [1, 3],
        [5],
        [1, 5],
        [3, 5],
        [1, 3, 5],
    ]
    assert sol.findSubsets([1, 5, 3, 3]) == [
        [],
        [1],
        [3],
        [1, 3],
        [3, 3],
        [1, 3, 3],
        [5],
        [1, 5],
        [3, 5],
        [1, 3, 5],
        [3, 3, 5],
        [1, 3, 3, 5],
    ]

    print("All test cases passed.")
