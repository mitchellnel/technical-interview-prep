class Solution:
    def find_subsets(self, nums):
        """
        O(N * 2^N) time

        Every time we consider a number in the input array, we double the number of subsets
        by adding the number to all existing subsets.
        """
        subsets = [[]]

        for num in nums:
            n_subsets = len(subsets)
            for i in range(n_subsets):
                new_subset = subsets[i] + [num]
                subsets.append(new_subset)

        return subsets


if __name__ == "__main__":
    sol = Solution()

    assert sol.find_subsets([1, 3]) == [[], [1], [3], [1, 3]]
    assert sol.find_subsets([1, 5, 3]) == [
        [],
        [1],
        [5],
        [1, 5],
        [3],
        [1, 3],
        [5, 3],
        [1, 5, 3],
    ]

    print("All test cases passed.")
