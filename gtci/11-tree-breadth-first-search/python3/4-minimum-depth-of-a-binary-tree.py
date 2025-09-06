from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    def findDepth(self, root):
        if root is None:
            return 0

        queue = deque()
        queue.append((root, 1))

        while queue:
            node, depth = queue.popleft()

            if node.left is None and node.right is None:
                return depth

            if node.left is not None:
                queue.append((node.left, depth + 1))

            if node.right is not None:
                queue.append((node.right, depth + 1))

        return 0


if __name__ == "__main__":
    sol = Solution()

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    assert sol.findDepth(root) == 2

    root = TreeNode(4)
    root.left = TreeNode(9)
    root.right = TreeNode(7)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(6)
    assert sol.findDepth(root) == 2

    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(3)
    root.left.left = TreeNode(7)
    root.right.right = TreeNode(9)
    assert sol.findDepth(root) == 3

    print("All test cases passed.")
