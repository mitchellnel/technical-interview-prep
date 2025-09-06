from collections import deque


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def traverse(self, root):
        if root is None:
            return []

        traversal = []

        deq = deque()
        deq.append(root)
        level_stack = []

        while deq:
            level_size = len(deq)
            level_stack.append([])

            for _ in range(level_size):
                node = deq.popleft()

                level_stack[-1].append(node.val)

                if node.left is not None:
                    deq.append(node.left)

                if node.right is not None:
                    deq.append(node.right)

        return level_stack[::-1]


if __name__ == "__main__":
    sol = Solution()

    root = TreeNode(4, TreeNode(5, TreeNode(5), TreeNode(7)), TreeNode(10))
    assert sol.traverse(root) == [[5, 7], [5, 10], [4]]

    root = TreeNode(9)
    assert sol.traverse(root) == [[9]]

    root = TreeNode(
        1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(7))
    )
    assert sol.traverse(root) == [[4, 5, 6, 7], [2, 3], [1]]

    print("All test cases passed.")
