class Solution:
    def __init__(self):
        self.memo = {}

    def countTrees(self, n):
        if n in self.memo:
            return self.memo[n]

        if n <= 1:
            return 1

        count = 0

        for root_val in range(1, n + 1):
            left_subtree_count = self.countTrees(root_val - 1)
            right_subtree_count = self.countTrees(n - root_val)

            count += left_subtree_count * right_subtree_count

        self.memo[n] = count
        return count


if __name__ == "__main__":
    sol = Solution()

    assert sol.countTrees(2) == 2
    assert sol.countTrees(3) == 5

    print("All test cases passed.")
