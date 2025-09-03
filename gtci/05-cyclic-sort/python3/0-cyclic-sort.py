class Solution:
    def sort(self, nums):
        i = 0
        while i < len(nums):
            num = nums[i]

            if i + 1 != num:
                nums[i], nums[num - 1] = nums[num - 1], nums[i]
            else:
                i += 1

        return nums


if __name__ == "__main__":
    sol = Solution()

    assert sol.sort([3, 1, 5, 4, 2]) == [1, 2, 3, 4, 5]
    assert sol.sort([2, 6, 4, 3, 1, 5]) == [1, 2, 3, 4, 5, 6]
    assert sol.sort([1, 5, 6, 4, 3, 2]) == [1, 2, 3, 4, 5, 6]

    print("All test cases passed.")
