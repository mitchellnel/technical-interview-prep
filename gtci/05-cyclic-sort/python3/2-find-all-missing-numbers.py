class Solution:
    def findNumbers(self, nums):
        missingNumbers = []

        i = 0
        while i < len(nums):
            correct_position = nums[i] - 1

            # is the number at index i currently in it's correct position
            # not necesarrily the actual object at i, but the number itself
            if nums[i] != nums[correct_position]:
                nums[i], nums[correct_position] = nums[correct_position], nums[i]
            else:
                i += 1

        for i in range(len(nums)):
            if i + 1 != nums[i]:
                missingNumbers.append(i + 1)

        return missingNumbers


if __name__ == "__main__":
    sol = Solution()

    assert sol.findNumbers([2, 3, 1, 8, 2, 3, 5, 1]) == [4, 6, 7]
    assert sol.findNumbers([2, 4, 1, 2]) == [3]
    assert sol.findNumbers([2, 3, 2, 1]) == [4]

    print("All test cases passed.")
