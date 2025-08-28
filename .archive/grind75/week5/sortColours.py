from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        low = 0
        mid = 0
        high = len(nums) - 1

        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]

                low += 1
                mid += 1
            elif nums[mid] == 2:
                nums[high], nums[mid] = nums[mid], nums[high]

                high -= 1
            else:
                mid += 1

        return nums


def main():
    soln = Solution()

    print(f"[2,0,2,1,1,0] --> {soln.sortColors([2,0,2,1,1,0])}")
    print(f"[2,0,1] --> {soln.sortColors([2,0,1])}")


main()
