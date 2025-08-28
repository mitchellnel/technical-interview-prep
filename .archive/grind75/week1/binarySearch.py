from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

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

    print("Find 9 in [-1,0,3,5,9,12]")
    print(soln.search([-1, 0, 3, 5, 9, 12], 9))

    print("Find 2 in [-1,0,3,5,9,12]")
    print(soln.search([-1, 0, 3, 5, 9, 12], 2))


main()
