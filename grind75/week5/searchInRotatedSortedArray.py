from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # first find the index of the smallest element
        #   -- the is the start of the original nums array
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        # left is now the index of the smallest value, and the pivot index
        small = left

        # work out whether the target is to the left or right of small
        left = 0
        right = len(nums) - 1
        if target >= nums[small] and target <= nums[right]:
            left = small
        else:
            right = small

        # binary search to find target
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1

        return -1


def main():
    soln = Solution()

    print(f"Target 0 in [4,5,6,7,0,1,2] is at index {soln.search([4,5,6,7,0,1,2], 0)}")
    print(f"Target 3 in [4,5,6,7,0,1,2] is at index {soln.search([4,5,6,7,0,1,2], 3)}")
    print(f"Target 0 in [1] is at index {soln.search([1], 0)}")


main()
