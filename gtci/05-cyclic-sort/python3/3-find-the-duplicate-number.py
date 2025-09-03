class Solution:
    def findNumber(self, nums):
        i = 0
        while i < len(nums):
            correct_position = nums[i] - 1
            if nums[i] != nums[correct_position]:
                nums[i], nums[correct_position] = nums[correct_position], nums[i]
            else:
                i += 1

        for i in range(len(nums)):
            if i + 1 != nums[i]:
                return nums[i]

        return -1

    def find_number_alternate_soln(self, nums):
        i = 0
        while i < len(nums):
            if nums[i] != i + 1:
                correct_position = nums[i] - 1

                # if we are swapping the same number, then it's a duplicate
                if nums[i] != nums[correct_position]:
                    nums[i], nums[correct_position] = nums[correct_position], nums[i]
                else:
                    return nums[i]
            else:
                i += 1

        return -1


if __name__ == "__main__":
    sol = Solution()

    assert sol.findNumber([1, 4, 4, 3, 2]) == 4
    assert sol.findNumber([2, 1, 3, 3, 5, 4]) == 3
    assert sol.findNumber([2, 4, 1, 4, 4]) == 4

    print("All test cases passed.")
