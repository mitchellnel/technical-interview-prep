class Solution:
    def findNumbers(self, nums):
        i = 0
        while i < len(nums):
            correct_position = nums[i] - 1
            if nums[i] != nums[correct_position]:
                nums[i], nums[correct_position] = nums[correct_position], nums[i]
            else:
                i += 1

        for i in range(len(nums)):
            if i + 1 != nums[i]:
                return [nums[i], i + 1]

        return [-1, -1]


if __name__ == "__main__":
    sol = Solution()

    assert sol.findNumbers([3, 1, 2, 5, 2]) == [2, 4]
    assert sol.findNumbers([3, 1, 2, 3, 6, 4]) == [3, 5]

    print("All test cases passed.")
