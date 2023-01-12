# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        return self.getHeight(root) != -1

    def getHeight(self, root):
        if root is None:
            return 0

        left_height = self.getHeight(root.left)
        right_height = self.getHeight(root.right)

        if left_height < 0 or right_height < 0 or abs(left_height - right_height) > 1:
            return -1

        return max(self.getHeight(root.left), self.getHeight(root.right)) + 1
