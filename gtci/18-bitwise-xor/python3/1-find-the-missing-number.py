class Solution:
    def find_missing_number(self, nums):
        n = len(nums) + 1

        x1 = nums[0]
        for i in range(1, len(nums)):
            x1 ^= nums[i]

        x2 = 1
        for i in range(2, n + 1):
            x2 ^= i

        return x1 ^ x2


if __name__ == "__main__":
    sol = Solution()

    nums1 = [1, 5, 2, 6, 4]
    assert sol.find_missing_number(nums1) == 3

    nums2 = [1, 3]
    assert sol.find_missing_number(nums2) == 2

    nums3 = [10, 6, 4, 2, 3, 5, 7, 8, 1]
    assert sol.find_missing_number(nums3) == 9

    print("All test cases passed.")
