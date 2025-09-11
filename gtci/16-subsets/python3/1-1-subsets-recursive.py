class Solution:
    def find_subsets(self, nums):
        subsets = []

        def backtrack(start, path):
            # add the current subset to the result
            subsets.append(path[:])  # syntactic sugar for new_path = [] + path

            # try including each remaining number
            for i in range(start, len(nums)):
                path.append(nums[i])  # include nums[i] in the path
                backtrack(i + 1, path)  # recurse
                path.pop()  # pop nums[i] from the path to consider other paths

        backtrack(0, [])
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
