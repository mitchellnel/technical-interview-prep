class Solution:
    def binary_search(self, nums, target):
        if not nums:
            return -1

        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1

        return -1


if __name__ == "__main__":
    sol = Solution()

    assert sol.binary_search([1, 2, 3, 4, 5], 3) == 2
    assert sol.binary_search([1, 2, 3, 4, 5], 6) == -1
    assert sol.binary_search([], 1) == -1
    assert sol.binary_search([1], 1) == 0
    assert sol.binary_search([1], 0) == -1

    print("All test cases passed.")
