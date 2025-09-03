class Solution:
    def findNumbers(self, nums):
        duplicateNumbers = []

        i = 0
        while i < len(nums):
            correct_position = nums[i] - 1

            if nums[i] != nums[correct_position]:
                nums[i], nums[correct_position] = nums[correct_position], nums[i]
            else:
                i += 1

        for i in range(len(nums)):
            if i + 1 != nums[i]:
                duplicateNumbers.append(nums[i])

        return duplicateNumbers


if __name__ == "__main__":
    sol = Solution()

    assert sol.findNumbers([3, 4, 4, 5, 5]) == [4, 5]
    assert sol.findNumbers([5, 4, 7, 2, 3, 5, 3]) == [3, 5]

    print("All test cases passed.")
