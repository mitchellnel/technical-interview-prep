from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    def findLevelAverages(self, root):
        if root is None:
            return []

        result = []

        queue = deque()
        queue.append(root)

        while queue:
            level_size = len(queue)

            level_sum = 0
            for _ in range(level_size):
                node = queue.popleft()

                level_sum += node.val

                if node.left is not None:
                    queue.append(node.left)

                if node.right is not None:
                    queue.append(node.right)

            result.append(level_sum / level_size)

        return result


if __name__ == "__main__":
    sol = Solution()

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    assert sol.findLevelAverages(root) == [1.0, 2.5]

    root = TreeNode(4)
    root.left = TreeNode(9)
    root.right = TreeNode(7)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(6)
    assert sol.findLevelAverages(root) == [4.0, 8.0, 4.0]

    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(3)
    root.left.left = TreeNode(7)
    root.right.right = TreeNode(9)
    assert sol.findLevelAverages(root) == [10.0, 4.0, 8.0]

    print("All test cases passed.")
