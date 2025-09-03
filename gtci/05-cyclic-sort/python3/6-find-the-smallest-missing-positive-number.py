class Solution:
    def findNumber(self, nums):
        i = 0
        while i < len(nums):
            correct_position = nums[i] - 1

            # ignore numbers not in the range to be sorted
            if (
                correct_position < len(nums)
                and nums[i] >= 1
                and nums[i] != nums[correct_position]
            ):
                nums[i], nums[correct_position] = nums[correct_position], nums[i]
            else:
                i += 1

        # then the numbers we ignore indicate the places where we are missing the smallest positive number
        for i in range(len(nums)):
            if i + 1 != nums[i]:
                return i + 1

        return len(nums) + 1


if __name__ == "__main__":
    sol = Solution()

    assert sol.findNumber([-3, 1, 5, 4, 2]) == 3
    assert sol.findNumber([3, -2, 0, 1, 2]) == 4
    assert sol.findNumber([3, 2, 5, 1]) == 4
    assert sol.findNumber([33, 37, 5]) == 1

    print("All test cases passed.")
