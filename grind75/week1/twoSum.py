from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        subtractions_to_reach_target = {}

        for idx, num in enumerate(nums):
            subtraction = target - num

            if subtraction not in subtractions_to_reach_target:
                subtractions_to_reach_target[num] = idx
            else:
                return [idx, subtractions_to_reach_target[subtraction]]


def main():
    soln = Solution()
    print(f"nums: [2,7,11,15]; target: 9")
    print("\t" + str(soln.twoSum([2, 7, 11, 15], 9)))

    print(f"nums: [3,2,4]; target: 6")
    print("\t" + str(soln.twoSum([3, 2, 4], 6)))

    print(f"nums: [3,3]; target: 6")
    print("\t" + str(soln.twoSum([3, 3], 6)))


main()
