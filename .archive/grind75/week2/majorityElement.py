from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = 0
        counter = 0

        for num in nums:
            if counter == 0:
                candidate = num

            if num == candidate:
                counter += 1
            else:
                counter -= 1

        return candidate


def main():
    soln = Solution()

    print(f"Majority element in [3,2,3] is {soln.majorityElement([3,2,3])}")
    print(
        f"Majority element in [2,2,1,1,1,2,2] is {soln.majorityElement([2,2,1,1,1,2,2])}"
    )


main()
