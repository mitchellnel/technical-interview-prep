class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def get_minimum_path_sum(self, root):
        if root is None:
            return float("inf")

        if root.left is None and root.right is None:
            return root.val

        return root.val + min(
            self.get_minimum_path_sum(root.left), self.get_minimum_path_sum(root.right)
        )


if __name__ == "__main__":
    sol = Solution()

    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(5)
    root.left.right = TreeNode(2)
    root.right.right = TreeNode(1)
    assert sol.get_minimum_path_sum(root) == 16

    print("All test cases passed.")
