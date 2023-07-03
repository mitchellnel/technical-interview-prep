from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        result = []
        for left in range(0, len(nums) - 2):
            # avoid duplicates
            if left > 0 and nums[left] == nums[left - 1]:
                continue

            mid = left + 1
            right = len(nums) - 1
            while mid < right:
                curr_sum = nums[left] + nums[mid] + nums[right]

                if curr_sum < 0:
                    mid += 1
                elif curr_sum > 0:
                    right -= 1
                else:
                    result.append([nums[left], nums[mid], nums[right]])

                    # avoid mid duplicates
                    while mid < right and nums[mid] == nums[mid + 1]:
                        mid += 1

                    # avoid right duplicates
                    while mid < right and nums[right] == nums[right - 1]:
                        right -= 1

                    mid += 1
                    right -= 1

        return result


def main():
    soln = Solution()

    print(f"nums [-1,0,1,2,-1,-4] --> {soln.threeSum([-1,0,1,2,-1,-4])}")
    print(f"nums [0,1,1] --> {soln.threeSum([0,1,1])}")
    print(f"nums [0,0,0] --> {soln.threeSum([0,0,0])}")


main()
