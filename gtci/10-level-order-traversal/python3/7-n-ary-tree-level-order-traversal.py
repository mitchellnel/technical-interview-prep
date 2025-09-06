from collections import deque


class NAryNode:
    def __init__(self, val=0, children=None):
        self.val = val
        self.children = children if children is not None else []


class Solution:
    def levelOrder(self, root):
        if root is None:
            return []

        traversal = []

        queue = deque()
        queue.append(root)

        while queue:
            level_size = len(queue)

            level = []
            for _ in range(level_size):
                node = queue.popleft()

                level.append(node.val)

                if node.children:
                    queue.extend(node.children)

            traversal.append(level)

        return traversal


if __name__ == "__main__":
    sol = Solution()

    root1 = NAryNode(1)
    root1.children = [NAryNode(3), NAryNode(2), NAryNode(4)]
    root1.children[0].children = [NAryNode(5), NAryNode(6)]
    assert sol.levelOrder(root1) == [[1], [3, 2, 4], [5, 6]]

    root2 = NAryNode(1)
    assert sol.levelOrder(root2) == [[1]]

    root3 = None
    assert sol.levelOrder(root3) == []

    root4 = NAryNode(10)
    root4.children = [NAryNode(15), NAryNode(12)]
    root4.children[0].children = [NAryNode(20)]
    root4.children[1].children = [NAryNode(25)]
    root4.children[0].children[0].children = [NAryNode(30), NAryNode(40)]
    assert sol.levelOrder(root4) == [[10], [15, 12], [20, 25], [30, 40]]

    print("All test cases passed.")
