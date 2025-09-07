from collections import defaultdict


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countPaths(self, root, S):
        prefix_sum_counts = defaultdict(int)
        prefix_sum_counts[0] = 1

        def dfs(node, curr_sum):
            if node is None:
                return 0

            curr_sum += node.val

            count = prefix_sum_counts[curr_sum - S]  # valid paths ending here

            prefix_sum_counts[curr_sum] += 1

            count += dfs(node.left, curr_sum)
            count += dfs(node.right, curr_sum)

            prefix_sum_counts[curr_sum] -= 1  # backtrack

            return count

        return dfs(root, 0)


if __name__ == "__main__":
    sol = Solution()

    root = TreeNode(1)
    root.left = TreeNode(7)
    root.right = TreeNode(9)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(2)
    root.right.right = TreeNode(3)
    assert sol.countPaths(root, 12) == 3

    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    assert sol.countPaths(root, 11) == 2

    root = TreeNode(4)
    root.left = TreeNode(4)
    root.right = TreeNode(4)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(4)
    root.left.left.left = TreeNode(4)
    root.left.left.right = TreeNode(4)
    root.left.right.left = TreeNode(4)
    root.left.right.right = TreeNode(4)
    assert sol.countPaths(root, 8) == 10

    print("All test cases passed.")
