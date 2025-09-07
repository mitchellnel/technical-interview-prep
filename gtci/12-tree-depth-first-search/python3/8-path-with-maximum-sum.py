import math


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def findMaximumPathSum(self, root):
        self.globalMaximumSum = -math.inf

        self.findMaximumPathSum_helper(root)

        return self.globalMaximumSum

    def findMaximumPathSum_helper(self, node):
        if node is None:
            return 0

        # max of 0 and a positive path
        # we would not include the negative branch in our calculation of the global max sum
        max_sum_left = max(0, self.findMaximumPathSum_helper(node.left))
        max_sum_right = max(0, self.findMaximumPathSum_helper(node.right))

        self.globalMaximumSum = max(
            self.globalMaximumSum, max_sum_left + max_sum_right + node.val
        )

        return max(max_sum_left, max_sum_right) + node.val


if __name__ == "__main__":
    sol = Solution()

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    assert sol.findMaximumPathSum(root) == 6

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(6)
    assert sol.findMaximumPathSum(root) == 16

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(6)
    root.right.left.left = TreeNode(7)
    root.right.left.right = TreeNode(8)
    root.right.right.right = TreeNode(9)
    assert sol.findMaximumPathSum(root) == 31

    root = TreeNode(-1)
    root.left = TreeNode(-3)
    assert sol.findMaximumPathSum(root) == -1

    root = TreeNode(10)
    root.left = TreeNode(-5)
    root.right = TreeNode(3)
    assert sol.findMaximumPathSum(root) == 13

    print("All test cases passed.")
