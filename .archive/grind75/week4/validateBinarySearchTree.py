from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.isValidBSTHelper(root)

    def isValidBSTHelper(
        self,
        node: Optional[TreeNode],
        floor: int = float("-inf"),
        ceiling: int = float("inf"),
    ) -> bool:
        # base case
        if node is None:
            return True

        # validate node using floor and ceiling params
        if node.val <= floor or node.val >= ceiling:
            return False

        return self.isValidBSTHelper(
            node.left, floor, node.val
        ) and self.isValidBSTHelper(node.right, node.val, ceiling)
