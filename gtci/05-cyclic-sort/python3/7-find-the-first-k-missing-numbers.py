class Solution:
    def findFirstKMissingNumbers(self, nums, k):
        missingNumbers = []

        i = 0
        while i < len(nums):
            correct_position = nums[i] - 1

            if (
                correct_position < len(nums)
                and nums[i] >= 1
                and nums[i] != nums[correct_position]
            ):
                nums[i], nums[correct_position] = nums[correct_position], nums[i]
            else:
                i += 1

        extra_numbers = set()
        for i in range(len(nums)):
            if i + 1 != nums[i]:
                missingNumbers.append(i + 1)

                if len(missingNumbers) == k:
                    return missingNumbers

                extra_numbers.add(nums[i])

        i = 1
        while len(missingNumbers) < k:
            candidate_number = i + len(nums)

            if candidate_number not in extra_numbers:
                missingNumbers.append(candidate_number)

            i += 1

        return missingNumbers


if __name__ == "__main__":
    sol = Solution()

    assert sol.findFirstKMissingNumbers([3, -1, 4, 5, 5], 3) == [1, 2, 6]
    assert sol.findFirstKMissingNumbers([2, 3, 4], 3) == [1, 5, 6]
    assert sol.findFirstKMissingNumbers([-2, -3, 4], 2) == [1, 2]

    print("All test cases passed.")
