from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Kadane's Algorithm
        for i in range(1, len(nums)):
            if nums[i - 1] > 0:
                nums[i] += nums[i - 1]

        return max(nums)


def main():
    soln = Solution()

    print(
        f"Maximum subarray sum in [-2,1,-3,4,-1,2,1,-5,4] is {soln.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])}"
    )
    print(f"Maximum subarray sum in [1] is {soln.maxSubArray([1])}")
    print(f"Maximum subarray sum in [5,4,-1,7,8] is {soln.maxSubArray([5,4,-1,7,8])}")


main()
