from collections import deque

# class TreeNode:
#  def __init__(self, val):
#    self.val = val
#    self.left, self.right, self.next = None, None, None


class Solution:
    def connect(self, root):
        if root is None:
            return None

        queue = deque([root])

        while queue:
            node = queue.popleft()

            if node.left is not None:
                queue.append(node.left)

            if node.right is not None:
                queue.append(node.right)

            if not queue:
                node.next = None
            else:
                node.next = queue[0]

        return root
