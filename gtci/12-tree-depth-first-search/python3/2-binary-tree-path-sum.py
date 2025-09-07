class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPath(self, root, sum):
        if root is None:
            return False

        if root.left is None and root.right is None:
            return root.val == sum

        return self.hasPath(root.left, sum - root.val) or self.hasPath(
            root.right, sum - root.val
        )


if __name__ == "__main__":
    sol = Solution()

    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    assert sol.hasPath(root, 23)
    assert not sol.hasPath(root, 16)

    print("All test cases passed.")
