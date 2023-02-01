from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = []
        self.dfs(nums, [], permutations)
        return permutations

    def dfs(self, nums: List[int], curr_path: List[int], permutations: List[List[int]]):
        # base case -- we've permuted all of our nums, so nums is empty in the call
        if len(nums) == 0:
            permutations.append(curr_path)
            return

        # recursive step -- add a new number to the permutation
        for idx, num in enumerate(nums):
            # we want to exclude the current num we're iterating at
            self.dfs(nums[:idx] + nums[idx + 1 :], curr_path + [num], permutations)


def main():
    soln = Solution()

    print(f"Permutations of [1,2,3] are {soln.permute([1,2,3])}")
    print(f"Permutations of [0,1] are {soln.permute([0,1])}")
    print(f"Permutations of [1] are {soln.permute([1])}")


main()
