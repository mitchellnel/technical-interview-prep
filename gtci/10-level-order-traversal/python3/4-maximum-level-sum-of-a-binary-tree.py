from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxLevelSum(self, root):
        if root is None:
            return 0

        queue = deque()
        queue.append(root)

        max_sum = float("-inf")
        max_sum_level = 0

        level = 0
        while queue:
            level += 1
            level_size = len(queue)

            level_sum = 0
            for _ in range(level_size):
                node = queue.popleft()

                level_sum += node.val

                if node.left is not None:
                    queue.append(node.left)

                if node.right is not None:
                    queue.append(node.right)

            if level_sum > max_sum:
                max_sum = level_sum
                max_sum_level = level

        return max_sum_level


if __name__ == "__main__":
    sol = Solution()

    # Test case 1
    root1 = TreeNode(1)
    root1.left = TreeNode(7)
    root1.right = TreeNode(0)
    root1.left.left = TreeNode(7)
    root1.left.right = TreeNode(-8)
    assert sol.maxLevelSum(root1) == 2

    # Test case 2
    root2 = TreeNode(989)
    root2.right = TreeNode(10250)
    root2.right.left = TreeNode(98693)
    root2.right.right = TreeNode(-89388)
    root2.right.right.right = TreeNode(-32127)
    assert sol.maxLevelSum(root2) == 2

    print("All test cases passed.")
