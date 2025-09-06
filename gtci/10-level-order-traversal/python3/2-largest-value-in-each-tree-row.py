from typing import List
from collections import deque


# Definition for a binary tree node
class TreeNode:
    def __init__(self, val: int, left: "TreeNode" = None, right: "TreeNode" = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Method to find the largest value in each row of the binary tree
    def largestValues(self, root: TreeNode) -> List[int]:
        result = []

        queue = deque()
        queue.append(root)

        while queue:
            level_size = len(queue)
            max_level_val = float("-inf")

            for _ in range(level_size):
                node = queue.popleft()

                max_level_val = max(max_level_val, node.val)

                if node.left is not None:
                    queue.append(node.left)

                if node.right is not None:
                    queue.append(node.right)

            result.append(max_level_val)

        return result


if __name__ == "__main__":
    sol = Solution()

    root = TreeNode(4, TreeNode(5, TreeNode(5), TreeNode(7)), TreeNode(10))
    assert sol.largestValues(root) == [4, 10, 7]

    root = TreeNode(9)
    assert sol.largestValues(root) == [9]

    root = TreeNode(
        1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(7))
    )
    assert sol.largestValues(root) == [1, 3, 7]

    root = TreeNode(
        7,
        TreeNode(4, TreeNode(2, TreeNode(3)), TreeNode(5)),
        TreeNode(8, None, TreeNode(9)),
    )
    assert sol.largestValues(root) == [7, 8, 9, 3]

    print("All test cases passed.")
