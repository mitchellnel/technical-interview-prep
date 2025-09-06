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

        zigzag = False
        while queue:
            level_size = len(queue)

            level = deque()
            for _ in range(level_size):
                node = queue.popleft()

                if zigzag:
                    level.appendleft(node.val)
                else:
                    level.append(node.val)

                if node.left is not None:
                    queue.append(node.left)

                if node.right is not None:
                    queue.append(node.right)

            traversal.append(list(level))
            zigzag = not zigzag

        return traversal


if __name__ == "__main__":
    sol = Solution()

    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    assert sol.traverse(root) == [[12], [1, 7], [9, 10, 5]]

    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    assert sol.traverse(root) == [[3], [20, 9], [15, 7]]

    print("All test cases passed.")
