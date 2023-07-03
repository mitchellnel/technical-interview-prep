from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        combinations = []
        self.dfs(candidates, target, [], combinations)

        return combinations

    def dfs(
        self,
        candidates: List[int],
        target: int,
        curr_path: List[int],
        combinations: List[List[int]],
    ):
        # base case 1 -- exceeded target, so do not add curr_path
        if target < 0:
            return

        # base case 2 -- met target, so add curr_path
        if target == 0:
            combinations.append(curr_path)
            return

        # recursive step -- dfs on all candidates using curr_path
        for idx, num in enumerate(candidates):
            self.dfs(candidates[idx:], target - num, curr_path + [num], combinations)


def main():
    soln = Solution()

    print(f"candidates = [2,3,6,7], target = 7 --> {soln.combinationSum([2,3,6,7], 7)}")
    print(f"candidates = [2,3,5], target = 8 --> {soln.combinationSum([2,3,5], 8)}")
    print(f"candidates = [2], target = 1 --> {soln.combinationSum([2], 1)}")


main()
