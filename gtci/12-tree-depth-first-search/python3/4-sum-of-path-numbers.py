class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findSumOfPathNumbers(self, root):
        if root is None:
            return 0

        return self.findSumOfPathNumbers_helper(root, 0)

    def findSumOfPathNumbers_helper(self, node, current_number):
        if node is None:
            return 0

        current_number = current_number * 10 + node.val

        if node.left is None and node.right is None:
            return current_number

        return self.findSumOfPathNumbers_helper(
            node.left, current_number
        ) + self.findSumOfPathNumbers_helper(node.right, current_number)


if __name__ == "__main__":
    sol = Solution()

    root = TreeNode(1)
    root.left = TreeNode(7)
    root.right = TreeNode(9)
    root.right.left = TreeNode(2)
    root.right.right = TreeNode(9)

    assert sol.findSumOfPathNumbers(root) == 408

    root = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(1)
    root.left.left = TreeNode(1)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(5)

    assert sol.findSumOfPathNumbers(root) == 332

    print("All test cases passed.")
