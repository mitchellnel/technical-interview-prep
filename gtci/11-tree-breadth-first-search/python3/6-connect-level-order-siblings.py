from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = self.right = self.next = None


class Solution:
    def connect(self, root):
        if root is None:
            return None

        queue = deque()
        queue.append(root)

        while queue:
            level_size = len(queue)

            for i in range(level_size):
                node = queue.popleft()

                if i != level_size - 1:
                    node.next = queue[0]
                else:
                    node.next = None

                if node.left is not None:
                    queue.append(node.left)

                if node.right is not None:
                    queue.append(node.right)

        return root


if __name__ == "__main__":
    sol = Solution()

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    sol.connect(root)
    assert root.next is None
    assert root.left.next == root.right
    assert root.right.next is None
    assert root.left.left.next == root.left.right
    assert root.left.right.next == root.right.left
    assert root.right.left.next == root.right.right
    assert root.right.right.next is None

    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    sol.connect(root)
    assert root.next is None
    assert root.left.next == root.right
    assert root.right.next is None
    assert root.left.left.next == root.right.left
    assert root.right.left.next == root.right.right
    assert root.right.right.next is None

    print("All test cases passed.")
