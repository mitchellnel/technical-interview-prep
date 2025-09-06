from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # Method to find the maximum width of the binary tree
    def widthOfBinaryTree(self, root):
        if root is None:
            return 0

        max_width = 0

        queue = deque()
        queue.append((root, 0))

        while queue:
            level_size = len(queue)

            leftmost_index = None
            rightmost_index = None
            for i in range(level_size):
                (node, index) = queue.popleft()

                if i == 0:
                    leftmost_index = index
                if i == level_size - 1:
                    rightmost_index = index

                if node.left is not None:
                    queue.append((node.left, 2 * index))

                if node.right is not None:
                    queue.append((node.right, 2 * index + 1))

            max_width = max(max_width, rightmost_index - leftmost_index + 1)

        return max_width


if __name__ == "__main__":
    sol = Solution()

    # Test case 1
    root1 = TreeNode(1)
    root1.left = TreeNode(3)
    root1.right = TreeNode(2)
    root1.left.left = TreeNode(5)
    root1.left.right = TreeNode(3)
    root1.right.right = TreeNode(9)
    assert sol.widthOfBinaryTree(root1) == 4

    # Test case 2
    root2 = TreeNode(1)
    root2.left = TreeNode(3)
    root2.right = TreeNode(2)
    root2.left.left = TreeNode(5)
    root2.left.right = TreeNode(3)
    assert sol.widthOfBinaryTree(root2) == 2

    # Test case 3
    root3 = TreeNode(1)
    root3.left = TreeNode(3)
    root3.left.left = TreeNode(5)
    assert sol.widthOfBinaryTree(root3) == 1

    print("All test cases passed.")
