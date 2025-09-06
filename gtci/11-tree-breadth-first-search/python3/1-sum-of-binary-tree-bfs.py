from collections import deque


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sum_of_binary_tree(self, root):
        if root is None:
            return 0

        sum = 0

        queue = deque()
        queue.append(root)

        while queue:
            node = queue.popleft()

            sum += node.val

            if node.left is not None:
                queue.append(node.left)

            if node.right is not None:
                queue.append(node.right)

        return sum


if __name__ == "__main__":
    sol = Solution()

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    assert sol.sum_of_binary_tree(root) == 6

    root = TreeNode(4)
    root.left = TreeNode(9)
    root.right = TreeNode(7)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(6)
    assert sol.sum_of_binary_tree(root) == 28

    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(3)
    root.left.left = TreeNode(7)
    root.right.right = TreeNode(9)
    assert sol.sum_of_binary_tree(root) == 34

    print("All test cases passed.")
