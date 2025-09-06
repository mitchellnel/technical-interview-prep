from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    def findSuccessor(self, root, key):
        if root is None:
            return None

        queue = deque()
        queue.append(root)

        next_node_is_successor = False
        while queue:
            node = queue.popleft()

            if next_node_is_successor:
                return node

            if node.val == key:
                next_node_is_successor = True

            if node.left is not None:
                queue.append(node.left)

            if node.right is not None:
                queue.append(node.right)

        return None


if __name__ == "__main__":
    sol = Solution()

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    assert sol.findSuccessor(root, 3).val == 4
    assert sol.findSuccessor(root, 4).val == 5
    assert sol.findSuccessor(root, 5).val == 6
    assert sol.findSuccessor(root, 6).val == 7
    assert sol.findSuccessor(root, 7) is None

    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    assert sol.findSuccessor(root, 12).val == 7
    assert sol.findSuccessor(root, 9).val == 10
    assert sol.findSuccessor(root, 7).val == 1
    assert sol.findSuccessor(root, 1).val == 9
    assert sol.findSuccessor(root, 10).val == 5
    assert sol.findSuccessor(root, 5) is None

    print("All test cases passed.")
