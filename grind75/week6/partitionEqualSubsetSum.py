from typing import List
from functools import cache


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        @cache
        def subset_sum(curr_sum, i=0):
            if curr_sum == 0:
                return True

            if i >= len(nums) or curr_sum < 0:
                return False

            return subset_sum(curr_sum - nums[i], i + 1) or subset_sum(curr_sum, i + 1)

        total_sum = sum(nums)
        return total_sum & 1 == 0 and subset_sum(total_sum // 2)


def main():
    soln = Solution()

    print(f"[1,5,11,5] --> {soln.canPartition([1,5,11,5])}")
    print(f"[1,2,3,5] --> {soln.canPartition([1,2,3,5])}")


main()
