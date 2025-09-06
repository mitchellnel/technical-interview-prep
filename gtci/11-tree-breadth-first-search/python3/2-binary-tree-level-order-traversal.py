from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    def traverse(self, root):
        if root is None:
            return []

        traversal = []

        queue = deque()
        queue.append(root)

        while queue:
            level_size = len(queue)

            level = []
            for _ in range(level_size):
                node = queue.popleft()

                level.append(node.val)

                if node.left is not None:
                    queue.append(node.left)

                if node.right is not None:
                    queue.append(node.right)

            traversal.append(level)

        return traversal


if __name__ == "__main__":
    sol = Solution()

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    assert sol.traverse(root) == [[1], [2, 3], [4, 5, 6, 7]]

    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    assert sol.traverse(root) == [[12], [7, 1], [9, 10, 5]]

    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    assert sol.traverse(root) == [[3], [9, 20], [15, 7]]

    print("All test cases passed.")
