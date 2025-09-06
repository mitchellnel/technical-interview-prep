from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isEvenOddTree(self, root: TreeNode) -> bool:
        if root is None:
            return True

        queue = deque()
        queue.append(root)

        level = -1
        while queue:
            level_size = len(queue)
            level += 1

            prev_node_val = None
            for _ in range(level_size):
                node = queue.popleft()

                if level % 2 == 0:
                    if node.val % 2 == 0 or (
                        prev_node_val is not None and node.val <= prev_node_val
                    ):
                        return False
                else:
                    if node.val % 2 != 0 or (
                        prev_node_val is not None and node.val >= prev_node_val
                    ):
                        return False

                if node.left is not None:
                    queue.append(node.left)

                if node.right is not None:
                    queue.append(node.right)

                prev_node_val = node.val

        return True


if __name__ == "__main__":
    sol = Solution()

    root = TreeNode(1)
    root = TreeNode(1)
    root.left = TreeNode(10)
    root.right = TreeNode(4)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(7)
    assert sol.isEvenOddTree(root) is True

    root = TreeNode(5)
    root.left = TreeNode(9)
    root.right = TreeNode(3)
    root.left.left = TreeNode(12)
    root.right.right = TreeNode(8)
    assert sol.isEvenOddTree(root) is False

    root = TreeNode(7)
    root.left = TreeNode(10)
    root.right = TreeNode(2)
    root.left.left = TreeNode(12)
    root.left.right = TreeNode(8)
    assert sol.isEvenOddTree(root) is False

    print("All test cases passed.")
