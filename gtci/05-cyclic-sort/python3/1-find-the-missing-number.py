class Solution:
    def findMissingNumber(self, nums):
        i = 0
        while i < len(nums):
            num = nums[i]

            if num < len(nums) and num != i:
                nums[i], nums[num] = nums[num], nums[i]
            else:
                i += 1

        for i in range(len(nums)):
            if i != nums[i]:
                return i

        return len(nums)


if __name__ == "__main__":
    sol = Solution()

    assert sol.findMissingNumber([3, 0, 1]) == 2
    assert sol.findMissingNumber([0, 1]) == 2
    assert sol.findMissingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]) == 8

    print("All test cases passed.")
