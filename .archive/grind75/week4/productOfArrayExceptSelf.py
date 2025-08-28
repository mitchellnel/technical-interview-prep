from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1 for _ in range(len(nums))]

        prefix_product = 1
        suffix_product = 1

        for i in range(len(nums)):
            ans[i] *= prefix_product
            prefix_product *= nums[i]

            ans[-1 - i] *= suffix_product
            suffix_product *= nums[-1 - i]

        return ans


def main():
    soln = Solution()

    print(f"[1,2,3,4] --> {soln.productExceptSelf([1,2,3,4])}")
    print(f"[-1,1,0,-3,3] --> {soln.productExceptSelf([-1,1,0,-3,3])}")


main()
