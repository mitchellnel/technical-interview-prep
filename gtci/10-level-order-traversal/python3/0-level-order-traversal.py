from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getLevelOrder(self, root):
        if root is None:
            return []

        traversal = []

        queue = deque()
        queue.append(root)

        while queue:
            level_size = len(queue)

            for _ in range(level_size):
                node = queue.popleft()
                traversal.append(node.val)

                if node.left is not None:
                    queue.append(node.left)

                if node.right is not None:
                    queue.append(node.right)

        return traversal


if __name__ == "__main__":
    sol = Solution()

    root = TreeNode(4, TreeNode(5, TreeNode(5), TreeNode(7)), TreeNode(10))
    assert sol.getLevelOrder(root) == [4, 5, 10, 5, 7]

    root = TreeNode(9)
    assert sol.getLevelOrder(root) == [9]

    print("All test cases passed.")
