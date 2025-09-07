class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findPath(self, root, sequence):
        if root is None and not sequence:
            return True

        return self.findPath_helper(root, sequence, [])

    def findPath_helper(self, node, sequence, curr_path):
        if node is None:
            return False

        curr_path = curr_path + [node.val]

        if node.left is None and node.right is None:
            return curr_path == sequence

        return self.findPath_helper(
            node.left, sequence, curr_path
        ) or self.findPath_helper(node.right, sequence, curr_path)


if __name__ == "__main__":
    sol = Solution()

    root = TreeNode(1)
    root.left = TreeNode(7)
    root.right = TreeNode(9)
    root.right.left = TreeNode(2)
    root.right.right = TreeNode(9)
    assert sol.findPath(root, [1, 9, 9])

    root = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(1)
    root.left.left = TreeNode(1)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(5)
    assert not sol.findPath(root, [1, 0, 7])
    assert sol.findPath(root, [1, 1, 6])

    print("All test cases passed.")
