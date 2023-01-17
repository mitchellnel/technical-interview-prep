from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        appears = set()
        for num in nums:
            if num in appears:
                return True

            appears.add(num)

        return False
