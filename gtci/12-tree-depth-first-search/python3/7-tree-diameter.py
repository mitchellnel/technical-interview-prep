class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findDiameter(self, root):
        if root is None:
            return 0

        self.diameter = 0
        self.longestPath(root)

        return self.diameter

    def longestPath(self, root):
        if root is None:
            return 0

        longest_left_path = self.longestPath(root.left)
        longest_right_path = self.longestPath(root.right)

        self.diameter = max(self.diameter, longest_left_path + longest_right_path + 1)

        return max(longest_left_path, longest_right_path) + 1


if __name__ == "__main__":
    sol = Solution()

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(6)
    assert sol.findDiameter(root) == 5

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(6)
    root.right.left.left = TreeNode(7)
    root.right.right.right = TreeNode(8)
    root.right.left.left.left = TreeNode(9)
    root.right.right.right.left = TreeNode(10)
    root.right.right.right.left.left = TreeNode(11)
    assert sol.findDiameter(root) == 8

    print("All test cases passed.")
